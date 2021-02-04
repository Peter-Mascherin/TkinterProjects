#Peter Mascherin
#this project will be an ongoing project to make a functional, styled calculator to the best of my ability
import tkinter as tk
from tkinter.constants import *

defaultbackground="#585858"
defaultforeground="#FFE8E8"
defaultactivebackground=defaultbackground
defaultactiveforeground=defaultforeground

def placeholdermethod():
    print("hello world")


root = tk.Tk()
root.configure(bg="#3F3F3F")
#-------DECLARATION OF WIDGETS---------#
firstlabel = tk.Label(root,text="Placeholder Label")
firstbutton = tk.Button(root,text="Placeholder Button",command=lambda: placeholdermethod())
#-------EXTRA CONFIGURATION OF WIDGETS---------#
firstbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1)
firstlabel.configure(bg=defaultbackground,fg=defaultforeground)
#-------PLACEMENT OF WIDGETS-----------#
firstlabel.grid(row=0,column=0,padx=10,pady=10)
firstbutton.grid(row=0,column=1,padx=10,pady=10)
#-------MAINLOOP ROOT SPECIFICATIONS----------#
root.title("Calculator App")
root.iconbitmap(r'CalculatorResources\calculatoricon.ico')
root.geometry("500x300")
root.mainloop()