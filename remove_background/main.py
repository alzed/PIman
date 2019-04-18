import os
import glob
import remove_bg

input_data = #PATH to the input images folder

masked_data = #Path to the manipulated images folder

for image_path in glob.glob(input_data)
    img = remove_bg.remove_bg(image_path)

    #save to disk
    img_name = image_path.split('/')[-1]
    dest = os.path.join(masked_data, 'masked_' + img_name)
    cv2.imwrite(dest, img)
    