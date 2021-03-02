#A simple internet radio app where you can listen to your favourite stations as well as customize the theme of the app
#Built by peter mascherin

import tkinter as tk
from tkinter.font import *
from tkinter.constants import *
import vlc #pip install python-vlc (you also need the 64-bit version of VLC installed which can be downloaded here https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe)
import time
import json
import RadioResources.radiourls as rad

#METHODS
def stopmedia():
    media.stop()

def pausemedia():
    media.pause()

def playmedia():
    media.play()
    
def switchstation():
    print('yp')

#WIDGET DECLARATION
root = tk.Tk()
fowardimage = tk.PhotoImage(file="RadioResources/foward.png")
backimage = tk.PhotoImage(file="RadioResources/back.png")
stopimage = tk.PhotoImage(file="RadioResources/stop.png")
pauseimage = tk.PhotoImage(file="RadioResources/pause.png")
playimage = tk.PhotoImage(file="RadioResources/play.png")
custfont = Font(family="Helivetica",size=24)
playbutton = tk.Button(root,image=playimage,command=lambda:playmedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=40,bd=0)
pausebutton = tk.Button(root,image=pauseimage,command=lambda:pausemedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=40,bd=0)
stopbutton = tk.Button(root,image=stopimage,command=lambda:stopmedia(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=40,bd=0)
nextbutton = tk.Button(root,image=fowardimage,command=lambda:switchstation(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=40,bd=0)
previousbutton = tk.Button(root,image=backimage,command=lambda:switchstation(),bg="#3D3939",fg="#FFFFFF",activeforeground="#FFFFFF",activebackground="#3D3939",height=40,bd=0)
testtext = tk.Label(root,text="font change me",font=custfont,fg="#FFFFFF",bg="#3D3939")


#WIDGET PLACEMENT
playbutton.grid(row=2,column=1,sticky=(S,W,E),pady=6,padx=2)
pausebutton.grid(row=2,column=2,sticky=(S,E,W),pady=6,padx=2)
stopbutton.grid(row=2,column=0,sticky=(S,E,W),pady=6,padx=2)
nextbutton.grid(row=1,column=2,sticky=(E,W),pady=2,padx=6,rowspan=2)
previousbutton.grid(row=1,column=0,sticky=(E,W),pady=6,padx=2,rowspan=2)
testtext.grid(row=0,column=0,sticky=(N,W),padx=6,pady=2,columnspan=3)


#VLC MEDIA CONFIGURATION

datad = json.loads(rad.urls)
urlstore = []
for url in datad['stations']:
    urlstore.append(url['radiourl'])
media = vlc.MediaPlayer(urlstore[4])
media.audio_set_volume(80)


#ROOT CONFIGURATION
root.rowconfigure((0,1,2),weight=1)
root.columnconfigure((0,1,2),weight=1)
root.configure(bg="#3D3939")
root.iconbitmap(r"RadioResources\radioicon.ico")
root.title("Internet Radio")
root.geometry("550x300")
root.mainloop()