import cv2
import time
import pyfirmata




faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def draw_rect(img, classifier, scaleFactor, minNeighbours, color, clf, baseline, detect):
    gray = cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbours)
    coords = []



    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
        id, confidence  = clf.predict(gray[y:y+h, x:x+w])

        # if id==1:
        print(confidence)
        if id == 1 and confidence <= 50:
            cv2.putText(img, "Gian Kongruangkit", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            detect = True
        else:
            cv2.putText(img, "Who is this guy?", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        coords = [x,y,w,h]

        # GPIO write
        if (detect is baseline):
            gpioPin.write(1)
        else:
            gpioPin.write(0)
        
        
        # accuracy information
        if (confidence < 100):
            confidence = "{0}%".format(round(100-confidence))
        else:
            confidence = "{0}%".format(round(100-confidence))
        print(confidence)

    return img, coords

def detect(img, faceCascade, img_id, clf):
    baseline = True
    detect = False
    img, coords = draw_rect(img, faceCascade, 1.1, 10, (0,255,0), clf, baseline, detect)

    # create image only when there's a detection!
    if len(coords) == 4:
        id = 1
        crop_img = img[
            coords[1]: coords[1] + coords[3],
            coords[0]: coords[0] + coords[2]
            ]
        # create_dataset(crop_img, id, img_id)
    return img




# main ------------------------------------------------------------------------
img_id = 0
cap = cv2.VideoCapture(0)

# setup arduino and pin
port = '/dev/tty.usbmodem14101'
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()
gpioPin = board.get_pin('d:12:o')

# setup camera
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

while(True):
    ter, frame = cap.read()
    frame = detect(frame, faceCascade, img_id, clf)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
