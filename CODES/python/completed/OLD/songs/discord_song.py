#!/usr/bin/env python3
import time
import pyautogui

time.sleep(5)

with open('/home/taj/CODES/python/completed/songs/songs.txt','r') as songfile:
	songlist = songfile.read().split('\n')
	for song in songlist:
		pyautogui.typewrite('-p ' + song)
		pyautogui.press('Enter')
		time.sleep(1.2)