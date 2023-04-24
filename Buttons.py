import tkinter
from tkinter import *
import random
import time
from playsound import playsound
from tkinter import messagebox
#The screen is lava!
b=0
n = 0
x = 0
s = 0
c = 0
l = 1
v = 0
FinishedLava=0
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
print (e)
print (f)
fe =str(f)
ef =str(e)
def quit4():
    global FinishedLava
    FinishedLava+=1
    quit()
def GameOver4():
    global l
    global screen2
    l = 1
    if s>= 1:
        screen2.destroy()
        screen3.destroy()
    sscore = str(score)
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry4).pack()
    Button(screen2,text="Quit", command=quit4).pack()
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
    btn1 = Button(screen3, text = 'Click me !', bg='lime', command = Score4)
    global e
    global f
    btn1.place(x=f, y=e)
def Buttons4():
    global screen
    screen = Toplevel(screen0)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Button(screen,  width= '1523',height= '1523',text="Click me ;)",bg = 'red',command=GameOver4).pack()
    global btn
    btn = Button(screen, text = 'Click me !', bg = 'lime', command = Score4)
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
Button3Done = 0
a = 0
r = 0
x = 0
p = 0
h = 1
TimedStarted=0
u = 0
w = 1
Gameoveroccured = 0
s = 0
TimedFinished = 0
z = 0
o = 0
q = 0
c = 0
g = random.randint(0,760)
d =  random.randint(1,1520)
l = 1
y = 1
m = 1
FinishedTimed=0
score = 0
print (e)
print (f)
fe =str(f)
ef =str(e)
def quit3():
    global FinishedTimed
    FinishedTimed+=1
    quit()
def GameOver3():
    global i
    global k
    global l
    global r
    global o
    global u
    global w
    global aa
    global screen6
    global Button3Done
    global Gameoveroccured
    Gameoveroccured+=1
    screen6.destroy()
    aa+=1
    w+=1
    u+=1
    if o >= 1:
        r+=1
    l = 1
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Quit", command=quit3).pack()
    Button(screen2,text="Main Menu", command=aftergamestartingscreen).pack()
addbutton=0
def secret(E):
    global addbutton
    global extrabutton1
    global extrabutton2
    global extrabutton3
    global extrabutton4
    global extrabutton5
    addbutton +=1
    if addbutton == 1:
        extrabutton1 = Button(screen6, text="Click me.")
    if addbutton == 2:
        extrabutton2 = Button(screen6, text="Click me.")
    if addbutton == 3:
        extrabutton3 = Button(screen6, text="Click me.")
    if addbutton == 4:
        extrabutton4 = Button(screen6, text="Click me.")
    if addbutton == 5:
        extrabutton5 = Button(screen6, text="Click me.")
def Buttons3():
    global TimedStarted
    global TimedFinished
    global i
    global q
    global b
    global h
    global t
    global Button3Done
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
    global screen9
    global iteration
    global Gameoveroccured
    iteration = 1
    TimedStarted+=1
    screen.destroy()
    y=1
    i+=1
    p=1
    e = random.randint(0,760)
    f = random.randint(1,1520)

    if v == 0:
        t = l * 60

    screen6 = Toplevel(screen0)
    if z >= 1 and TimedFinished == 0:
        screen6.destroy()
    screen6.attributes('-fullscreen', True)
    screen6.title("Buttons, and more buttons!")

    Label(text="Let's play a game!").pack()
    Label(text="").pack()

    btn = Button(screen6, text='Click me!', command=Score3)
    btn.place(x=f, y=e)

    time1 = Label(screen6, text=t, font=("Arial", 24), fg="red")
    time1.place(relx=0.5, rely=0.5, anchor='center')

    btn2 = Button(screen6, text="Click me ;)", command=GameOver3)
    screen6.bind('<Tab>',secret)
    j = random.randint(0, 760)
    k = random.randint(1, 1520)
    btn2.place(x=k, y=j)
    Button3Done  = 1
    TimedFinished = 0
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
    if t > 0:
        time1.config(text=t)
        screen6.after(1000, update_screen)
        t -= 1
    else:
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
    u = 0




#Button Mayhem
a = 0
n = 0
x = 0
s = 0
c = 0
l = 1
y = 1
score = 0
FinishedMayhem = 0
e = random.randint(0,760)
f = random.randint(1,1520)

print (e)
print (f)
fe =str(f)
ef =str(e)
def quit2():
    global FinishedMayhem
    FinishedMayhem+=1
    quit()
def GameOver2():
    global screen2
    global a
    if a >= 1:
        screen2.destroy()
        screen3.destroy()
    global l
    l = 1
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry2).pack()
    Button(screen2,text="Quit", command=quit2).pack()
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
    screen = Toplevel(screen0)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
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
    global screen
    global screen3
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
FinishedRegular = 0
print (e)
print (f)
fe =str(f)
ef =str(e)
def quit1():
    global FinishedRegular
    FinishedRegular+=1
    quit()
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
    Button(screen2,text="Quit", command=quit1).pack()
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
    screen = Toplevel(screen0)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
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
#For The Worthy
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
FinishedFTW=0
score = 0
print (e)
print (f)
fe =str(f)
ef =str(e)
def quit5():
    global FinishedFTW
    FinishedFTW+=1
    quit()
def GameOver5():
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
    if s>= 1:
        screen3.destroy()
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=Retry5).pack()
    Button(screen2,text="Quit", command=quit5).pack()
    Button(screen2,text="Main Menu", command=Starting_Screen).pack()
def Retry5():
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
        t1 = 30
    time2 = Label(screen3,text = t1, font=("Arial", 24), fg="red")
    time2.place(relx=0.5, rely=0.5, anchor='center')


    Button(screen3,width= '1523',height= '1523',text="Click me ;)",bg = 'red',command=GameOver5).pack()
    btn1 = Button(screen3, text = 'Click me !', command = Score5)
    j = random.randint(0,760)
    k = random.randint(1,1520)
    btn1.place(x=k, y=j)

    w += 1
    countdown1_5()




def Buttons5():
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
        t = 30

    screen6 = Toplevel(screen0)
    if z >= 1:
        screen6.destroy()
    screen6.attributes('-fullscreen', True)
    screen6.title("Buttons, and more buttons!")



    time1 = Label(screen6, text=t, font=("Arial", 24), fg="red")
    time1.place(relx=0.5, rely=0.5, anchor='center')

    Button(screen6,width= '1523',height= '1523',text="Click me ;)",bg = 'red',command=GameOver5).pack()
    btn = Button(screen6, text='Click me!', command=Score5)
    btn.place(x=f, y=e)
    z+=1
    b += 1
    q = 0
    if v ==0:
        countdown_5()
    
    screen0.mainloop()

def countdown_5():
    global t
    update_screen_5()
    playsound('TheWorthyMusic.mp3')

def update_screen_5():
    global v
    v+=1
    global t 
    global time1
    global screen6
    global w
    if w ==2:
        screen6.destroy()
    if t > 0:
        time1.config(text=t)
        screen6.after(1000, update_screen_5)
        t -= 1
    else:
        GameOver5()





def countdown1_5():
    global aa
    aa=0
    update_screen1_5()
def update_screen1_5():
    global t1
    global a
    global time2
    global screen3
    a+=1
    if t1 > 0:
        time2.config(text=t1)
        screen3.after(1000, countdown1_5)
        t1 -= 1
    if t1==0:
        GameOver5()
def Score5():
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
        if p == 1:
            score += 1
            print(score)
            e = random.randint(0, 760)
            f = random.randint(1, 1520)
            btn.place(x=f, y=e)
            Buttons5()
        if y >= 2:
            j = random.randint(0, 760)
            k = random.randint(1, 1520)
            btn1.place(x=k, y=j)
            Retry5()

    u = 0
def ForTheWorthy():
    global screen7
    screen7 = Toplevel(screen0)
    screen7.attributes('-fullscreen', True)
    screen7.title("...")
    screen7.configure(bg='red')
    Label(screen7,text="Only those who have TRUE experience may get past this gate").pack()
    Label(screen7,text="",bg='red').pack()
    Label(screen7,text="",bg='red').pack()
    Label(screen7,text="",bg='red').pack()
    Label(screen7,text="",bg='red').pack()
    Button(screen7,text="Continue",command=Buttons5,bg='red').pack()
    Label(screen7,text="",bg='red').pack()
    Button(screen7,text="Quit",command=quit,bg='red').pack()
aftergame = 0
def aftergamestartingscreen():
    global screen2
    global screen9
    global aftergame
    screen2.destroy()
    screen9 = tkinter.Tk()
    screen9.attributes('-fullscreen', True)
    screen9.title("Buttons, and more buttons!")
    Label(screen9,text = "What gamemode would you like to play?").pack()
    Label(screen9,text = "").pack()
    global btn
    btn = Button(screen9, text = 'Normal',bg = 'green', command = Buttons1).pack()
    global e
    global f

    Button(screen9,text="Button Mayhem!",bg = 'blue',command=Buttons2).pack()
    Button(screen9,text="Timed",bg = 'orange',command=Test).pack()

    Button(screen9,text="The screen is lava!",bg='red',command=Buttons4).pack()
    Button(screen9, text="For The Worthy",bg='purple',command=ForTheWorthy).pack()
    aftergame+=1
def Starting_Screen():
    global screen0
    screen0 = tkinter.Tk()
    screen0.attributes('-fullscreen', True)
    screen0.title("Buttons, and more buttons!")
    Label(screen0,text = "What gamemode would you like to play?").pack()
    Label(screen0,text = "").pack()
    global btn
    btn = Button(screen0, text = 'Normal',bg = 'green', command = Buttons1).pack()
    global e
    global f

    Button(screen0,text="Button Mayhem!",bg = 'blue',command=Buttons2).pack()
    Button(screen0,text="Timed",bg = 'orange',command=Test).pack()

    Button(screen0,text="The screen is lava!",bg='red',command=Buttons4).pack()
    Button(screen0, text="For The Worthy",bg='purple',command=ForTheWorthy).pack()
    screen0.mainloop()
def up():
        global l
        l +=1
        if mainmenuclicked >= 3:
            screen.after(0, Test)
        else:
            screen.after(0, testscreen)
def down():
        global l
        l-=1
        if mainmenuclicked >= 3:
            screen.after(0, Test)
        else:
            screen.after(0, testscreen)
mainmenuclicked=1
iteration = 1
screenexists = 0
def Test():
    global mainmenuclicked
    global v
    global l
    global TimedStarted
    global TimedFinished
    global score
    global screenexists
    global aftergame
    if aftergame == 1:
        screen9.destroy()
    if screenexists >= 1:
        global downbutton
        global minutelabel
        global upbutton
        global Confirm
        global Reminder
        if l >= 2:
            downbutton.destroy()
        minutelabel.destroy()
        if l <= 5:
            upbutton.destroy()
        Confirm.destroy()
        Reminder.destroy()
    score = 0
    TimedFinished +=1
    v = 0
    mainmenuclicked += 1
    if mainmenuclicked >= 3:
        screen6.destroy()
    if mainmenuclicked == 1:
            l=1
    testscreen()
def useimages():
    if l > 1:
        global downbutton
        downbutton = Button(screen, text = l-1,command=down)
        downbutton.pack()
    global minutelabel
    minutelabel = Label(screen,text=l,font=('Calibri', 26))
    minutelabel.pack()
    if l < 5:
        global upbutton
        upbutton = Button(screen, text= l+1,command=up)
        upbutton.pack()
    global Confirm
    Confirm = Button(screen,text="Confirm", command=Buttons3)
    Confirm.pack()
    global Reminder
    Reminder = Label(screen,text="Remember, this is measured in minutes!")
    Reminder.pack()
    global screenexists
    screenexists +=1


def testscreen():
    global iteration
    global screenexists
    global aftergame
    global screen,mainmenuclicked
    if screenexists >= 1:
        global downbutton
        global minutelabel
        global upbutton
        global Confirm
        global Reminder
        if l >= 1 and screenexists >= 2:
            downbutton.destroy()
        minutelabel.destroy()
        if l < 6:
            upbutton.destroy()
        Confirm.destroy()
        Reminder.destroy()
    if iteration == 1:
        screen = Toplevel(screen0)
        screen.attributes('-fullscreen', True)
        screen.title()
    iteration+=1
    aftergame = 0
    useimages()


global all
Starting_Screen()