import numpy as np
import os, cv2
# python image library
from PIL import Image

def train_classifier(data_dir):
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    
    faces = []
    ids = []

    for image in path:
        if image == data_dir + '.DS_Store':
            continue
        if image == data_dir + '.AppleDouble':
            continue
        # convert each image to greyscale
        # convert into numpy array as "unsigned int 8-bit"
        img = Image.open(image).convert("L")
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids)
    # train model with assigned id
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.xml")




#-------------------------- MAIN --------------------------
addr = "face_img/"
train_classifier(addr)