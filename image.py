#!/usr/bin/env python3

import sys

from PIL import Image
from pathlib import Path
from inky.auto import auto
from inky import InkyPHAT

testmode_file = Path("/frame/testmode.txt")

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    from inky.inky_ssd1608 import Inky #Inky phat for debugging
    print("TESTING SETUP DETECTED")
else:
    from inky.inky_uc8159 import Inky #Inky impression
    saturation = 0.5

inky = Inky()
saturation = 0.5

if len(sys.argv) == 1:
    print("""
Usage: {file} image-file
""".format(file=sys.argv[0]))
    sys.exit(1)

image = Image.open(sys.argv[1])

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    display = InkyPHAT('yellow')
    display.set_border(inky.YELLOW)
    inky.set_image(image)
else:
    display.set_border(inky.WHITE)
    inky.set_image(image, saturation=saturation)
inky.show()
