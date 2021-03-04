#A simple internet radio app where you can listen to your favourite stations as well as customize the theme of the app
#Built by Peter Mascherin

import tkinter as tk
from tkinter.font import *
from tkinter.constants import *
import vlc # install this module using this: pip install python-vlc 
#(you also need the 64-bit version of VLC installed which can be downloaded here https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe)
import time
import json
import RadioResources.radiostationinfo as rad

#BASE COLOURS OF APP
basebgcolour = "#1A1A1A"
stationtextcolour = "#1ED760"
statustextcolour = "#1ED760"


#METHODS

# stopmedia simple changes status to 'Currently Stopped' and stops the player (whichs cut off connection to stream)
def stopmedia():
    statustext.configure(text="Currently Stopped...")
    player.stop()

# pausemedia simply changes status to 'Paused' and pauses player
def pausemedia():
    statustext.configure(text="Currently Paused...")
    player.pause()

# playmedia sets sets the audio into MediaPlayer variable, 
# changes the radioname and statustext labels to current stations and current status(playing,paused,stopped)
# and then plays the media (print statement for debugging)
def playmedia():
    player.set_media(theaudio)
    rnamestring = str(stationstore[channelnumber])
    radionametext.configure(text=rnamestring)
    statustext.configure(text="Currently Playing...")
    player.play()
    print(urlstore[channelnumber])
    

#have to rewrite the switchstation() logic , try except wont work
# switchstation checks the global channelnumber (if its out of array bounds or negative) and corrects if needed
# then stops the current audio with stopmedia(), setups the new media to play in setupmedia(), and then calls playmedia()
def switchstation(switchnum):
    global channelnumber
    try:
        if(switchnum == 1):
            channelnumber = channelnumber + 1
            stopmedia()
            setupmedia(channelnumber)
            playmedia()
        else:
            channelnumber = channelnumber - 1
            stopmedia()
            setupmedia(channelnumber)
            playmedia()
    except:
        if(channelnumber < 0):
            channelnumber = len(urlstore) - 1
            stopmedia()
            setupmedia()
            playmedia()
        elif(channelnumber > (len(urlstore)-1)):
            channelnumber = 0
            stopmedia()
            setupmedia()
            playmedia()

# declares global variable theaudio, releases the current url (which feels the wrong way to do it but i dont know another way) 
# and sets audio to new url(1 foward or 1 behind)
def setupmedia(channelnumber): 
    global theaudio
    theaudio.release()
    theaudio = vlc.Media(urlstore[channelnumber])
    

#WIDGET DECLARATION
root = tk.Tk()
fowardimage = tk.PhotoImage(file="RadioResources/foward.png")
backimage = tk.PhotoImage(file="RadioResources/back.png")
stopimage = tk.PhotoImage(file="RadioResources/stop.png")
pauseimage = tk.PhotoImage(file="RadioResources/pause.png")
playimage = tk.PhotoImage(file="RadioResources/play.png")
stationfont = Font(family="Helivetica",size=36)
statusfont = Font(family="Helvetica",size=12)
playbutton = tk.Button(root,image=playimage,command=lambda:playmedia(),bg=basebgcolour,activebackground=basebgcolour,height=40,bd=0)
pausebutton = tk.Button(root,image=pauseimage,command=lambda:pausemedia(),bg=basebgcolour,activebackground=basebgcolour,height=40,bd=0)
stopbutton = tk.Button(root,image=stopimage,command=lambda:stopmedia(),bg=basebgcolour,activebackground=basebgcolour,height=40,bd=0)
nextbutton = tk.Button(root,image=fowardimage,command=lambda:switchstation(1),bg=basebgcolour,activebackground=basebgcolour,height=40,bd=0)
previousbutton = tk.Button(root,image=backimage,command=lambda:switchstation(-1),bg=basebgcolour,activebackground=basebgcolour,height=40,bd=0)
radionametext = tk.Label(root,text="Python Internet Radio",font=stationfont,fg=stationtextcolour,bg=basebgcolour)
statustext = tk.Label(root,text="Ready to Play",font=statusfont,fg=statustextcolour,bg=basebgcolour)


#WIDGET PLACEMENT
playbutton.grid(row=3,column=1,sticky=(S,W,E),pady=6,padx=2)
pausebutton.grid(row=3,column=2,sticky=(S,E,W),pady=6,padx=2)
stopbutton.grid(row=3,column=0,sticky=(S,E,W),pady=6,padx=2)
nextbutton.grid(row=2,column=2,sticky=(E,W),pady=25,padx=6,rowspan=3)
previousbutton.grid(row=2,column=0,sticky=(E,W),pady=25,padx=6,rowspan=3)
radionametext.grid(row=0,column=0,sticky=(N,W,S),padx=10,pady=0,columnspan=3)
statustext.grid(row=1,column=0,sticky=(N,W),pady=0,padx=25,columnspan=3)

#JSON DATA GRAB
datad = json.loads(rad.urls) #loads the JSON list into datad
channelnumber = 0
urlstore = [] #the array of urls for radio stations
stationstore = [] #the array of radio names for the radio stations
for url in datad['stations']: #loops through the 'stations' object in datad JSON
    urlstore.append(url['radiourl']) #appends the radio station urls to urlstore
    stationstore.append(url['radioname']) #appends the radio station names to stationstore


#VLC MEDIA CONFIGURATION 
theaudio = vlc.Media(urlstore[channelnumber])
player = vlc.MediaPlayer()
player.audio_set_volume(80)


#ROOT CONFIGURATION
root.rowconfigure((0,1,2,3),weight=1)
root.columnconfigure((0,1,2),weight=1)
root.configure(bg=basebgcolour)
root.resizable(FALSE,FALSE)
root.iconbitmap(r"RadioResources\radioicon.ico")
root.title("Internet Radio")
root.geometry("750x300+400+300")
root.mainloop()