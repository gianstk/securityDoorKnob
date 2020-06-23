import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascade.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("train_image/pos_grey/1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=7,
    # minSize=(30, 30),
    # flags = cv2.CASCADE_SCALE_IMAGE
)

for (x,y,w,h) in faces:
    img = cv2.rectangle(gray(x,y), (x+w, y+h), (255,0,0), 2)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows