from rembg import remove
from PIL import Image
import crop_img as ci

def remove_background(input_path):
    output_path = ci.get_cropped_image(input_path)
    input = Image.open(output_path)
    output = remove(input)

    output.save(output_path)