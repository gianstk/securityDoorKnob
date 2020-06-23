"""
resource: https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/
This program converts color images into grey scale

"""

import cv2
import os

# def convert_to_grey(src_addr, des_addr):
#     # for i in range(1,room_number+1):    
#     for image_name in os.listdir(src_addr):
#         img_addr = src_addr + image_name
#         image = cv2.imread(img_addr)
#         grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
#         # cv2.imshow('Original image',image)
#         # cv2.imshow('Gray image', grey)        

#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#         store_addr = des_addr + image_name
#         cv2.imwrite(store_addr, grey)

def convert_to_grey(src_addr, des_addr):
	for img_name in os.listdir(src_addr):
		print(img_name)
		img = cv2.imread(src_addr + img_name)
		# print(img)
		grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cv2.imwrite(des_addr+img_name, grey)

# positive image addr
pos_color_addr = 'train_image/pos_color/'
pos_grey_addr = 'train_image/pos_grey/'

# convert positive photo to grey scale
convert_to_grey(pos_color_addr, pos_grey_addr)