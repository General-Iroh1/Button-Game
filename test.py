
import time
from tkinter import *
from tkinter import messagebox
 
def SB3():
    root = Tk()
    b=0
    root.geometry("300x250")
  
    root.title("Time Counter")
    second=StringVar()
    second.set("")
    secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second)
    secondEntry.place(x=180,y=20)
    secondEntry.place(x=760,y=380)
    def submit():
        try:
            temp = int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            root.update()
            time.sleep(1)
            if (temp == 0):
                global b
                b+=1
                messagebox.showinfo("Time Countdown", "Time's up ")
            temp -= 1
    btn = Button(root, text='Set Time Countdown', bd='5',
                 command= submit)
    btn.place(x = 720,y = 520)
  

    root.mainloop()