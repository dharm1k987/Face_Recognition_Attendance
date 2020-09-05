import cv2
import numpy as np
import os
from img_encodings import encoding
import time
path = 'train_imgs'
imgs = []
labels = []

for file in os.listdir(path):
    img = cv2.imread(f'{path}/{file}', cv2.COLOR_BGR2RGB)
    imgs.append(img)
    labels.append(file.split('.')[0])

print(labels)

train_encodings = encoding.find_encoding(imgs)
print(len(train_encodings))

frameWidth = 960
frameHeight = 720
frame_rate = 30

cap = cv2.VideoCapture(0)

# width is id number 3, height is id 4
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

# change brightness to 150
# cap.set(10, 150)

prev = 0
RESIZE_FACTOR = 4

while True:
    time_elapsed = time.time() - prev

    success, img = cap.read()

    if time_elapsed > 1. / frame_rate:
        prev = time.time()

        img_resized = cv2.resize(img.copy(), None, fx=1/RESIZE_FACTOR, fy=1/RESIZE_FACTOR)
        img_color = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

        # find current face location and encodings
        face_location, face_encodings = encoding.find_location_and_encoding(img_color)

        # compare each face against the train_imgs
        for face_encode, face_loc in zip(face_encodings, face_location):
            matches, distance = encoding.find_location_and_distance(train_encodings, face_encode)
            best_index = np.argmin(distance)

            # if they exist
            if matches[best_index]:
                name = labels[best_index].upper()
                y1, x2, y2, x1 = list(map(lambda x: x * RESIZE_FACTOR, face_loc))
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0),2)
                cv2.rectangle(img, (x1,y2-35), (x2, y2), (0,255,0), cv2.FILLED)
                cv2.putText(img, name, (x1+5, y2-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

                # print(y1, x2, y2, x1)

        cv2.imshow('result', img)


    wait = cv2.waitKey(1)
    if wait & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()