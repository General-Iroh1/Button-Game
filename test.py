from tkinter import *

def countdown():
    global l
    global skreen
    l = 1
    t = l*60
    skreen = Toplevel()
    skreen.attributes('-fullscreen', True)
    skreen.title("Countdown")
    time1 = Label(skreen)
    time1.pack()
    update_screen(skreen, time1, t)
def update_screen(skreen, time1, t):
    if t > 0:
        time1.config(text=t)
        skreen.after(1000, update_screen, skreen, time1, t-1)
    else:
        skreen.destroy()
        screen2 = Toplevel()
        screen2.attributes('-fullscreen', True)
        screen2.title("Buttons, and more buttons!")
        Label(screen2,text="Great job!")
countdown()
global all