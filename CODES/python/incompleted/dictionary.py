#!/usr/bin/env python3
import PyDictionary
from tkinter import *

root = Tk()
root.title("Dictionary!")
root.geometry("500x500")

d = PyDictionary.PyDictionary()

UNDERLINE = '\033[4m'
END = '\033[0m'

def get_meaning():
	word = entry.get()
	# string = ""
	try:
		for k, v in d.meaning(word).items():
			string = f"\n{k}: \n{''.join(v)}\n"
			# string += "\n" + k + ": \n" + "\n".join(v) + "\n"
		t.insert(END, string)
	except:
		t.insert(END, "NO MEANING FOUND")
	# for i in d.meaning(word).items():
	# 	t.insert(END, i[0] + "\n" + ", ".join(i[1]))


label = Label(root, text="ENTER YOUR WORD BELOW :-")
label.pack()

entry = Entry(root, width=50)
entry.pack()

b = Button(root, width=20, text="Get Meaning", command=get_meaning)
b.pack()


t = Text(root)
t.pack()





root.mainloop()