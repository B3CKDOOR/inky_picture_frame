#!/usr/bin/env python3

import sys
import subprocess
import os
import time
from PIL import Image
from pathlib import Path
from inky.auto import auto
from inky import InkyPHAT
import shutil

testmode_file = Path("/frame/testmode.txt")

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    from inky.inky_ssd1608 import Inky  # Inky phat for debugging
    print("TESTING SETUP DETECTED")
else:
    from inky.inky_uc8159 import Inky  # Inky impression
    saturation = 0.5

inky = Inky()
timestamp = str(int(time.time()))

if len(sys.argv) == 1:
    print(""" Usage: {file} image-file """.format(file=sys.argv[0]))
    sys.exit(1)

image_argument = sys.argv[1]

new_image = image_argument + '-' + timestamp + '.jpg'

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    subprocess.run(['convert', '-resize', '250x122', '-auto-orient', image_argument, '-gravity', 'center', '-background', 'white', '-extent', '250x122', new_image], check=True)
    # this uses imagemagick to create a 250x122px image.
else:
    subprocess.run(['convert', '-resize', '600x448', '-auto-orient', image_argument, '-gravity', 'center', '-background', 'white', '-extent', '600x448', new_image], check=True)
    # this uses imagemagick to create a 600x448px image which is ready to be sent to the picture frame

image = Image.open(new_image)

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

if testmode_file.is_file():
    # Are we in test mode with a Inky PHat?
    display = InkyPHAT('yellow')
    display.set_border(inky.YELLOW)
    inky.set_image(image)
else:
    inky.set_image(image, saturation=saturation)
    inky.show()

# Copy the file to the recentimage folder. I do that to be able to revert back to the latest image after displaying the current news for a limited time period
shutil.copy(new_image, '/frame/recent.jpg')
