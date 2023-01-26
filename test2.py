import tkinter
from tkinter import *
l=5
p = 0
hi =  tkinter.Tk()
downarrow = PhotoImage(file=r"D:/Applications/Python/Button-Game/button_down.png")
uparrow = PhotoImage(file=r"D:/PC/Pictures/Saved Pictures/button_up.png")
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
    Label(screen,text=l).pack()
    Button(screen, image=downarrow,command=down,width=300,height=200, pady=10).pack()
    Button(screen, image=uparrow,command=down,width=300,height=200, pady=10).pack()
    screen.mainloop()
global all
testscreen()