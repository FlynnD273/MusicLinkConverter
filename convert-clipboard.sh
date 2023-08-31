#!/usr/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

echo -n $("$SCRIPTPATH/.venv/bin/python" ~/Documents/MusicLinkConverter/convert.py $(xclip -o -selection clipboard)) | xclip -i -selection clipboard
