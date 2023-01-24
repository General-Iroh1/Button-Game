import tkinter
from tkinter import *
l = 5
p = 0
def down():
    global l
    l-=1
    screen.update()
def testscreen():
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    button_down =PhotoImage('button_down')
    Label(screen,text=l).pack()
    Button(screen,image=(button_down), command=down,width=1000,height=1000, pady=100).pack()
    screen.mainloop()
global all
testscreen()