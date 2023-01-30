import tkinter
from tkinter import *
l=1
p = 0
hi =  tkinter.Tk()
downarrow = PhotoImage(file=r"D:/Applications/Python/Button-Game/button_down.png")
uparrow = PhotoImage(file=r"D:/PC/Pictures/Saved Pictures/button_up.png")
def up():
    global l
    l +=1
    screen.after(1, testscreen)
hi.withdraw()
def down():
    global l
    l-=1
    screen.after(1, testscreen)
def testscreen():
    global p
    p += 1
    global screen
    screen = Toplevel(hi)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(screen,text=l,font=('Calibri', 26)).pack()
    if l ==5:
        Label(screen,text="5 minutes is the max you can go!",font=('Times', 26)).pack()
    if l < 5:
        Button(screen, image=uparrow,command=up,width=300,height=200, pady=10).pack()
    if l == 1:
        Label(screen,text="1 minute is the lowest you can go!",font=('Times', 26)).pack()
    if l> 1:
        Button(screen, image=downarrow,command=down,width=300,height=200, pady=10).pack()
    Button(screen,text="Confirm", command=countdown).pack()
    Label(screen,text="Remember, this is measured in minutes!").pack()
    screen.mainloop()
import tkinter
from tkinter import *
import time
def countdown():
    global l
    t = l
    while t:
        mins, secs = divmod(t, 60)
        print(l, end="\r")
        time.sleep(1)
        t -= 0.0166666667
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
global all
testscreen()