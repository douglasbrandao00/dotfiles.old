#!/usr/bin/env bash 

lxsession &
picom &
volumeicon &
nm-applet &
nitrogen --restore  &
xrandr --output HDMI-1 --left-of eDP-1
 
