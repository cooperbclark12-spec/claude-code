#!/usr/bin/env bash
# Soft soundtrack for a Northside Reel: warm pad + whooshes on scene changes + pops on accents.
# Usage: make_soundtrack.sh <in.mp4> <out.mp4> <duration_s> "<whoosh times, comma sep>" "<pop times, comma sep>"
set -euo pipefail
IN=$1; OUT=$2; D=$3; WH=${4:-}; POPS=${5:-}
f="aevalsrc='0.10*sin(2*PI*110*t)+0.07*sin(2*PI*164.81*t)+0.06*sin(2*PI*220*t)+0.045*sin(2*PI*277.18*t)+0.03*sin(2*PI*329.63*t)':s=48000:d=$D,volume='0.9+0.1*sin(2*PI*0.25*t)':eval=frame,lowpass=f=1800,afade=t=in:st=0:d=1.5,afade=t=out:st=$(echo "$D-2" | bc):d=2[s0];"
n=1; labels="[s0]"
for t in ${WH//,/ }; do ms=$(echo "$t*1000/1" | bc); f+="anoisesrc=c=pink:a=0.3:d=0.8:s=48000,bandpass=f=900:w=1200,afade=t=in:d=0.4,afade=t=out:st=0.4:d=0.4,adelay=$ms|$ms,apad=whole_dur=$D[s$n];"; labels+="[s$n]"; n=$((n+1)); done
for t in ${POPS//,/ }; do ms=$(echo "$t*1000/1" | bc); f+="aevalsrc='0.22*sin(2*PI*880*t)*exp(-9*t)':s=48000:d=0.4,adelay=$ms|$ms,apad=whole_dur=$D[s$n];"; labels+="[s$n]"; n=$((n+1)); done
f+="${labels}amix=inputs=$n:normalize=0,alimiter=limit=0.8,atrim=0:$D[out]"
ffmpeg -v error -y -i "$IN" -filter_complex "$f" -map 0:v -map "[out]" -c:v libx264 -crf 22 -preset slow -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$OUT"
ffmpeg -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2
