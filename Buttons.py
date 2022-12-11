import tkinter
from tkinter import *
import random
n = 0
x = 0
s = 0
c = 0
l = 0
score = 0
e = random.randint(0,800)
f = random.randint(1,1560)
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver():
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen)
    screen2.geometry("1560x800")
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Quit & Retry", command=Retry).pack()
def Retry():
    global c
    c+=1
    global x
    if x >= 1:
        score == 0
    global s
    s+=1
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("1560x800")
    screen3.title("Buttons, and more buttons!")
    Label(screen3,text = "Lets  play a game!").pack()
    Label(screen3,text = "").pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !', command = Score)
    global e
    global f
    btn1.place(x=f, y=e)
    Button(screen3,text="DONT CLICK ME!",command=GameOver).pack()
def Buttons():
    global screen
    screen = tkinter.Tk()
    screen.geometry("1560x800")
    screen.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn
    btn = Button(screen, text = 'Click me !', command = Score)
    global e
    global f
    btn.place(x=f, y=e)
    Label(text = "").pack()
    Button(text="DONT CLICK ME!",command=GameOver).pack()
    screen.mainloop()
def Score():
    global s
    if s >= 1:
        global x
        x +=1
    global c
    if c != 1:
        x = 0
    global l
    if x == 1 and l == 1:
        global score
        score = 0
    global n
    n+=1
    if n == 1:
        score = 0
        score  = score + 1
        print(score)
    else:
        if l == 2:
            score= score+1
            print (score)
            global e
            global f
            e = random.randint(0,800)
            f = random.randint(1,1560)
            btn1.place(x=f, y=e)
        score= score+1
        print (score)
        e = random.randint(0,800)
        f = random.randint(1,1560)
        btn.place(x=f, y=e)
    c = 0
global all
Buttons()