#!/usr/bin/env python3
import pyautogui
import time

textfile = input("Enter the spam text file: ")

time.sleep(5)

with open(textfile,'r') as lyrics:
	for line in lyrics:
		pyautogui.typewrite(line)
		pyautogui.press("enter")
