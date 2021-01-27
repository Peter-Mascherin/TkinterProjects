#"main" must be ran from main workspace folder, any folders deeper and the imports dont work for god knows what reason
#A practice project meant to create something fun and learning Tkinter methods, classes, and styling of the app

import tkinter as tk
from tkinter.constants import *
from tkinter.ttk import *
from tkinter import messagebox

def buttonchange():
    print("bye bye")
    root.destroy()
    

def buttonmsgbox():
    print("hi hi")
    messagebox.showwarning(title="ALERT ALERT",message="THIS IS TKINTER OI")

def maybenewwindow():
    print("new window coming right up")
    newwindow = tk.Tk()
    newlabel = tk.Label(newwindow,text="Im a new window, what can i do in here").pack()
    newbutton = tk.Button(newwindow,text="What will this button do???",command=lambda: makelabel(2)).pack()
    newwindow.title("Im a new window")
    newwindow.geometry("300x100")
    

def makelabel(num):
    labelA1 = tk.Label(root)
    if(num == 1):
        labelA1.config(text="This label was made in the root window")
    elif(num == 2):
        labelA1.config(text="This label was actually made in the new window")
    
    labelA1.pack()

      
def makeinputwindow():
    inputwindow = tk.Tk()
    inputlabel = tk.Label(inputwindow,text="Input text to show up on main window :)")
    inputtext = tk.Entry(inputwindow)
    inputbutton = tk.Button(inputwindow,text="Submit",command=lambda: showinputtext(inputtext.get()))
    inputlabel.pack(side=TOP)
    inputtext.pack()
    inputbutton.pack(side=BOTTOM)
    inputwindow.geometry("300x100")
    inputwindow.title("Im the input window")
          
def showinputtext(thetext):
    theinputtext = tk.Label(root,text=thetext)
    theinputtext.pack()

root = tk.Tk()
root.title("Practice Project for widgets and style")
label = tk.Label(root,text="Ohaiyo Gozaimas").pack()
firstbutton = tk.Button(root,text="Click to close!",command=buttonchange).pack()
secondbutton = tk.Button(root,text="Click to show message box!",command=buttonmsgbox).pack()
thirdbutton = tk.Button(root,text="Magic man?",command=maybenewwindow).pack()
fourthbutton = tk.Button(root,text="Click me for Labels",command=lambda: makelabel(1)).pack()
fifthbutton = tk.Button(root,text="Click me to open an input window",command=lambda: makeinputwindow()).pack()


root.geometry("500x300")
root.mainloop()