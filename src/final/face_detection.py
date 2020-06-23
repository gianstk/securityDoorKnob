'''
This is the testing code for simple facial detection with default HAAR Cascade front face
'''

import sys
import cv2

# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)

#faceCascade = cv2.CascadeClassifier('classifier.xml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



video_capture = cv2.VideoCapture(0)

i = 0
while True:
    # Capture frame-by-frame from video source
    ret, frame = video_capture.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
        # flags = cv2.CASCADE_SCALE_IMAGE
        # flags=cv2.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print("FACE DETECTED!", i)
        i += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()