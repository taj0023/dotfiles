#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

url = 'https://docs.parrotlinux.org/mirror-list/'

sauce = requests.get(url).text

soup = BeautifulSoup(sauce, 'lxml')

stuff = soup.find_all('sub')

for each in stuff:
    s = each.text.split()[1]
    if s.startswith('http'):
        print(str(requests.get('http://mirror.amberit.com.bd/parrotsec/').elapsed.total_seconds()).ljust(8), s)
