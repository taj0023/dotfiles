#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import sys
import emoji

def news():
    url = 'http://www.rit.ac.in/'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')

    event_box = soup.find('div', { "style": "vertical-align:top;box-shadow: 4px 4px 15px;border-radius: 10px;padding-left: 20px;padding-right: 20px"})
    events = event_box.text[18:-15].split("Click here")
    return events

def notice_board():
    url = 'http://www.rit.ac.in/noticeboard.php'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
    board = soup.find_all('div', {"style": "overflow:scroll;height:300px;padding-left:20px;box-shadow: 4px 4px 11px;border-radius: 5px;"})[1]
    notices = board.text[1:-2].split("Click here")
    return notices

def main():
    if len(sys.argv) == 1:
        print("Usage: college.py <events/notice>")
    else:
        if sys.argv[1] == 'events':
            events = news()
            emo =  emoji.emojize(":ribbon:")
            for event in events:
                print(emo+"-> "+event+".")
        elif sys.argv[1] == 'notice':
            notices = notice_board()
            emo =  emoji.emojize(":ribbon:")
            for notice in notices:
                print(emo+"-> "+notice+".")
        else:
            print("INVALID!")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print(emoji.emojize(':no_mobile_phones:') + " Check your Connection!"+ emoji.emojize(':no_mobile_phones:'))