#!/usr/bin/env bash
# Capture demo.html image par image (Chromium headless) puis assemble
# demo.gif (README), demo.mp4 (réseaux sociaux) et apercu.png (dernière image).
set -euo pipefail
cd "$(dirname "$0")"
FPS=${FPS:-25}
DUREE=13
IMAGES=$(mktemp -d)
trap 'rm -rf "$IMAGES"' EXIT
N=$((FPS * DUREE))
seq 0 $((N - 1)) | xargs -P "$(nproc)" -I{} sh -c '
  t=$(awk "BEGIN{printf \"%.3f\", {}/'"$FPS"'}")
  chromium --headless=new --disable-gpu --hide-scrollbars --window-size=1280,720 \
    --screenshot="'"$IMAGES"'/$(printf %04d {}).png" "file://'"$PWD"'/demo.html#t=$t" 2>/dev/null'
ffmpeg -y -loglevel error -framerate "$FPS" -i "$IMAGES/%04d.png" \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart demo.mp4
ffmpeg -y -loglevel error -framerate "$FPS" -i "$IMAGES/%04d.png" \
  -vf "fps=20,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" \
  demo.gif
chromium --headless=new --disable-gpu --hide-scrollbars --window-size=1280,720 \
  --screenshot="$PWD/apercu.png" "file://$PWD/demo.html#t=11.5" 2>/dev/null
ls -lh demo.gif demo.mp4 apercu.png
