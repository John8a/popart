from PIL import Image, ImageDraw, ImageFont

def add_custom_text(input_path, text):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((0, 0), text, (255, 255, 255), font=font)
    image.save(input_path)