#!/usr/bin/bash

echo -n $($(get-python.sh) ~/Documents/MusicLinkConverter/search-tidal.py "$*") | xclip -i -selection clipboard
