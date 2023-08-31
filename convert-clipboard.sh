#!/usr/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

echo -n $($("$SCRIPTPATH/get-python.sh") ~/Documents/MusicLinkConverter/convert.py $(xclip -o -selection clipboard)) | xclip -i -selection clipboard
