from PIL import Image, ImageEnhance
import random
import os

colors = [
    ['#d60f84', '#68c1c9', '#FDE6B0', '#fb1d36', '#9697c0', '#B1BCAE']
    # ['#FF0000', '#FFFF00', '#00FF00', '#0000FF', '#FF00FF', '#00FFFF']
]

def add_bg(input_path, output_path, color):
    img = Image.open(input_path)
    # fill_color = (120, 8, 220)  # your new background color
    fill_color = color

    img = img.convert("RGBA")   # it had mode P after DL it from OP
    # make img gray
    # img = ImageEnhance.Color(img).enhance(0.0)
    if img.mode in ('RGBA', 'LA'):
        background = Image.new(img.mode[:-1], img.size, fill_color)
        background.paste(img, img.split()[-1]) # omit transparency
        img = background

    img.convert("RGB").save(output_path)

def select_color(input_path, flag=0):
    color_section = random.choice(colors)
    for i in range(0, 4):
        color = random.choice(color_section)
        add_bg(input_path, "intermediate/image" + str(i) + ".png", color)
        color_section.pop(color_section.index(color))
    
    if flag == 0:
        os.remove(input_path)
    