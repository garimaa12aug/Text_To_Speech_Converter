import os
import tkinter as tk
from tkinter import *
import parser
import tkinter.messagebox

def speak(text):
        os.system('espeak "{}"'.format(text) )

def clicked():
        text = entry.get()
        speak(text)

root = tk.Tk()
root.title("Text to Speech")
root.resizable(width=False, height=False)
root.geometry("1200x700+0+0")
label1 = tk.Label(root, text='What do you want me to speak?',bg="blue", font=('Helvetica',20,'bold'))
label1.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='Speak!', command=clicked)
button.pack()
photo = PhotoImage(file = "robo.gif")
w = Label(root, image=photo)
w.pack(fill=BOTH, expand=YES)

root.mainloop()


