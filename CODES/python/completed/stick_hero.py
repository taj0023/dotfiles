#!/usr/bin/env python3
from ppadb.client import Client
from PIL import Image
import numpy as np
import cv2 as cv
import time

adb = Client('127.0.0.1', 5037)
device = adb.device('ffd4c1ed')

# device.shell('input touchscreen swipe 500 500 500 500 500')

while True:
	image = device.screencap()
	with open('screen.png', 'wb') as f:
		f.write(image)
	#(2340, 1080)
	image = np.array(cv.imread('screen.png',0), dtype = 'uint8')
	# cv.imshow("thenga",image[1790:1791,:])
	# cv.waitKey(0)
	# cv.destroyAllWindows()
	transitions = []
	black = True
	ignore = True
	for i,p in enumerate(image[1800:1801,:][0]):
		if ignore and p != 0:
			continue
		ignore = False

		if black and p != 0:
			black = not black
			transitions.append(i)
			continue
		if not black and p == 0:
			black = not black
			transitions.append(i)
			continue

	start, target1, target2 = transitions
	gap = target1-start
	target = target2 - target1
	d = (gap +target/2) * 0.98

	device.shell(f'input touchscreen swipe 500 500 500 500 {int(d)}')
	time.sleep(3)