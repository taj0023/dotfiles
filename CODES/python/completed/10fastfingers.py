#!/usr/bin/env python3
import pytesseract, subprocess, cv2, pyautogui, time
for _ in range(16):
    pyautogui.screenshot('thengakola.jpg')
    pyautogui.typewrite(" ".join([i.strip() for i in pytesseract.image_to_string(cv2.imread('thengakola.jpg', 0)[272:380, 219:1072]).split('\n')]), interval=0.005)
    subprocess.run(['rm', 'thengakola.jpg'])

# cropped = image[226:335, 235:978]# cropped = image[272:380, 219:1072]  #custom=cropped=image[278:384, 220:986]
