#!/usr/bin/env bash
# Capture demo.html image par image (Chromium headless) puis assemble
# le GIF (README), le MP4 (réseaux sociaux) et l'aperçu PNG (dernière image).
#   ./rendu.sh       → demo.gif, demo.mp4, apercu.png      (français)
#   ./rendu.sh en    → demo-en.gif, demo-en.mp4, apercu-en.png
set -euo pipefail
cd "$(dirname "$0")"
LANGUE=${1:-fr}
SUFFIXE=$([ "$LANGUE" = fr ] || printf -- "-%s" "$LANGUE")
FPS=${FPS:-25}
DUREE=13
N=$((FPS * DUREE))
TRAVAIL=$(mktemp -d)
trap 'rm -rf "$TRAVAIL"' EXIT
export TRAVAIL FPS LANGUE PAGE="file://$PWD/demo.html"

capture() {  # capture <numéro d'image>
  local i=$1 t
  t=$(awk "BEGIN{printf \"%.3f\", $i/$FPS}")
  # profil jetable par capture : pas de verrou partagé, pas de contact avec le navigateur de l'utilisateur
  timeout 40 chromium --headless=new --disable-gpu --hide-scrollbars --no-first-run \
    --user-data-dir="$TRAVAIL/profil-$i" --window-size=1280,720 \
    --screenshot="$TRAVAIL/$(printf %04d "$i").png" "$PAGE#t=$t&lang=$LANGUE" >/dev/null 2>&1 || true
  rm -rf "$TRAVAIL/profil-$i"
}
export -f capture

seq 0 $((N - 1)) | xargs -P "$(nproc)" -I{} bash -c 'capture {}'
for essai in 1 2 3; do  # nouvel essai pour les captures ratées
  manquantes=$(for i in $(seq 0 $((N - 1))); do [ -s "$TRAVAIL/$(printf %04d "$i").png" ] || echo "$i"; done)
  [ -z "$manquantes" ] && break
  echo "essai $essai : $(echo "$manquantes" | wc -l) image(s) à refaire"
  echo "$manquantes" | xargs -P 4 -I{} bash -c 'capture {}'
done

ffmpeg -y -loglevel error -framerate "$FPS" -i "$TRAVAIL/%04d.png" \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart "demo$SUFFIXE.mp4"
ffmpeg -y -loglevel error -framerate "$FPS" -i "$TRAVAIL/%04d.png" \
  -vf "fps=20,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" \
  "demo$SUFFIXE.gif"
cp "$TRAVAIL/$(printf %04d $((FPS * 115 / 10)))".png "apercu$SUFFIXE.png"
ls -lh "demo$SUFFIXE.gif" "demo$SUFFIXE.mp4" "apercu$SUFFIXE.png"
