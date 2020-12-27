#!/usr/bin/env python3
from tkinter import *
import requests

root = Tk()
root.title("NEW")
root.geometry("500x500")

entry = Entry(root, width=62)
entry.grid(row=0, column=0)

# e2 = Entry(root, width=64)
# e2.grid(row=3, column=0)

t = Text(root, width=58, height=25)
t.grid(row=4, column=0)


def get_data():
	link = entry.get()
	click(link)

def click(url):
	t.insert(END, requests.get(url).text)


get_details = Button(root,text="Get Link", command=get_data)
get_details.grid(row=1, column=0)

root.mainloop()
