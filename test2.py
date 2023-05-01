import tkinter as tk

root = tk.Tk()

def my_function(event):
    print("Key 1 was pressed")

root.bind("<1>", my_function)

root.mainloop()