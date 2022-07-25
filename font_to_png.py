# coding: utf-8
"""
Convert Font file (ex: .ttf) to PNG file (224 x 224)
"""
import os
import re
import sys
import shutil
from PIL import Image, ImageDraw, ImageFont


def font2png(
    font_name: str, 
    font_size: int, 
    background_color: str, 
    font_color: str, 
    word: str,
) -> None:
    """Create picture from fonttype"""

    # Font
    font = ImageFont.truetype(
        f"fonts/{font_name}", 
        font_size, 
        encoding="utf-8",
    )

    # Image
    image = Image.new(
        "RGB", 
        (font_size, font_size), 
        background_color,
    )
    draw = ImageDraw.Draw(image)

    # Position
    _w, _h = draw.textsize(word, font=font)
    offset_w, offset_h = font.getoffset(word)
    offset_w += _w
    offset_h += _h
    
    pos = (
        (font_size-offset_w) / 2, 
        (font_size-offset_h) / 2,
    )

    # Draw
    draw.text(pos, word, font_color, font=font)

    # Save png file
    for item in image.getdata():
        if item != (0, 0, 0):
            image_id = len(os.listdir(f"images/{word}/")) + 1
            # if len(os.listdir(f"images/{word}/")) >= 1:
            #     max_num = max([int(re.sub(r"\.png", "", png)) for png in os.listdir(f"images/{word}/")])
            #     max_num += 1
            # else:
            #     max_num = 1

            print(word, image_id)
            image.save(f"images/{word}/{image_id}.png")
            break


def main() -> None:
    """Entry point"""

    # Check the "fonts" existed
    if "fonts" not in os.listdir("./"):
        print("Error! You have no \"./fonts/\" folder.\nMaybe you can execute `bash donwload.sh` to get some example.")
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
            try:
                font2png(font_name, font_size, background_color, font_color, word)
            except OSError as e:
                print(f"An Error occurred. {e}")

if __name__ == '__main__':
    main()
