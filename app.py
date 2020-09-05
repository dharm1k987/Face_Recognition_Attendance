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