#!/usr/bin/env bash

python convert.py `xclip -o -selection clipboard` | xclip -i -selection clipboard
