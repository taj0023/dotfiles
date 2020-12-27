#!/usr/bin/env python3
from turtle import *

window = Screen()
window.title = "Nice"
window.screensize(500, 500, 'blue')

one = Turtle()

def start(num):
    one.up()
    if num == 1:
        one.goto(250, 250)
        one.down()
        one.forward(50)

# start(1)
