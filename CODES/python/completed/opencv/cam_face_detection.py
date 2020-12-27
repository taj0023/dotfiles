#!/usr/bin/env python3
import cv2 as cv
import time

video = cv.VideoCapture(0)
# face_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

a = 0

while True:
	a += 1
	check, frame = video.read()
# 	print(frame)

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

	for x,y,w,h in faces:
		image = cv.rectangle(gray, (x,y), (x+h, y+w), (0, 255, 0), 3)
	cv.imshow('showing image', gray)
	key = cv.waitKey(1)

	if key == ord('q'):
		break

print(a)

video.release()
cv.destroyAllWindows()
