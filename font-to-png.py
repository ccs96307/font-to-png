# coding: utf-8
"""
Convert Font file (ex: .ttf) to PNG file (224 x 224)
"""
import os
import re
import shutil
from PIL import Image, ImageDraw, ImageFont


def font2png(W, H, font_name, font_size, bg_color, font_color, word):
    # Font
    font = ImageFont.truetype('fonts/{}'.format(font_name), font_size, encoding='utf-8')

    # Image
    image = Image.new('RGB', (W, H), bg_color)
    draw = ImageDraw.Draw(image)

    offset_w, offset_h = font.getoffset(word)
    w, h = draw.textsize(word, font=font)
    pos = ((W - w - offset_w) / 2, (H - h - offset_h) / 2)

    # Draw
    draw.text(pos, word, font_color, font=font)

    # Save png file
    for item in image.getdata():
        if item != (0, 0, 0):
            if len(os.listdir('images/{}/'.format(word))) >= 1:
                max_num = max([int(re.sub('\.png', '', png)) for png in os.listdir('images/{}/'.format(word))])
                max_num += 1
            else:
                max_num = 1

            print(word, max_num)
            image.save('images/{}/{}.png'.format(word, max_num))
            break


def main():
    # Check the 'fonts' existed
    if 'fonts' not in os.listdir('./'):
        print('Error! You have no "./fonts/" folder.\nMaybe you can execute donwload.sh to get some example.')
        exit()

    # Settings
    words = open('inputs.txt').read().split('\n')
    W, H = (256, 256)
    font_size = 256
    background_color = 'black'
    font_color = 'white'
    font_path = 'fonts/'

    # Remove existed folder
    if 'images' in os.listdir('./'):
        shutil.rmtree('images')

    os.mkdir('images/')

    # Save the font images in echo other folder
    for word in words:
        os.mkdir('images/{}'.format(word))

        for font_name in os.listdir(font_path):
            try:
                font2png(W, H, font_name, font_size, background_color, font_color, word)
            except:
                continue


if __name__ == '__main__':
    main()
