#!/usr/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

echo -n $($("$SCRIPTPATH/get-python.sh") ~/Documents/MusicLinkConverter/search-spotify.py "$*") | xclip -i -selection clipboard
