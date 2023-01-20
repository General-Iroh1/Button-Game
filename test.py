import tkinter
from tkinter import *
import random
import time
from tkinter import messagebox
def countdown(t):
    
    while t:
        
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
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