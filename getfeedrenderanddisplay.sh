#!/bin/bash

CWD='~/frame/html' # path to your feeds.py
python3 $CWD/feeds.py
filename='feed.htm' # output name of the html file
chromium-browser  --window-size=600,448 --hide-scrollbars --screenshot=~/frame/html/screenshot.png --headless file://$CWD/$filename
~/frame/html/image.py ~/frame/html/screenshot.png
