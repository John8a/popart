import cv2
from colorama import Fore

weights = "ssd_mobilenet/frozen_inference_graph.pb"
model = "ssd_mobilenet/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"

# load the MobileNet SSD model trained  on the COCO dataset
net = cv2.dnn.readNetFromTensorflow(weights, model)

def get_cropped_image(image_path):
    # get current working directory
    image = cv2.imread(image_path)
    image_path = image_path.split('.')[0] + '.png'
    # image detection
    h = image.shape[0]
    w = image.shape[1]
    blob = cv2.dnn.blobFromImage(image, 1.0/127.5, (320, 320), [127.5, 127.5, 127.5])

    # pass the blog through our network and get the output predictions
    net.setInput(blob)
    output = net.forward() 
    # get every detection in the output and cut the image if probability is greater than 0.5
    for detection in output[0, 0, :, :]:
        probability = detection[2]
        if probability < 0.5:
            continue

        # print class name (person, cat, dog, etc.)
        class_name = detection[1]
        with open("ssd_mobilenet/coco_names.txt", "r") as f:
            coco_names = f.read().split("\n")
        print("» Recognized as:", Fore.RED + coco_names[int(class_name) - 1] + Fore.RESET)

        # create a box around the object
        box = [int(a * b) for a, b in zip(detection[3:7], [w -  (w * 0.2), h - (h * 0.2), w + (w * 0.05), h + (h * 0.05)])] # box = [int(a * b) for a, b in zip(detection[3:7], [w, h, w, h])]
        # check if the box is inside the image
        if box[0] < 0:
            box[0] = 0
        if box[1] < 0:
            box[1] = 0
        if box[2] > w:
            box[2] = w
        if box[3] > h:
            box[3] = h
        box = tuple(box)


        # crop the image
        image = image[box[1]:box[3], box[0]:box[2]]
    
    cv2.imwrite(image_path, image)
    return image_path