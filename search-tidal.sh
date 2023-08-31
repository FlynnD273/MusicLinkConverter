#!/usr/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

echo -n $("$SCRIPTPATH/.venv/bin/python" ~/Documents/MusicLinkConverter/search-tidal.py "$*") | xclip -i -selection clipboard
