import tkinter as tk

root = tk.Tk()

root.attributes('-fullscreen', True)
root.title("=)")

frame = tk.Frame(root)
frame.place(relx=.5, rely=.5, anchor='c')

label = tk.Label(frame, text="Введи ключ и нажми ctrl+c")
label.pack()

entry = tk.Entry(frame)
entry.pack()

root.mainloop()
