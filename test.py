# -*- coding: utf-8 -*-
"""
This is a simple Python test script.
"""
from PIL import Image, ImageDraw, ImageFont


# Settings
W, H = (256, 256)
word = "毐"


# Font
font = ImageFont.truetype("fonts/DFGangBiStd-W2.otf", 224, encoding='utf-8')


# Image
image = Image.new("RGB", (W, H), "black")
draw = ImageDraw.Draw(image)
offset_w, offset_h = font.getoffset(word)
w, h = draw.textsize(word, font=font)
pos = ((W-w-offset_w)/2, (H-h-offset_h)/2)

# Draw
draw.text(pos, word, "white", font=font)

# Save png file
image.save("{}.png".format(word))

for item in image.getdata():
    if item != (0, 0, 0):
        break
