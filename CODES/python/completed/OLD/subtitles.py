#!/usr/bin/env python3
from selenium import webdriver
import pyautogui
import time

movie = input("Enter movie name: ")

driver = webdriver.Chrome()

driver.get('https://opensubtitle.info/')
driver.find_element_by_xpath('//*[@id="q"]').send_keys(movie)
pyautogui.press('enter')
driver.find_element_by_xpath('//*[@id="list-group-item-home"]/div/div[2]/h4/strong').click()
driver.find_element_by_xpath('//*[@id="contact-list"]/a[1]/div[1]/span[2]/small/strong').click()
box = pyautogui.confirm('Is this the movie you are looking for?')
if box == 'OK':
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/table/tbody/tr/td[2]/a[1]').click()
	time.sleep(4)
	driver.quit()
	print("--------------------")
	print("Added to ~/Downloads")
	print("--------------------")