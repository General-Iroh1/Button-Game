import tkinter
from tkinter import *
import time
def countdown(t):
    
    while t:
        
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(screen,text="hi").pack()
    Button(screen,text="start timer", command=countdown).pack()
  
  
# input time in seconds
t = l
def testscreen():
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(screen,text="hi").pack()
    Button(screen,text="start timer", command=countdown).pack()
  
# function call
countdown(int(t))

global all
testscreen()