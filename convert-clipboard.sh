#!/usr/bin/bash

echo -n $($(get-python.sh) ~/Documents/MusicLinkConverter/convert.py $(xclip -o -selection clipboard)) | xclip -i -selection clipboard
