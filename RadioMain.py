#A simple internet radio app where you can listen to your favourite stations as well as customize the theme of the app
#Built by peter mascherin

import tkinter as tk
from tkinter.constants import *
import vlc #pip install python-vlc (you also need the 64-bit version of VLC installed which can be downloaded here https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe)

#METHODS
def stopmedia():
    media.stop()

def pausemedia():
    media.pause()

def playmedia():
    media.play()


#WIDGET DECLARATION
root = tk.Tk()
playbutton = tk.Button(root,text="Play",command=lambda:playmedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=2)
pausebutton = tk.Button(root,text="Pause/Resume",command=lambda:pausemedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=2)
stopbutton = tk.Button(root,text="Stop",command=lambda:stopmedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=2)

#WIDGET PLACEMENT
playbutton.grid(row=2,column=0,sticky=(S,W,E),pady=6,padx=2)
pausebutton.grid(row=2,column=1,sticky=(S,E,W),pady=6,padx=2)
stopbutton.grid(row=2,column=2,sticky=(S,E,W),pady=6,padx=2)

#VLC MEDIA CONFIGURATION
media = vlc.MediaPlayer("https://uk3.internet-radio.com/proxy/majesticjukebox?mp=/live")

#ROOT CONFIGURATION
root.rowconfigure((0,1,2),weight=1)
root.columnconfigure((0,1,2),weight=1)
root.configure(bg="#3D3939")
root.iconbitmap(r"RadioResources\radioicon.ico")
root.title("Internet Radio")
root.geometry("550x300")
root.mainloop()