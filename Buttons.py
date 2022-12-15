import tkinter
from tkinter import *
import random

#The Screen Is Lava!


n8 = 0
x8 = 0
s8 = 0
c8 = 0
l8 = 1
y8 = 1
z8 = 1
score8 = 0
e8 = random.randint(0,760)
f8 = random.randint(1,1520)
print (e8)
print (f8)
fe8 =str(f8)
ef8 =str(e8)
def GameOver9():
    global l8
    l8 = 1
    if s8>= 1:
        screen38.destroy()
    sscore8 = str(score8)
    global screen28
    screen28=Toplevel(screen58)
    screen28.attributes('-fullscreen', True)
    screen28.title("Game Over!")
    Label(screen28,text="You got a score of "+sscore8).pack()
    Label(screen28,text="Game Over! Better luck next time!").pack()
    Button(screen28,text="Retry", command=Retry9).pack()
    Button(screen28,text="Quit", command=quit).pack()
def Retry9():
    global y8
    y8 = 2
    global l8
    l8+=1
    global c8
    c8+=1
    global x8
    if x8 >= 1:
        score8 == 0
    global s8
    s8+=1
    global screen38
    screen38 = Toplevel(screen58)
    screen38.attributes('-fullscreen', True)
    screen38.title("Buttons, and more buttons!")
    Label(screen38,text = "Lets  play a game!").pack()
    Label(screen38,text = "").pack()
    global btn18
    btn18 = Button(screen38, text = 'Click me !',bg='green', command = Score9)
    global e8
    global f8
    btn18.place(x=f8, y=e8)
    global btn38
    btn38 =Button(screen38,text="DONT CLICK ME!",bg='red',command=GameOver9)
def Buttons9():
    global y8
    y8 = 1
    global screen58
    screen58 = Toplevel(screen)
    screen58.attributes('-fullscreen', True)
    screen58.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn8
    btn8 = Button(screen58, text = 'Click me !',bg='green', command = Score9)
    global e8
    global f8
    btn8.place(x=f8, y=e8)
    Label(text = "").pack()
    global btn28
    btn28 =Button(screen58,text="DONT CLICK ME!", bg='red',command=GameOver9)
    screen58.mainloop()
def Score9():
    global l8
    global s8
    global c8
    global x8
    global score8
    if c8 == 1:
        score8 = 0
    if s8>= 1:
        x8 +=1
    if c8 != 1:
        x8 = 0
    global l8
    if x8 == 1 and l8 == 1:
        score8 = 0
    global n8
    n8+=1
    if n8 == 1:
        score8 = 0
        score8  = score8 + 1
        print(score8)
    else:
        if l8 == 2:
            score8= score8+1
            print (score8)
            global e8
            global f8
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn18.place(x=f8, y=e8)
        if l8 == 1:
            score8= score8+1
            print (score8)
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn8.place(x=f8, y=e8)
        if y8 == 1:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn28.place(x=760, y=370)
        if y8 == 2:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn38.place(x=760, y=370)
    c8 = 0


#Timed

import time
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
n8 = 0
x8 = 0
s8 = 0
c8 = 0
l8 = 1
y8 = 1
z8 = 1
score8 = 0
e8 = random.randint(0,760)
f8 = random.randint(1,1520)
print (e8)
print (f8)
fe8 =str(f8)
ef8 =str(e8)
def GameOver8():
    global l8
    l8 = 1
    if s8>= 1:
        screen38.destroy()
    sscore8 = str(score8)
    global screen28
    screen28=Toplevel(screen58)
    screen28.attributes('-fullscreen', True)
    screen28.title("Game Over!")
    Label(screen28,text="You got a score of "+sscore8).pack()
    Label(screen28,text="Game Over! Better luck next time!").pack()
    Button(screen28,text="Retry", command=Retry8).pack()
    Button(screen28,text="Quit", command=quit).pack()
def Retry8():
    global y8
    y8 = 2
    global l8
    l8+=1
    global c8
    c8+=1
    global x8
    if x8 >= 1:
        score8 == 0
    global s8
    s8+=1
    global screen38
    screen38 = Toplevel(screen58)
    screen38.attributes('-fullscreen', True)
    screen38.title("Buttons, and more buttons!")
    Label(screen38,text = "Lets  play a game!").pack()
    Label(screen38,text = "").pack()
    global btn18
    btn18 = Button(screen38, text = 'Click me !',bg='green', command = Score8)
    global e8
    global f8
    btn18.place(x=f8, y=e8)
    global btn38
    btn38 =Button(screen38,text="DONT CLICK ME!",bg='red',command=GameOver8)
def Buttons81():
    global y8
    y8 = 1
    global screen58
    screen58 = Toplevel(screen)
    screen58.attributes('-fullscreen', True)
    screen58.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn8
    btn8 = Button(screen58, text = 'Click me !',bg='green', command = Score8)
    global e8
    global f8
    btn8.place(x=f8, y=e8)
    Label(text = "").pack()
    global btn28
    btn28 =Button(screen58,text="DONT CLICK ME!", bg='red',command=GameOver8)
    screen58.mainloop()
def Score8():
    global l8
    global s8
    global c8
    global x8
    global score8
    if c8 == 1:
        score8 = 0
    if s8>= 1:
        x8 +=1
    if c8 != 1:
        x8 = 0
    global l8
    if x8 == 1 and l8 == 1:
        score8 = 0
    global n8
    n8+=1
    if n8 == 1:
        score8 = 0
        score8  = score8 + 1
        print(score8)
    else:
        if l8 == 2:
            score8= score8+1
            print (score8)
            global e8
            global f8
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn18.place(x=f8, y=e8)
        if l8 == 1:
            score8= score8+1
            print (score8)
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn8.place(x=f8, y=e8)
        if y8 == 1:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn28.place(x=k8, y=j8)
        if y8 == 2:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn38.place(x=k8, y=j8)
    c8 = 0

#Normal Mode

n8 = 0
x8 = 0
s8 = 0
c8 = 0
l8 = 1
y8 = 1
z8 = 1
score8 = 0
e8 = random.randint(0,760)
f8 = random.randint(1,1520)
print (e8)
print (f8)
fe8 =str(f8)
ef8 =str(e8)
def GameOver8():
    global l8
    l8 = 1
    if s8>= 1:
        screen38.destroy()
    sscore8 = str(score8)
    global screen28
    screen28=Toplevel(screen58)
    screen28.attributes('-fullscreen', True)
    screen28.title("Game Over!")
    Label(screen28,text="You got a score of "+sscore8).pack()
    Label(screen28,text="Game Over! Better luck next time!").pack()
    Button(screen28,text="Retry", command=Retry8).pack()
    Button(screen28,text="Quit", command=quit).pack()
def Retry8():
    global y8
    y8 = 2
    global l8
    l8+=1
    global c8
    c8+=1
    global x8
    if x8 >= 1:
        score8 == 0
    global s8
    s8+=1
    global screen38
    screen38 = Toplevel(screen58)
    screen38.attributes('-fullscreen', True)
    screen38.title("Buttons, and more buttons!")
    Label(screen38,text = "Lets  play a game!").pack()
    Label(screen38,text = "").pack()
    global btn18
    btn18 = Button(screen38, text = 'Click me !',bg='green', command = Score8)
    global e8
    global f8
    btn18.place(x=f8, y=e8)
    global btn38
    btn38 =Button(screen38,text="DONT CLICK ME!",bg='red',command=GameOver8)
def Buttons8():
    global y8
    y8 = 1
    global screen58
    screen58 = Toplevel(screen)
    screen58.attributes('-fullscreen', True)
    screen58.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn8
    btn8 = Button(screen58, text = 'Click me !',bg='green', command = Score8)
    global e8
    global f8
    btn8.place(x=f8, y=e8)
    Label(text = "").pack()
    global btn28
    btn28 =Button(screen58,text="DONT CLICK ME!", bg='red',command=GameOver8)
    screen58.mainloop()
def Score8():
    global l8
    global s8
    global c8
    global x8
    global score8
    if c8 == 1:
        score8 = 0
    if s8>= 1:
        x8 +=1
    if c8 != 1:
        x8 = 0
    global l8
    if x8 == 1 and l8 == 1:
        score8 = 0
    global n8
    n8+=1
    if n8 == 1:
        score8 = 0
        score8  = score8 + 1
        print(score8)
    else:
        if l8 == 2:
            score8= score8+1
            print (score8)
            global e8
            global f8
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn18.place(x=f8, y=e8)
        if l8 == 1:
            score8= score8+1
            print (score8)
            e8 = random.randint(0,760)
            f8 = random.randint(1,1520)
            btn8.place(x=f8, y=e8)
        if y8 == 1:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn28.place(x=k8, y=j8)
        if y8 == 2:
            j8 = random.randint(0,760)
            k8 = random.randint(1,1520)
            btn38.place(x=k8, y=j8)
    c8 = 0

#Button Maddness

n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
z = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def Newbutton():
    if score==5 or 10 or 15 or 20 or 25 or 30 or 35 or 40 or 45 or 50 or 75 or 100:
        global btn2
        btn2 =Button(screen5,text="DONT CLICK ME!", bg='red',command=GameOver)
        global y
        if y == 2:
            global btn3
            btn3 =Button(screen3,text="DONT CLICK ME!",bg='red',command=GameOver)
def GameOver():
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen5)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry).pack()
    Button(screen2,text="Quit", command=quit).pack()
def Retry():
    global y
    y = 2
    global l
    l+=1
    global c
    c+=1
    global x
    if x >= 1:
        score == 0
    global s
    s+=1
    global screen3
    screen3 = Toplevel(screen5)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Label(screen3,text = "Lets  play a game!").pack()
    Label(screen3,text = "").pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !',bg='green', command = Score)
    global e
    global f
    btn1.place(x=f, y=e)
    global btn3
    btn3 =Button(screen3,text="DONT CLICK ME!",bg='red',command=GameOver)
def Buttons():
    global y
    y = 1
    global screen5
    screen5 = Toplevel(screen)
    screen5.attributes('-fullscreen', True)
    screen5.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn
    btn = Button(screen5, text = 'Click me !',bg='green', command = Score)
    global e
    global f
    btn.place(x=f, y=e)
    Label(text = "").pack()
    global btn2
    btn2 =Button(screen5,text="DONT CLICK ME!", bg='red',command=GameOver)
    screen5.mainloop()
def Score():
    global l
    global s
    global c
    global score
    if c == 1:
        global score
        score = 0
    if s >= 1:
        global x
        x +=1
    if c != 1:
        x = 0
    global l
    if x == 1 and l == 1:
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
            e = random.randint(0,760)
            f = random.randint(1,1520)
            btn1.place(x=f, y=e)
        if l == 1:
            score= score+1
            print (score)
            e = random.randint(0,760)
            f = random.randint(1,1520)
            btn.place(x=f, y=e)
        if y == 1:
            j = random.randint(0,760)
            k = random.randint(1,1520)
            btn2.place(x=k, y=j)
        if y == 2:
            j = random.randint(0,760)
            k = random.randint(1,1520)
            btn3.place(x=k, y=j)
    c = 0
    Newbutton()
def Starting_Screen():
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(text = "What gamemode would you like to play?").pack()
    Label(text = "").pack()
    Button(screen, text = 'Button Madness!',bg='red', command = Buttons).pack()
    Label(text = "").pack()
    Button(screen,text="Normal mode", bg='Yellow',command=Buttons8).pack()
    Label(text="").pack()
    Button(screen,text="Hot button", bg="green",command=Buttons81).pack()
    Label(text="").pack()
    Button(screen,text="The screen is lava!",command=Buttons9).pack()
    screen.mainloop()
global all
Starting_Screen()
