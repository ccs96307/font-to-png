# coding: utf-8
"""
Convert Font file (ex: .ttf) to PNG file (224 x 224)
"""
import os
import re
import sys
import shutil
from PIL import Image, ImageDraw, ImageFont


def font2png(font_name: str, font_size: int, bg_color: str, font_color: str, word: str) -> None:
    """Make picture from font type"""
    # Font
    font = ImageFont.truetype(f"fonts/{font_name}", font_size, encoding="utf-8")

    # Image
    image = Image.new("RGB", (font_size, font_size), bg_color)
    draw = ImageDraw.Draw(image)

    offset_w, offset_h = font.getoffset(word)
    _width, _height = draw.textsize(word, font=font)
    pos = ((font_size - _width - offset_w) / 2, (font_size - _height - offset_h) / 2)

    # Draw
    draw.text(pos, word, font_color, font=font)

    # Save png file
    for item in image.getdata():
        if item != (0, 0, 0):
            if len(os.listdir(f"images/{word}/")) >= 1:
                max_num = max([int(re.sub(r"\.png", "", png)) for png in os.listdir(f"images/{word}/")])
                max_num += 1
            else:
                max_num = 1

            print(word, max_num)
            image.save(f"images/{word}/{max_num}.png")
            break


def main() -> None:
    """Entry point"""
    # Check the "fonts" existed
    if "fonts" not in os.listdir("./"):
        print("Error! You have no \"./fonts/\" folder.\nMaybe you can execute donwload.sh to get some example.")
        sys.exit()

    # Settings
    with open("inputs.txt", "r", encoding="utf-8") as word_file:
        words = word_file.read()

    word_list = words.splitlines()
    font_size = 256
    background_color = "black"
    font_color = "white"
    font_path = "fonts/"

    # Remove existed folder
    if "images" in os.listdir("./"):
        shutil.rmtree("images")

    os.mkdir("images/")

    # Save the font images in echo other folder
    for word in word_list:
        os.mkdir(f"images/{word}")

        for font_name in os.listdir(font_path):
            font2png(font_name, font_size, background_color, font_color, word)


if __name__ == '__main__':
    main()
