import tkinter
from tkinter import *
import random
import time
from tkinter import messagebox
def testscreen():
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(screen,text="hi").pack()
def countdown(t):
    
    while t < 6:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    testscreen()
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))

global all
testscreen()