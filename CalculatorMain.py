#Peter Mascherin
#this project will be an ongoing project to make a functional, styled calculator to the best of my ability


import tkinter as tk
from tkinter.constants import *
from tkinter.font import Font



#----DECLARATION OF BASE GLOBAL VARIABLES-------#
defaultbackground="#585858"
defaultforeground="#FFE8E8"
defaultactivebackground=defaultbackground
defaultactiveforeground=defaultforeground

#-------DECLARATION OF METHODS--------#
def placeholdermethod():
    print("hello world")


root = tk.Tk()
root.configure(bg="#3F3F3F")
thefont = Font(family="Helvetica",size=36)
#-------DECLARATION OF WIDGETS---------#
firstlabel = tk.Label(root,text="Placeholder Label")
onebutton = tk.Button(root,text="1",command=lambda: placeholdermethod())
twobutton = tk.Button(root,text="2")
threebutton = tk.Button(root,text="3")
fourbutton = tk.Button(root,text="4")
fivebutton = tk.Button(root,text="5")
sixbutton = tk.Button(root,text="6")
sevenbutton = tk.Button(root,text="7")
eightbutton = tk.Button(root,text="8")
ninebutton = tk.Button(root,text="9")
zerobutton = tk.Button(root,text="0")


#-------EXTRA CONFIGURATION OF WIDGETS---------#
onebutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
twobutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
threebutton.configure(bg=defaultbackground,fg=defaultactiveforeground,activeforeground=defaultactiveforeground,activebackground=defaultactivebackground,bd=1,width=12,height=5,font=thefont)
fourbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
fivebutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
sixbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
sevenbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
eightbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
ninebutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
zerobutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
firstlabel.configure(bg=defaultbackground,fg=defaultforeground,font=thefont)

#-------GRID ROW AND COLUMN CONFIGURATION-----#
root.rowconfigure((1,2,3,4),weight=1)
root.columnconfigure((0,1,2,3,4),weight=1)

#-------PLACEMENT OF WIDGETS-----------#
firstlabel.grid(row=0,column=0,columnspan=3)
onebutton.grid(row=1,column=0,sticky=(N,S,E,W),pady=2,padx=2)
twobutton.grid(row=1,column=1,sticky=(N,S,E,W),pady=2,padx=2)
threebutton.grid(row=1,column=2,sticky=(N,S,E,W),pady=2,padx=2)
fourbutton.grid(row=2,column=0,sticky=(N,S,E,W),pady=2,padx=2)
fivebutton.grid(row=2,column=1,sticky=(N,S,E,W),pady=2,padx=2)
sixbutton.grid(row=2,column=2,sticky=(N,S,E,W),pady=2,padx=2)
sevenbutton.grid(row=3,column=0,sticky=(N,S,E,W),pady=2,padx=2)
eightbutton.grid(row=3,column=1,sticky=(N,S,E,W),pady=2,padx=2)
ninebutton.grid(row=3,column=2,sticky=(N,S,E,W),pady=2,padx=2)
zerobutton.grid(row=4,column=1,sticky=(N,S,E,W),pady=2,padx=2)


#-------MAINLOOP ROOT SPECIFICATIONS----------#
root.title("Calculator App")
root.minsize(300,300)
root.maxsize(1000,700)

root.iconbitmap(r'CalculatorResources\calculatoricon.ico')
root.geometry("400x500")
root.mainloop()