#!/usr/bin/env bash

echo -n `python ~/Documents/MusicLinkConverter/convert.py `xclip -o -selection clipboard`` | xclip -i -selection clipboard
