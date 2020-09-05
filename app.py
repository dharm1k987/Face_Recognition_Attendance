import cv2
import numpy as np
import os
from img_encodings import encoding

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

cap = cv2.VideoCapture(0)

# width is id number 3, height is id 4
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# change brightness to 150
cap.set(10, 150)

while True:

    success, img = cap.read()

    cv2.imshow('window', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()