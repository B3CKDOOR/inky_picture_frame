#!/usr/bin/env python3

import sys
import subprocess
import os
import time
from PIL import Image
from pathlib import Path
from inky.auto import auto

testmode_file = Path("/frame/testmode.txt")
if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    from inky.inky_ssd1608 import Inky #Inky phat for debugging
    display = InkyPHAT('yellow')
    display.set_border(inky.YELLOW)
    print("TESTING SETUP DETECTED")
else:
    from inky.inky_uc8159 import Inky #Inky impression
    display.set_border(inky.WHITE)


inky = Inky()
saturation = 0.5

timestamp=str(int(time.time()))

if len(sys.argv) == 1:
    print("""
Usage: {file} image-file
""".format(file=sys.argv[0]))
    sys.exit(1)

imageargument = sys.argv[1]

newimage=imageargument+'-'+timestamp+'.jpg'

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    os.system('convert -resize 250x122 -auto-orient '+imageargument+' -gravity center -background white -extent 250x122 '+newimage) # this uses imagemagick to create a 250x122px image.
else:
    os.system('convert -resize 600x448 -auto-orient '+imageargument+' -gravity center -background white -extent 600x448 '+newimage) # this uses imagemagick to create a 600x448px image which is ready to be sent to the picture frame


image = Image.open(newimage)

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    inky.set_image(image)
else:
    inky.set_image(image, saturation=saturation)
inky.show()
os.system('cp '+newimage+ ' /frame/recent.jpg') # copy the file to the recentimage folder. I do that to be able to revert back to the latest image after displaying the current news for a limited time period
