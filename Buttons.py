import tkinter
from tkinter import *
import random
import time
from tkinter import messagebox
#The screen is lava!
b=0
n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver4():
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry4).pack()
    Button(screen2,text="Quit", command=quit).pack()
def Retry4():
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
    screen3 = Toplevel(screen)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Button(screen3,width= '1523',height= '1523',text="DONT CLICK ME!", bg='red',command=GameOver4).pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !', command = Score4)
    global e
    global f
    btn1.place(x=f, y=e)
def Buttons4():
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Button(screen,  width= '1523',height= '1523',text="DONT CLICK ME!", bg='red',command=GameOver4).pack()
    global btn
    btn = Button(screen, text = 'Click me !', command = Score4)
    global e
    global f
    btn.place(x=f, y=e)
    screen.mainloop()
def Score4():
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
    c = 0

#Timed

b = 1
n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver3():
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry3).pack()
    Button(screen2,text="Quit", command=quit).pack()
def Retry3():
    global y
    y+=1
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
    screen3 = Toplevel(screen)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Label(screen3,text = "Lets  play a game!").pack()
    Label(screen3,text = "").pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !', command = Score3)
    global e
    global f
    btn1.place(x=f, y=e)
    global btn3
    btn3 =Button(screen3,bg='red',text="DONT CLICK ME!",command=GameOver3)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn3.place(x=k, y=j)
def Buttons3():
    global b
    if b == 1:
        temp = 5
    if temp == 0:
        GameOver3()
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn
    btn = Button(screen, text = 'Click me !', command = Score3)
    global e
    global f
    btn.place(x=f, y=e)
    Label(text = "").pack()
    global btn2
    btn2 =Button(screen,text="DONT CLICK ME!", bg='red',command=GameOver3)
    time.sleep(1)
    temp -= 1
    b+=1
    screen.mainloop()
def Score3():
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
            btn2.place(x=k, y=j)
    c = 0

def SB3():
    root = Tk()
    root.geometry("300x250")
  
    root.title("Time Counter")
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    second.set("10")
    secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second)
    secondEntry.place(x=180,y=20)
    def submit():
        try:
            global temp
            temp = 30
        except:
            print("Please input the right value")
        while temp >-1:
            global b
            secs = divmod(temp,60)
            root.update()
            time.sleep(1)
            if (temp == 30):
                Buttons3()
            temp -= 1
    btn = Button(root, text='Set Time Countdown', bd='5',
                command= submit)
    btn.place(x = 70,y = 120)
  

    root.mainloop()
#Button Madness

n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver2():
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry2).pack()
    Button(screen2,text="Quit", command=quit).pack()
def Retry2():
    global y
    y+=1
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
    screen3 = Toplevel(screen)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Label(screen3,text = "Lets  play a game!").pack()
    Label(screen3,text = "").pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !', command = Score2)
    global e
    global f
    btn1.place(x=f, y=e)
    global btn3
    btn3 =Button(screen3,bg='red',text="DONT CLICK ME!",command=GameOver2)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn3.place(x=k, y=j)
def Buttons2():
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn
    btn = Button(screen, text = 'Click me !', command = Score2)
    global e
    global f
    btn.place(x=f, y=e)
    Label(text = "").pack()
    global btn2
    btn2 =Button(screen,text="DONT CLICK ME!", bg='red',command=GameOver2)
    screen.mainloop()
def newbutton():
    if score == 1 or 2 or 3 or 4 or 5 or 10 or 20 or 30 or 40 or 50 or 60 or 70 or 75 or 100:
        global btn2
        btn2 =Button(screen,text="DONT CLICK ME!", bg='red',command=GameOver2)
    if y == 2 and score == 1 or 2 or 3 or 4 or 5 or 10 or 20 or 30 or 40 or 50 or 60 or 70 or 75 or 100:
        global btn3
        btn3 =Button(screen3,text="DONT CLICK ME!", bg='red',command=GameOver2)
def Score2():
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
    newbutton()
    c = 0

#Normal

n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver1():
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry1).pack()
    Button(screen2,text="Quit", command=quit).pack()
def Retry1():
    global y
    y+=1
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
    screen3 = Toplevel(screen)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Label(screen3,text = "Lets  play a game!").pack()
    Label(screen3,text = "").pack()
    global btn1
    btn1 = Button(screen3, text = 'Click me !', command = Score1)
    global e
    global f
    btn1.place(x=f, y=e)
    global btn3
    btn3 =Button(screen3,text="DONT CLICK ME!",command=GameOver1)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn3.place(x=k, y=j)
def Buttons1():
    global screen
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Label(text = "Lets  play a game!").pack()
    Label(text = "").pack()
    global btn
    btn = Button(screen, text = 'Click me !', command = Score1)
    global e
    global f
    btn.place(x=f, y=e)
    Label(text = "").pack()
    global btn2
    btn2 =Button(screen,text="DONT CLICK ME!", bg='blue',command=GameOver1)
    screen.mainloop()
def Score1():
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

def Starting_Screen():
    global screen0
    screen0 = tkinter.Tk()
    screen0.attributes('-fullscreen', True)
    screen0.title("Buttons, and more buttons!")
    Label(screen0,text = "What gamemode would you like to play?").pack()
    Label(screen0,text = "").pack()
    global btn
    btn = Button(screen0, text = 'Normal', command = Buttons1).pack()
    global e
    global f
    Label(text = "").pack()

    Button(screen0,text="Button Mayhem!", bg='blue',command=Buttons2).pack()
    Label(text = "").pack()

    Button(screen0,text="Timed", bg='blue',command=Buttons3).pack()
    Label(text = "").pack()

    Button(screen0,text="The screen is lava!", bg='blue',command=Buttons4).pack()
    screen0.mainloop()
global all
Starting_Screen()