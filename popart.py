import cv2 as cv
import numpy as np
from colorama import Fore

def create_popart(filename):
    # Read the smaller images
    image1 = cv.imread('intermediate/image0.png')
    image2 = cv.imread('intermediate/image1.png')
    image3 = cv.imread('intermediate/image2.png')
    image4 = cv.imread('intermediate/image3.png')

    # Get the sizes of the smaller images
    height1, width1, _ = image1.shape
    height2, width2, _ = image2.shape
    height3, width3, _ = image3.shape
    height4, width4, _ = image4.shape

    # Calculate the size of the new image
    total_height = height1 * 2
    total_width = width1 * 2

    # Create a new image with the desired size and color depth
    new_image = np.zeros((total_height, total_width, 3), np.uint8)

    # Paste the smaller images into the new image at the desired positions
    new_image[0:height1, 0:width1] = image1
    new_image[0:height2, width1:width1 + width2] = image2
    new_image[height1:height1 + height3, 0:width3] = image3
    new_image[height1:height1 + height4, width3:width3 + width4] = image4
    new_image = cv.xphoto.oilPainting(new_image, int(4 * (height1 / 512)), 1)

    # Save the new image to a file
    cv.imwrite(filename, new_image)
    print("» " + Fore.GREEN + "Popart created at: " + filename + Fore.RESET)