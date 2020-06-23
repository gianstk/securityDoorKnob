import cv2


def create_dataset(img, id, img_id):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # specify result directory
    cv2.imwrite("face_img/pic." + str(id) + "." + str(img_id) + ".jpg", img)



def draw_rect(img, classifier, scaleFactor, minNeighbours, color, text):

    gray = cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbours)
    coords = []

    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        coords = [x,y,w,h]
    return img, coords

def detect(img, faceCascade, img_id):
    img, coords = draw_rect(img, faceCascade, 1.1, 10, (0,255,0), "Face")

    # create image only when there's a detection!
    if len(coords) == 4:
        #id of the dataset
        id = 1
        crop_img = img[
            coords[1]: coords[1] + coords[3],
            coords[0]: coords[0] + coords[2]
            ]
        create_dataset(crop_img, id, img_id)
    return img


# main
img_id = 0
video_capture = cv2.VideoCapture(0) 

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (True):
    ret, frame = video_capture.read()
    frame = detect(frame, faceCascade, img_id)
    cv2.imshow('frame', frame)
    img_id += 1
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()


