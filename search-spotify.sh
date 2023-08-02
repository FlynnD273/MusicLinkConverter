#!/usr/bin/bash

echo -n $(python ~/Documents/MusicLinkConverter/search-spotify.py $@) | xclip -i -selection clipboard
