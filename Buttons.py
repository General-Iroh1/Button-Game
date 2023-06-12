import tkinter
from tkinter import *
import random
import time
from playsound import playsound
from tkinter import messagebox
from pygame import mixer
import time
unbind= 0
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
    quit()
def GameOver4():
    global screen9
    global l
    global score
    global Heatdeath
    global Lavatime
    global screen2
    mixer.music.stop()
    screen.destroy()
    l = 1
    sscore = str(score)
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    if Heatdeath >=1:
        Label(screen2,text="You burnt!").pack()
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Quit", command=quit4).pack()
    global FinishedLava
    FinishedLava+=1
    Button(screen2,text="Main Menu", command=aftergamestartingscreen).pack()
    Lavatime = 4
    score = 0
def Buttons4(Event):
    global screen9
    global unbind
    if unbind >=1:
        screen9.unbind('<KeyPress-1>')
        screen9.unbind('<KeyPress-2>')
        screen9.unbind('<KeyPress-3>')
    else:
        global screen0
        screen0.unbind('<KeyPress-1>')
        screen0.unbind('<KeyPress-2>')
        screen0.unbind('<KeyPress-3>')
    unbind+=1
    mixer.init()
    mixer.music.load('Lava.mp3')
    mixer.music.play(-1)
    global screen
    global aftergame
    if aftergame>=1:
        screen9.destroy()
    screen = Toplevel(screen0)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Button(screen,  width= '1523',height= '1523',text="",bg = 'red',command=GameOver4).pack()
    global btn
    clickme = PhotoImage(file="Click me!.png")
    btn = Button(screen, image=clickme, borderwidth=0,highlightthickness=0,activebackground='red',activeforeground='red', fg= 'red', bg="red",command = Score4)
    global e
    global f
    btn.place(x=f, y=e)
    def LavatimeChecker():
        global Lavatime
        if Lavatime>0:
            screen.after(1000, LavatimeChecker)
            Lavatime-=1
        else:
            global Heatdeath
            Heatdeath+=1
            GameOver4()
    LavatimeChecker()
    screen0.mainloop()
Heatdeath = 0
def Buttons4A():
    global screen9
    global Lavatime
    global unbind
    if unbind >=1:
        screen9.unbind('<KeyPress-1>')
        screen9.unbind('<KeyPress-2>')
        screen9.unbind('<KeyPress-3>')
    else:
        global screen0
        screen0.unbind('<KeyPress-1>')
        screen0.unbind('<KeyPress-2>')
        screen0.unbind('<KeyPress-3>')
    unbind+=1
    global screen
    global aftergame
    if aftergame>=1:
        screen9.destroy()
    mixer.init()
    mixer.music.load('Lava.mp3')
    mixer.music.play(-1)
    screen = Toplevel(screen0)
    screen.attributes('-fullscreen', True)
    screen.title("Buttons, and more buttons!")
    Button(screen,  width= '1523',height= '1523',text="",bg = 'red',command=GameOver4).pack()
    global btn
    clickme = PhotoImage(file="Click me!.png")
    btn = Button(screen, image=clickme, borderwidth=0,highlightthickness=0,activebackground='red',activeforeground='red', fg= 'red', bg="red",command = Score4)
    global e
    global f
    btn.place(x=f, y=e)
    def LavatimeChecker():
        global Lavatime
        if Lavatime>0:
            screen.after(1000, LavatimeChecker)
            Lavatime-=1
        else:
            global Heatdeath
            Heatdeath+=1
            GameOver4()
    LavatimeChecker()
    screen0.mainloop()
def Score4():
    global l
    global s
    global c
    global Lavatime
    global score
    Lavatime = 4
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
score = 0
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
    global screen2
    global score
    global Button3Done
    global Gameoveroccured
    global FinishedTimed
    mixer.music.stop()
    mixer.init()
    mixer.music.load('Ring.mp3')
    mixer.music.play()
    FinishedTimed+=1
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
    score = 0
addbutton=0
unbinddone = 0
def Buttons3():
    global TimedStarted
    global TimedFinished
    global screen9
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
    global unbinddone
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
    global aftergame
    global Gameoveroccured
    if aftergame>=1:
        screen9.destroy()
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
    clickme3 = s
    btn2 = Button(screen6,image='',highlightthickness=0,activebackground='red',activeforeground='red', fg= 'red', bg="red",command = GameOver3)
    j = random.randint(0, 760)
    k = random.randint(1, 1520)
    btn2.place(x=k, y=j)
    Button3Done  = 1
    TimedFinished = 0
    unbinddone +=1
    z+=1
    b += 1
    q = 0
    mixer.init()
    mixer.music.load('Timed.mp3')
    mixer.music.play(-1)
    if v ==0:
        countdown()
    
    screen0.mainloop()
Lavatime = 4
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
    quit()
def GameOver2():
    mixer.music.stop()
    global screen
    global screen2
    global a
    global score
    screen.destroy()
    global FinishedMayhem
    FinishedMayhem+=1
    global l
    l = 1
    sscore = str(score)
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Quit", command=quit2).pack()
    Button(screen2,text="Main Menu", command=aftergamestartingscreen).pack()
    score = 0
def Buttons2(Event):
    global screen9
    global unbind
    if unbind >=1:
        screen9.unbind('<KeyPress-1>')
        screen9.unbind('<KeyPress-2>')
        screen9.unbind('<KeyPress-3>')
    else:
        global screen0
        screen0.unbind('<KeyPress-1>')
        screen0.unbind('<KeyPress-2>')
        screen0.unbind('<KeyPress-3>')
    unbind+=1
    global screen
    global aftergame
    if aftergame>=1:
        screen9.destroy()
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
    mixer.init()
    mixer.music.load('Button confusion.mp3')
    mixer.music.play(-1)
    screen0.mainloop()
def Buttons2A():
    global screen9
    global unbind
    if unbind >=1:
        screen9.unbind('<KeyPress-1>')
        screen9.unbind('<KeyPress-2>')
        screen9.unbind('<KeyPress-3>')
    else:
        global screen0
        screen0.unbind('<KeyPress-1>')
        screen0.unbind('<KeyPress-2>')
        screen0.unbind('<KeyPress-3>')
    unbind+=1
    global screen
    global aftergame
    if aftergame>=1:
        screen9.destroy()
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
    mixer.init()
    mixer.music.load('Button confusion.mp3')
    mixer.music.play(-1)
    screen0.mainloop()
def newbutton():
    global screen
    if score == 1 or 2 or 3 or 4 or 5 or 10 or 20 or 30 or 40 or 50 or 60 or 70 or 75 or 100:
        global btn2
        btn2 =Button(screen,text="Click me ;)",command=GameOver2)
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
    newbutton()
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
    global screen11
    global screen9
    screen.destroy()
    screen11.destroy()
    aa+=1
    w+=1
    global score
    u+=1
    if o >= 1:
        r+=1
    sscore = str(score)
    global screen2
    screen2=Toplevel(screen0)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+sscore).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Quit", command=quit5).pack()
    Button(screen2,text="Main Menu", command=aftergamestartingscreen).pack()

    mixer.music.stop()
    score = 0
Heatdeath2 = 0
t5 = 30
Lavatime2 = 3
def Buttons5():
    global i
    global q
    global b
    global h
    global t5
    global e
    global f
    global btn
    global btn2
    global screen11
    global screen
    global time5
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
    global Onetime
    if Onetime == 0:
        screen7.destroy()
    y=1
    i+=1
    p=1
    e = random.randint(0,760)
    f = random.randint(1,1520)

    if v == 0:
        t5 = 30

    screen11 = Toplevel(screen0)
    screen11.attributes('-fullscreen', True)
    screen11.title("Buttons, and more buttons!")

    Button(screen11,width= '1523',height= '1523',text=" ",bg = 'red',command=GameOver5).pack()
    time5 = Label(screen11, text=t5, font=("Arial", 24), fg="black", bg="red")
    time5.place(relx=0.5, rely=0.5, anchor='center')
    btn = Button(screen11,bg = "lime", command=Score5)
    btn.place(x=f, y=e)
    z+=1
    b += 1
    q = 0
    if Onetime == 0:
        mixer.init()
        mixer.music.load('TheWorthyMusic.mp3')
        mixer.music.play(-1)
    Onetime += 1
    def LavatimeChecker2():
        global Lavatime2
        global screen11
        if Lavatime2>0:
            screen11.after(1000, LavatimeChecker2)
            Lavatime2-=1
        else:
            global Heatdeath2
            Heatdeath2+=1
            GameOver5()
    LavatimeChecker2()
    countdown5()
#fix timer

def countdown5():
    global t5
    update_screen5()

def update_screen5():
    global v
    v+=1
    global t5
    global time5
    global screen11
    global w
    if t5 > 0:
        time5.config(text=t5)
        screen11.after(1000, update_screen5)
        t5 -= 1
    else:
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



    u = 0
def ForTheWorthy():
    screen9.destroy()
    global screen7
    screen7 = Toplevel(screen0)
    global Onetime
    Onetime = 0
    screen7.attributes('-fullscreen', True)
    screen7.title("...")
    screen7.configure(bg='red')
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
    if FinishedMayhem >=1:
        screen2.destroy()
    if FinishedLava >=1:
        screen2.destroy()
    if FinishedTimed >=1:
        screen2.destroy()
    screen9 = tkinter.Tk()
    screen9.attributes('-fullscreen', True)
    screen9.title("Buttons, and more buttons!")
    Label(screen9,text = "What gamemode would you like to play?").pack()
    Label(screen9,text = "").pack()
    global btn
    global e
    global f

    Button(screen9,text="Button Confusion",bg = 'green',command=Buttons2A).pack()
    Button(screen9,text="Timed",bg = 'orange',command=Test2).pack()
    screen9.bind('<KeyPress-1>',Buttons2)
    screen9.bind('<KeyPress-2>',Test1)
    screen9.bind('<KeyPress-3>',Buttons4)
    Button(screen9,text="The screen is lava!",bg='red',command=Buttons4A).pack()
    Label(screen9).pack()
    Label(screen9).pack()
    Label(screen9).pack()
    Label(screen9).pack()
    Label(screen9).pack()
    Button(screen9, text="Legendary",bg='yellow',command=ForTheWorthy).pack()
    aftergame+=1
def Starting_Screen():
    global score
    global screen0
    score = 0
    screen0 = tkinter.Tk()
    screen0.attributes('-fullscreen', True)
    screen0.title("Buttons, and more buttons!")
    Label(screen0,text = "What gamemode would you like to play?").pack()
    Label(screen0,text = "").pack()
    global btn
    global e
    global f
    Button(screen0,text="Button Confusion",bg = 'green',command=Buttons2A).pack()
    Button(screen0,text="Timed",bg = 'orange',command=Test3).pack()

    Button(screen0,text="The screen is lava!",bg='red',command=Buttons4A).pack()
    screen0.bind('<KeyPress-1>',Buttons2)
    screen0.bind('<KeyPress-2>',Test)
    screen0.bind('<KeyPress-3>',Buttons4)
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
def Test(event):
    if unbinddone == 0:
        screen0.unbind('<KeyPress-1>')
        screen0.unbind('<KeyPress-2>')
        screen0.unbind('<KeyPress-3>')
    global mainmenuclicked
    global v
    global l
    global TimedStarted
    global TimedFinished
    global score
    global screenexists
    global aftergame
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
def Test3():
    global mainmenuclicked
    global v
    global l
    global TimedStarted
    global TimedFinished
    global score
    global screenexists
    global aftergame
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
def up2():
        global l
        l +=1
        if mainmenuclicked >= 3:
            screen.after(0, Test2)
        else:
            screen.after(0, testscreen2)
def down2():
        global l
        l-=1
        if mainmenuclicked >= 3:
            screen.after(0, Test2)
        else:
            screen.after(0, testscreen2)
mainmenuclicked=1
iteration = 1
screenexists1 = 0
def Test2():
    
    global mainmenuclicked
    global screenexists
    global v
    global l
    global TimedStarted
    global TimedFinished
    global score
    global aftergame
    mainmenuclicked = 1
    screenexists = 0
    if screenexists1 >= 1:
        global downbutton2
        global minutelabel2
        global upbutton2
        global Confirm2
        global Reminder2
        if l >= 2:
            downbutton2.destroy()
        minutelabel2.destroy()
        if l <= 5:
            upbutton2.destroy()
        Confirm2.destroy()
        Reminder2.destroy()
    score = 0
    TimedFinished +=1
    v = 0
    mainmenuclicked += 1
    if mainmenuclicked >= 3:
        screen6.destroy()
    if mainmenuclicked == 1:
            l=1
    testscreen2()
def useimages2():
    if l > 1:
        global downbutton2
        downbutton2 = Button(screen, text = l-1,command=down2)
        downbutton2.pack()
    global minutelabel2
    minutelabel2= Label(screen,text=l,font=('Calibri', 26))
    minutelabel2.pack()
    if l < 5:
        global upbutton2
        upbutton2 = Button(screen, text= l+1,command=up2)
        upbutton2.pack()
    global Confirm2
    Confirm2 = Button(screen,text="Confirm", command=Buttons3)
    Confirm2.pack()
    global Reminder2
    Reminder2= Label(screen,text="Remember, this is measured in minutes!")
    Reminder2.pack()
    global screenexists1
    screenexists1 +=1

def testscreen2():
    global iteration
    global screenexists
    global aftergame
    global screen,mainmenuclicked
    if screenexists >= 1:
        global downbutton2
        global minutelabel2
        global upbutton2
        global Confirm2
        global Reminder2
        if l >= 1:
            downbutton2.destroy()
        minutelabel2.destroy()
        if l < 6:
            upbutton2.destroy()
        Confirm2.destroy()
        Reminder2.destroy()
    if iteration == 1:
        screen = Toplevel(screen0)
        screen.attributes('-fullscreen', True)
        screen.title()
    iteration+=1
    if aftergame == 1:
        screen9.destroy()
    aftergame = 0
    useimages()

def up1():
        global l
        l +=1
        if mainmenuclicked >= 3:
            screen.after(0, Test1)
        else:
            screen.after(0, testscreen1)
def down1():
        global l
        l-=1
        if mainmenuclicked >= 3:
            screen.after(0, Test1)
        else:
            screen.after(0, testscreen1)
mainmenuclicked=1
unbinddone = 0
iteration = 1
screenexists1 = 0
def Test1(Event):
    global mainmenuclicked
    global screenexists
    global v
    global l
    global TimedStarted
    global TimedFinished
    global score
    global unbinddone
    global aftergame
    if unbinddone == 0:
        screen9.unbind('<KeyPress-1>')
        screen9.unbind('<KeyPress-2>')
        screen9.unbind('<KeyPress-3>')
        unbinddone+=1
    mainmenuclicked = 1
    screenexists = 0
    if screenexists1 >= 1:
        global downbutton1
        global minutelabel1
        global upbutton1
        global Confirm1
        global Reminder1
        if l >= 2:
            downbutton1.destroy()
        minutelabel1.destroy()
        if l <= 5:
            upbutton1.destroy()
        Confirm1.destroy()
        Reminder1.destroy()
    score = 0
    TimedFinished +=1
    v = 0
    mainmenuclicked += 1
    if mainmenuclicked >= 3:
        screen6.destroy()
    if mainmenuclicked == 1:
            l=1
    testscreen1()
def useimages1():
    if l > 1:
        global downbutton1
        downbutton1 = Button(screen, text = l-1,command=down1)
        downbutton1.pack()
    global minutelabel1
    minutelabel1= Label(screen,text=l,font=('Calibri', 26))
    minutelabel1.pack()
    if l < 5:
        global upbutton1
        upbutton1 = Button(screen, text= l+1,command=up1)
        upbutton1.pack()
    global Confirm1
    Confirm1 = Button(screen,text="Confirm", command=Buttons3)
    Confirm1.pack()
    global Reminder1
    Reminder1= Label(screen,text="Remember, this is measured in minutes!")
    Reminder1.pack()
    global screenexists1
    screenexists1 +=1

def testscreen1():
    global iteration
    global screenexists                
    global aftergame
    global screen,mainmenuclicked
    if screenexists >= 1:
        global downbutton1
        global minutelabel1
        global upbutton1
        global Confirm1
        global Reminder1
        if l >= 1:
            downbutton1.destroy()
        minutelabel1.destroy()
        if l < 6:
            upbutton.destroy()
        Confirm1.destroy()
        Reminder1.destroy()
    if iteration == 1:
        screen = Toplevel(screen0)
        screen.attributes('-fullscreen', True)
        screen.title()
    iteration+=1
    if aftergame == 1:
        screen9.destroy()
    aftergame = 0
    useimages()

global all
Starting_Screen()