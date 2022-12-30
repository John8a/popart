import sys
import os
from PIL import Image
import remove_background as rb
import popart as pa
import add_color_bg as acb

# 1. remove background & crop image
# 2. add color background
# 3. create popart

if __name__ == '__main__':
    print("Starting program...")
    if len(sys.argv) < 2:
        print("»» Usage: python remove_background.py INPUT_PATH")
        sys.exit(1)
    
    # get input path and extra flag
    input_path = sys.argv[1]
    try:
        extra_flag = sys.argv[2]
    except:
        extra_flag = None

    # reduce image size
    image = Image.open(input_path)
    image.save(input_path, optimize=True, quality=95)

    # get image file size in mb
    file_size = os.path.getsize(input_path) / 1000000
    print("» File size: " + str(file_size) + " MB")

    print("» Received File: " + input_path)
    result_path = "results/" + input_path.split('.')[0].split('/')[1] + '_result.png'

    if extra_flag == '1':
        print("» Choosing colors...")
        acb.select_color(input_path, 1)
        print("» Creating popart...")
        pa.create_popart(result_path)
        sys.exit(0)

    print("» Removing background...")
    rb.remove_background(input_path)
    print("» Adding color background...")
    input_path = input_path.split('.')[0] + '.png'
    acb.select_color(input_path)
    print("» Creating popart...")
    pa.create_popart(result_path)