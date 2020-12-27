#!/usr/bin/env python3
import cv2 as cv
import numpy as np

image = cv.imread('emma.jpg', 1)


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
	image = cv.rectangle(image, (x,y), (x+h, y+w), (0, 255, 0), 3)

resized = cv.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

cv.imshow("Emma", resized)
cv.waitKey(0)
cv.destroyAllWindows()