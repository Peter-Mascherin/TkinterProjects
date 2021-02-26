#Clock and Timer app created by Peter Mascherin
#A general purpose clock and timer app i plan to provide continous development on
#Shows the time, can set a timer, a stopwatch, and future functions to be added
#Current code is placeholder code
import tkinter as tk
from tkinter.constants import *
from time import *
from tkinter.font import *
from datetime import date, datetime

root = tk.Tk()
textfont = Font(family="Helvetica",size=36)
rootbackground = "#363535"

def clockupdate():
    
    timestring = datetime.today().strftime("%I:%M:%S %p %Z")
    if(timestring[0] == "0"):
        clocklabel.config(text=timestring[1:])
    else:
        clocklabel.config(text=timestring)
    clocklabel.after(10,clockupdate)

def stopwatchupdate():
    stopwatchstring = datetime.today().strftime('%I:%M:%S:%f')[:-3]
    stopwatchlabel.configure(text=stopwatchstring)
    stopwatchlabel.after(10,stopwatchupdate)
    

clocklabel = tk.Label(root,bg=rootbackground,fg="#FFFFFF",text="testest")
clocklabel.configure(font=textfont,padx=10,pady=10)
clocklabel.grid(row=0,column=0,sticky=(N,W),columnspan=6)
clockupdate()

stopwatchlabel = tk.Label(root,bg=rootbackground,fg="#FFFFFF",text="placehgolder text")
stopwatchlabel.configure(font=textfont,pady=10,padx=10)
stopwatchlabel.grid(row=5,column=5,sticky=(S,E),columnspan=6)
stopwatchupdate()

root.rowconfigure((0,1,2,3,4,5),weight=1)
root.columnconfigure((0,1,2,3,4,5),weight=1)

root.configure(bg=rootbackground)
root.title("Clock and Timer App")
root.geometry("500x200")
root.iconbitmap(r'ClockTimerResources\alarmclock.ico')
root.mainloop()


