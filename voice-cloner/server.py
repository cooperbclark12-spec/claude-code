"""Minimal voice cloner: a local web UI over the Fish Audio API.

Run:  FISH_API_KEY=... python server.py   then open http://127.0.0.1:8000
The key is read from the environment only and never sent to the browser.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from fishaudio import FishAudio

API_KEY = os.environ.get("FISH_API_KEY")
if not API_KEY:
    raise SystemExit("Set FISH_API_KEY in your environment first.")

client = FishAudio(api_key=API_KEY)
INDEX = (Path(__file__).parent / "index.html").read_bytes()
MAX_UPLOAD = 20 * 1024 * 1024  # 20 MB of reference audio is plenty


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status, obj):
        self._send(status, json.dumps(obj).encode())

    def _body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_UPLOAD:
            raise ValueError("File too large (20 MB max).")
        return self.rfile.read(length)

    def do_GET(self):
        if self.path == "/":
            return self._send(200, INDEX, "text/html; charset=utf-8")
        if self.path == "/api/voices":
            try:
                page = client.voices.list(self_only=True, page_size=50, sort_by="created_at")
                return self._json(200, [{"id": v.id, "title": v.title} for v in page.items])
            except Exception as e:
                return self._json(502, {"error": str(e)})
        self._json(404, {"error": "Not found"})

    def do_POST(self):
        try:
            if self.path == "/api/clone":
                # Raw audio body; the browser has already required the consent tick.
                if self.headers.get("X-Consent") != "yes":
                    return self._json(400, {"error": "Confirm you own this voice or have permission."})
                title = self.headers.get("X-Title", "").strip()[:60] or "My voice"
                voice = client.voices.create(title=title, voices=[self._body()], visibility="private")
                return self._json(200, {"id": voice.id, "title": voice.title})

            if self.path == "/api/speak":
                req = json.loads(self._body() or b"{}")
                text = (req.get("text") or "").strip()
                if not text:
                    return self._json(400, {"error": "Type something to say."})
                audio = client.tts.convert(text=text[:3000], reference_id=req.get("voice_id") or None)
                return self._send(200, audio, "audio/mpeg")
        except ValueError as e:
            return self._json(400, {"error": str(e)})
        except Exception as e:
            return self._json(502, {"error": str(e)})
        self._json(404, {"error": "Not found"})

    def log_message(self, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    print("Voice cloner running at http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
