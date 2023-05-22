#! /bin/bash

tmux ls | cut -d " " -f 1-1 | awk 'BEGIN { ORS = " " } { print }' | sed s/://g
