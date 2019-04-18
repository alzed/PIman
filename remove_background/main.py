import os
import cv2
import remove_bg
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-src", "--source", required=True, help="Path to images source folder")
ap.add_argument("-dst", "--destination", required=True, help="Path to images destination folder")

args = vars(ap.parse_args())

input_data = args["source"]
output_data = args["destination"]

for image in os.listdir(input_data):
    image_path = os.path.join(input_data, image)
    img = remove_bg.remove_bg(image_path)

    #save to disk
    dest = os.path.join(output_data, 'masked_' + image)
    cv2.imwrite(dest, img)
