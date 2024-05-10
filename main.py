import tkinter as tk
import time

import pyautogui #фокус - без библиотеки запускается
# from pyautogui import click


root = tk.Tk()

root.attributes('-fullscreen', True)
root.title("=)")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

frame = tk.Frame(root)
frame.place(relx=.5, rely=.5, anchor='c')

label = tk.Label(frame, text="Введи ключ и нажми ctrl+c")
label.pack()

entry = tk.Entry(frame)
entry.pack()

root.update()

pyautogui.click(x=width//2, y=height//2)

def on_closing():
    pyautogui.click(x=width//2, y=height//2)
    pyautogui.moveTo(x=width//2, y=height//2)
    root.attributes('-fullscreen', True)
    root.update()

# while True:
#     on_closing()
root.mainloop()