#!/usr/bin/env python3
from selenium import webdriver
import keyboard

movie = input("\033[4mEnter name of movie\033[0m : ")

driver = webdriver.Chrome()

driver.get('https://opensubtitle.info/Bad-Boys-for-Life-2020-Subtitles')
# driver.find_element_by_xpath('//*[@id="q"]').send_keys(movie)
# keyboard.press_and_release('enter')

