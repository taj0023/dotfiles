#!/usr/bin/env python3
import cv2 as cv
from ppadb.client import Client
import time

adb = Client('127.0.0.1', 5037)
device = adb.device('ffd4c1ed')

while True:
	image = device.screencap()
	with open('screen.png', 'wb') as f:
		f.write(image)

	image = cv.imread('screen.png', 1)[1789:1790,:]

	distance_to_red = 0
	blacks = []
	for i in image[0][1:]:
		if i[2] > 200:
			break
		else:
			distance_to_red += 1

	for j in image[0][1:]:
		if j[0] == 0:
			blacks.append('n')
		else:
			break

	distance = (distance_to_red - len(blacks)) - 3

	device.shell(f'input touchscreen swipe 500 500 500 500 {distance}')
	time.sleep(2.5)