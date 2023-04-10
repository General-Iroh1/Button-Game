import tkinter
from tkinter import *
import random

#Global variables
x = 0
y = 1
score = 0
e = random.randint(0,760)
f = random.randint(1,1520)
gamemode = "lava_timed"
time_left = 30
timer = None
screen = None
btn = None

#Game functions
def quit_game():
    global screen
    screen.destroy()

def game_over():
    global screen
    global timer
    if timer:
        screen.after_cancel(timer)
    screen2 = tkinter.Toplevel(screen)
    screen2.attributes('-fullscreen', True)
    screen2.title("Game Over!")
    Label(screen2,text="You got a score of "+str(score)).pack()
    Label(screen2,text="Game Over! Better luck next time!").pack()
    Button(screen2,text="Retry", command=restart_game).pack()
    Button(screen2,text="Quit", command=quit_game).pack()

def restart_game():
    global score
    score = 0
    global time_left
    time_left = 30
    start_game()

def start_timer():
    global time_left
    global timer
    time_left -= 1
    if time_left < 0:
        game_over()
    else:
        timer = screen.after(1000, start_timer)
        Label(screen, text=f"Time left: {time_left}", font=("Arial", 16)).pack()

def move_button():
    global btn
    global e
    global f
    e = random.randint(0,760)
    f = random.randint(1,1520)
    btn.place(x=f, y=e)

def check_collision():
    global x
    global y
    global e
    global f
    global score
    if gamemode == "lava_timed":
        if x == 1 and y == e:
            score += 1
            move_button()
        else:
            game_over()
    elif gamemode == "lava":
        if y >= 650:
            game_over()
        elif x == 1 and y == e:
            score += 1
            move_button()

def button_click():
    global x
    x = 1
    check_collision()

def start_game():
    global screen
    global btn
    global e
    global f
    global gamemode
    gamemode = "lava_timed"
    screen = tkinter.Tk()
    screen.attributes('-fullscreen', True)
    screen.title("Lava Timed Game")
    Label(text="Score: "+str(score), font=("Arial", 16)).pack()
    Label(screen, text=f"Time left: {time_left}", font=("Arial", 16)).pack()
    btn = Button(screen, text="Click me!", bg="lime", command=button_click)
    btn.place(x=f, y=e)
    start_timer()
    screen.mainloop()

#Start the game
start_game()