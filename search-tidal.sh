#!/usr/bin/bash

echo -n $(python ~/Documents/MusicLinkConverter/search-tidal.py "$*") | xclip -i -selection clipboard
