#!/usr/bin/env python3 
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://mobile-tracker-free.com/login/')

browser.find_element_by_xpath('//*[@id="email"]').send_keys('aquibjavedt007@gmail.com')
browser.find_element_by_xpath('//*[@id="password"]').send_keys('bChJrSSt@007')
browser.find_element_by_xpath('//*[@id="btnLogin"]').click()