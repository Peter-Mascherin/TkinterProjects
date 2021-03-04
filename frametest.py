import tkinter as tk
from tkinter.constants import *
import tkinter.font as ft

def switchframe(theframe):
    theframe.tkraise()

root = tk.Tk()

firstframe = tk.Frame(root)
secondframe = tk.Frame(root)

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
firstframe.rowconfigure((0,1,2),weight=1)
firstframe.columnconfigure((0,1,2),weight=1)
secondframe.rowconfigure((0,1,2),weight=1)
secondframe.columnconfigure((0,1,2),weight=1)

firstframe.configure(bg="#915F5F",width=1,height=1)
firstframebutton = tk.Button(firstframe,text="switch the frame idiot",command=lambda:switchframe(secondframe))
firstframe.grid(row=0,column=0,sticky=(N,S,E,W))
firstframebutton.grid(row=1,column=1,sticky=(N,S,E,W))

secondframe.configure(bg="#5F9171",width=1,height=1)
secondframebutton = tk.Button(secondframe,text="FUCK SWITCH BACK",command=lambda:switchframe(firstframe))
secondframe.grid(row=0,column=0,sticky=(N,S,E,W))
secondframebutton.grid(row=2,column=2,sticky=(N,S,E,W))


switchframe(firstframe)
root.geometry("300x300")
root.mainloop()