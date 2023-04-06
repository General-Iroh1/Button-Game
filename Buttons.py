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
v = 0
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
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry4).pack()
    Button(screen2,text="Quit", command=quit).pack()
    Button(screen2,text="Main Menu", command=Starting_Screen).pack()
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
    screen3 = Toplevel(screen0)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    Button(screen3,width= '1523',height= '1523',text="Click me ;)",bg = 'red',command=GameOver4).pack()
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
    Button(screen,  width= '1523',height= '1523',text="Click me ;)",bg = 'red',command=GameOver4).pack()
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
aa = 0
b = 1
i = 0
k = 0
n = 0
a = 0
r = 0
x = 0
p = 0
h = 1
u = 0
w = 1
s = 0
z = 0
o = 0
q = 0
c = 0
g = random.randint(0,760)
d =  random.randint(1,1520)
l = 1
y = 1
m = 1
score = 0
print (e)
print (f)
fe =str(f)
ef =str(e)
def GameOver3():
    global i
    global k
    global l
    global r
    global o
    global u
    global w
    global aa
    aa+=1
    w+=1
    u+=1
    if o >= 1:
        r+=1
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry3).pack()
    Button(screen2,text="Quit", command=quit).pack()
    Button(screen2,text="Main Menu", command=Starting_Screen).pack()
def Retry3():
    global i
    global a
    global y
    global o
    global u
    global p
    global score
    global screen6
    global w
    global r
    global s
    global t1
    global time2
    global screen3
    global c 
    global btn1
    global btn3
    global aa
    global t1
    p = 2
    y=2
    o+=1
    i = 0
    c+=1

    if u >= 1:
        if r >= 1:
            score = 0
    u = 0
    s+=1

    if a >= 1:
        screen3.destroy()
    screen2.destroy()

    screen3 = Toplevel(screen0)
    screen3.attributes('-fullscreen', True)
    screen3.title("Buttons, and more buttons!")
    if aa >= 1:
        t1 = l*60
    time2 = Label(screen3,text = t1, font=("Arial", 24), fg="red")
    time2.place(relx=0.5, rely=0.5, anchor='center')

    btn1 = Button(screen3, text = 'Click me !', command = Score3)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn1.place(x=k, y=j)

    btn3 =Button(screen3,text="Click me ;)",command=GameOver3)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn3.place(x=k, y=j)

    w += 1
    countdown1()





def Buttons3():
    global i
    global q
    global b
    global h
    global t
    global e
    global f
    global btn
    global btn2
    global screen6
    global screen
    global time1
    global l
    global score
    global x
    global s
    global v
    global p
    global z
    global c
    global n
    global y
    y=1
    i+=1
    p=1
    e = random.randint(0,760)
    f = random.randint(1,1520)

    if v == 0:
        t = l * 60

    screen6 = tkinter.Tk()
    if z >= 1:
        screen6.destroy()
    screen.destroy()
    screen6.attributes('-fullscreen', True)
    screen6.title("Buttons, and more buttons!")

    Label(text="Let's play a game!").pack()
    Label(text="").pack()

    btn = Button(screen6, text='Click me!', command=Score3)
    btn.place(x=f, y=e)

    time1 = Label(screen6, text=t, font=("Arial", 24), fg="red")
    time1.place(relx=0.5, rely=0.5, anchor='center')

    btn2 = Button(screen6, text="Click me ;)", command=GameOver3)
    j = random.randint(0, 760)
    k = random.randint(1, 1520)
    btn2.place(x=k, y=j)
    z+=1
    b += 1
    q = 0
    if v ==0:
        countdown()
    
    screen0.mainloop()

def countdown():
    global t
    update_screen()

def update_screen():
    global v
    v+=1
    global t 
    global time1
    global screen6
    global w
    if w ==2:
        screen6.destroy()
        GameOver3()
    if t > 0:
        time1.config(text=t)
        screen6.after(1000, update_screen)
        t -= 1
    else:
        GameOver3()





def countdown1():
    global aa
    aa=0
    update_screen1()
def update_screen1():
    global t1
    global a
    global time2
    global screen3
    a+=1
    if t1 > 0:
        time2.config(text=t1)
        screen3.after(1000, countdown1)
        t1 -= 1
    if t1==0:
        GameOver3()
def Score3():
    global m
    global b
    global l
    global s
    global c
    global score
    global x
    global u
    global n
    global btn
    global btn2
    global p

    if c == 1:
        score = 0


    if c != 1:
        r = 0

    n += 1

    if n == 1:
        score = 0
        score += 1
        print(score)
    else:
        if p == 2:
            score += 1
            print(score)
            e = random.randint(0, 760)
            f = random.randint(1, 1520)
            btn1.place(x=f, y=e)
        if p == 1:
            score += 1
            print(score)
            e = random.randint(0, 760)
            f = random.randint(1, 1520)
            btn.place(x=f, y=e)
        if y == 1:
            j = random.randint(0, 760)
            k = random.randint(1, 1520)
            btn2.place(x=k, y=j)
            Buttons3()
        if y == 2:
            j = random.randint(0, 760)
            k = random.randint(1, 1520)
            btn3.place(x=k, y=j)
            Retry3()
    u = 0




#Button Madness
a = 0
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
    global a
    if a >= 1:
        screen3.destroy()
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry2).pack()
    Button(screen2,text="Quit", command=quit).pack()
    Button(screen2,text="Main Menu", command=Starting_Screen).pack()
def Retry2():
    global a
    a+=1
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
    screen3 = Toplevel(screen0)
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
    btn3 =Button(screen3,text="Click me ;)",command=GameOver2)
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
    btn2 =Button(screen,text="Click me ;)",command=GameOver2)
    screen.mainloop()
def newbutton():
    if score == 1 or 2 or 3 or 4 or 5 or 10 or 20 or 30 or 40 or 50 or 60 or 70 or 75 or 100:
        global btn2
        btn2 =Button(screen,text="Click me ;)",command=GameOver2)
    if y == 2 and score == 1 or 2 or 3 or 4 or 5 or 10 or 20 or 30 or 40 or 50 or 60 or 70 or 75 or 100:
        global btn3
        btn3 =Button(screen3,text="Click me ;)",command=GameOver2)
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
    global a
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry1).pack()
    Button(screen2,text="Quit", command=quit).pack()
    Button(screen2,text="Main Menu", command=Starting_Screen).pack()
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
    screen3 = Toplevel(screen0)
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
    btn3 =Button(screen3,text="Click me ;)",command=GameOver1)
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
    btn2 =Button(screen,text="Click me ;)",command=GameOver1)
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

    Button(screen0,text="Button Mayhem!",command=Buttons2).pack()
    Button(screen0,text="Timed(W.I.P)",command=Test).pack()

    Button(screen0,text="The screen is lava!",command=Buttons4).pack()
    screen0.mainloop()
def up():
        global l
        l +=1
        screen.after(1, testscreen)
def down():
        global l
        l-=1
        screen.after(1, testscreen)
def Test():
    global l
    l=1
    global testscreen
    screenPLACEHOLDER = Toplevel(screen0)
    screenPLACEHOLDER.attributes('-fullscreen', True)
    screenPLACEHOLDER.title("Buttons, and more buttons!")
    downarrow = PhotoImage(file=r"D:/Applications/Python/Button-Game/button_down.png")
    uparrow = PhotoImage(file=r"D:/OneDrive/Pictures/Saved Pictures/button_up.png")
    screenPLACEHOLDER.withdraw()
    def testscreen():
        global screen
        screen = Toplevel(screen0)
        screen.attributes('-fullscreen', True)
        screen.title("Buttons, and more buttons!")
        if l ==5:
            Label(screen,text="5 minutes is the max you can go!",font=('Times', 26)).pack()
        if l < 5:
            Button(screen, image=uparrow,command=up,width=300,height=200, pady=10).pack()
        Label(screen,text=l,font=('Calibri', 26)).pack()
        if l == 1:
            Label(screen,text="1 minute is the lowest you can go!",font=('Times', 26)).pack()
        if l> 1:
            Button(screen, image=downarrow,command=down,width=300,height=200, pady=10).pack()
        Button(screen,text="Confirm", command=Buttons3).pack()
        Label(screen,text="Remember, this is measured in minutes!").pack()
        screen.mainloop()
    testscreen()
global all
Starting_Screen()