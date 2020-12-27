#!/usr/bin/env python3
import subprocess as sub
import time


def write():
    import pyautogui as pog
    with open('spam.txt') as f:
        for word in f.read().split():
            pog.typewrite(word + '\n')
            time.sleep(0.5)


def main():
    try:
        write()
    except ModuleNotFoundError:
        sub.run(['pip3', 'install', 'pyautogui'], capture_output=True)
        write()
    except FileNotFoundError:
        f = open('spam.txt', 'w').close()
        print("spam.txt created......\nPut some text inside spam.txt and run this script again!")


if __name__ == '__main__':
    main()
