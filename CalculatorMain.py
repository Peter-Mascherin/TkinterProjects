#Peter Mascherin
#this project will be an ongoing project to make a functional, styled calculator to the best of my ability


import tkinter as tk
from tkinter.constants import *
from tkinter.font import Font




#----DECLARATION OF BASE GLOBAL VARIABLES-------#
root = tk.Tk()
defaultbackground="#585858"
defaultforeground="#FFE8E8"
defaultactivebackground=defaultbackground
defaultactiveforeground=defaultforeground
defaultstring = tk.StringVar()


#-------DECLARATION OF METHODS--------#
def concatstrings(mybutton):
    grabtext = defaultstring.get() + mybutton.cget('text')
    defaultstring.set(grabtext)
    numberlabel.config(text=defaultstring.get())
    
def clearstring(clearbutton):
    defaultstring.set("")
    numberlabel.config(text="Input Numbers...")

def arimeticconcat(aributton):
    if(aributton.cget('text') == '÷'):
        defaultstring.set(defaultstring.get() + "/")
    else:
        defaultstring.set(defaultstring.get() + aributton.cget('text'))

    numberlabel.config(text=defaultstring.get())
    

def results():
    resultsum = eval(defaultstring.get())
    numberlabel.config(text=resultsum)
    defaultstring.set("")


root.configure(bg="#3F3F3F")
thefont = Font(family="Helvetica",size=36)
#-------DECLARATION OF WIDGETS---------#
numberlabel = tk.Label(root,text="Input Numbers...")
onebutton = tk.Button(root,text="1",command=lambda: concatstrings(onebutton))
twobutton = tk.Button(root,text="2",command=lambda: concatstrings(twobutton))
threebutton = tk.Button(root,text="3",command=lambda: concatstrings(threebutton))
fourbutton = tk.Button(root,text="4",command=lambda: concatstrings(fourbutton))
fivebutton = tk.Button(root,text="5",command=lambda: concatstrings(fivebutton))
sixbutton = tk.Button(root,text="6",command=lambda: concatstrings(sixbutton))
sevenbutton = tk.Button(root,text="7",command=lambda: concatstrings(sevenbutton))
eightbutton = tk.Button(root,text="8",command=lambda: concatstrings(eightbutton))
ninebutton = tk.Button(root,text="9",command=lambda: concatstrings(ninebutton))
zerobutton = tk.Button(root,text="0",command=lambda: concatstrings(zerobutton))
clearbutton = tk.Button(root,text="C",command=lambda: clearstring(clearbutton))
dividebutton = tk.Button(root,text="÷",command=lambda: arimeticconcat(dividebutton))
multiplybutton = tk.Button(root,text="*",command=lambda: arimeticconcat(multiplybutton))
addbutton = tk.Button(root,text="+",command=lambda: arimeticconcat(addbutton))
subtractbutton = tk.Button(root,text="-",command=lambda: arimeticconcat(subtractbutton))
equalsbutton = tk.Button(root,text="=",command=lambda: results())


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
clearbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
equalsbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
dividebutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
multiplybutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
addbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
subtractbutton.configure(bg=defaultbackground,fg=defaultforeground,activebackground=defaultactivebackground,activeforeground=defaultactiveforeground,bd=1,width=12,height=5,font=thefont)
numberlabel.configure(bg=root.cget('bg'),fg=defaultforeground,font=thefont)

#-------GRID ROW AND COLUMN CONFIGURATION-----#
root.rowconfigure((1,2,3,4),weight=1)
root.columnconfigure((0,1,2,3,4),weight=1)

#-------PLACEMENT OF WIDGETS-----------#
numberlabel.grid(row=0,column=0,columnspan=4)
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
clearbutton.grid(row=4,column=0,sticky=(N,S,E,W),padx=2,pady=2)
equalsbutton.grid(row=4,column=2,sticky=(N,S,E,W),padx=2,pady=2)
dividebutton.grid(row=1,column=3,sticky=(N,S,E,W),pady=2,padx=2)
multiplybutton.grid(row=2,column=3,sticky=(N,S,E,W),padx=2,pady=2)
addbutton.grid(row=3,column=3,sticky=(N,S,E,W),pady=2,padx=2)
subtractbutton.grid(row=4,column=3,sticky=(N,S,E,W),padx=2,pady=2)


#-------MAINLOOP ROOT SPECIFICATIONS----------#
root.title("Calculator App")
root.minsize(300,300)
root.maxsize(1000,700)

root.iconbitmap(r'CalculatorResources\calculatoricon.ico')
root.geometry("400x500")
root.mainloop()