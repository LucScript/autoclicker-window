import pyautogui
import tkinter as tk
from tkinter import *

fen = tk.Tk()

fen.title("Autoclicker for your games...")
fen.geometry("350x450")
fen.configure(background="black")


font = ("Courrier", 8)

text = Label(fen, text = "Welcome to my autoclicker now you can active it with the following button", font=font)
text.pack()

def activeautoclicker():
    while True:
        pyautogui.click()

button = Button(fen, text="Active autoclicker", command=activeautoclicker, background="white")
button.pack()

text1 = Label(fen, text = "Make Ctrl+alt+sup to stop the autoclicker", font=font)
text1.pack()

fen.mainloop()
