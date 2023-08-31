#!/usr/bin/bash

echo -n $($(get-python.sh) ~/Documents/MusicLinkConverter/search-spotify.py "$*") | xclip -i -selection clipboard
