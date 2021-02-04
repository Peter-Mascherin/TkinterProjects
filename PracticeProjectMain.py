#"main" must be ran from main workspace folder, any folders deeper and the imports dont work for god knows what reason
#A practice project meant to create something fun and learning Tkinter methods, classes, and styling of the app

#import tkinter as tk
#from tkinter.constants import *
#from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

def buttonchange():
    print("bye bye")
    root.destroy()
    

def buttonmsgbox():
    print("hi hi")
    messagebox.showerror(title="ALERT ALERT",message="YOUR DED FAGGOT LUL")

def maybenewwindow():
    print("new window coming right up")
    newwindow = Tk()
    newlabel = Label(newwindow,text="Im a new window, what can i do in here").pack()
    newbutton = Button(newwindow,text="What will this button do???",command=lambda: makelabel(2)).pack()
    newwindow.title("Im a new window")
    newwindow.geometry("300x100")
    

def makelabel(num):
    labelA1 = Label(root)
    if(num == 1):
        labelA1.config(text="This label was made in the root window")
    elif(num == 2):
        labelA1.config(text="This label was actually made in the new window")
    
    labelA1.pack()

      
def makeinputwindow():
    inputwindow = Tk()
    inputlabel = Label(inputwindow,text="Input text to show up on main window :)")
    inputtext = Entry(inputwindow)
    inputtext.focus()
    inputbutton = Button(inputwindow,text="Submit",command=lambda: showinputtext(inputtext.get()))
    inputlabel.pack(side=TOP)
    inputtext.pack()
    inputbutton.pack(side=BOTTOM)
    inputwindow.geometry("300x100")
    inputwindow.title("Im the input window")
          
def showinputtext(thetext):
    theinputtext = Label(root,text=thetext)
    theinputtext.pack()

root = Tk()
style = ttk.Style()
style.configure("TButton",background="red",foreground="black")
padding = 10
root.title("Practice Project for widgets and style")
label = Label(root,text="Ohaiyo Gozaimas").grid(row=0,column=0,padx=padding,pady=padding)
firstbutton = Button(root,text="Click to close!",command=buttonchange).grid(row=0,column=1,padx=padding,pady=padding)
secondbutton = Button(root,text="Click to show message box!",command=buttonmsgbox).grid(row=0,column=2,padx=padding,pady=padding)
thirdbutton = Button(root,text="Magic man?",command=maybenewwindow).grid(row=1,column=0,padx=padding,pady=padding)
fourthbutton = ttk.Button(root,text="Click me for Labels",command=lambda: makelabel(1),style="TButton").grid(row=1,column=1,padx=padding,pady=padding)
fifthbutton = Button(root,text="Click me to open an input window",command=lambda: makeinputwindow()).grid(row=1,column=2,padx=padding,pady=padding)

root.geometry("500x300+900+300")
root.mainloop()