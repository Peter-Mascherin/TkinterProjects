#A simple internet radio app where you can listen to your favourite stations as well as customize the theme of the app
#Built by Peter Mascherin

import tkinter as tk
from tkinter.font import *
from tkinter.constants import *
from tkinter import messagebox
import vlc # install this module using this: pip install python-vlc 
#(you also need the 64-bit version of VLC installed which can be downloaded here https://www.videolan.org/vlc/download-windows.html)
import json
import smtplib
import RadioResources.radiostationinfo as rad

#BASE COLOURS OF APP
basebgcolour = "#1A1A1A"
stationtextcolour = "#1ED760"
statustextcolour = "#1ED760"
entryboxcolour = "#222222"



#METHODS
# simple print debug checking for checking variables on play , stop , and switch
def debugchecker():
    print(urlstore[channelnumber])
    print(stationstore[channelnumber])
    print(channelnumber)

# to switch between frames (currently homescreen, in future settings and suggestions)
def switchframe(framing):
    framing.tkraise()

# stopmedia simple changes status to 'Currently Stopped' and stops the player (whichs cut off connection to stream)
def stopmedia():
    statustext.configure(text="Currently Stopped...")
    player.stop()

# pausemedia simply changes status to 'Paused' and pauses player
def pausemedia():
    statustext.configure(text="Currently Paused...")
    player.stop()
    

# playmedia sets sets the audio into MediaPlayer variable, 
# changes the radioname and statustext labels to current stations and current status(playing,paused,stopped)
# and then plays the media and also displays an error message if stream is revoked 
def playmedia():
    player.set_media(theaudio)
    rnamestring = str(stationstore[channelnumber])
    radionametext.configure(text=rnamestring)
    statustext.configure(text="Currently Playing...")
    setimage()
    stationimagelabel.configure(image=stationimage)
    playcheck = player.play()
    if(playcheck == -1):
        messagebox.showerror("Playback Error","This probably happened due to a access revoked stream, wait a minute or so and click play again, or restart the app after waiting")
    

# controls the volume   
def volumecontrol(volume):
    player.audio_set_volume(int(volume))


#have to rewrite the switchstation() logic , try except wont work
# switchstation checks the global channelnumber (if its out of array bounds or negative) and corrects if needed
# then stops the current audio with stopmedia(), setups the new media to play in setupmedia(), and then calls playmedia()
def switchstation(switchnum):
    global channelnumber
    channelnumber = channelnumber + switchnum
    if(channelnumber < 0):
        channelnumber = (len(urlstore)-1)
    elif(channelnumber > (len(urlstore)-1)):
        channelnumber = 0
    stopmedia()
    setupmedia(channelnumber)
    playmedia()

# declares global variable theaudio, releases the current url (which feels the wrong way to do it but i dont know another way) 
# and sets audio to new url(1 foward or 1 behind)
def setupmedia(channelnumber): 
    global theaudio
    theaudio.release()
    theaudio = vlc.Media(urlstore[channelnumber])

# changes the image of the radio station as you scroll through back and forth
def setimage():
    stationimage.configure(file=stationimagestore[channelnumber])

# email function used on suggestions page to send suggestions for radio stations through gmail
def sendemail():
    #grabs content of entry boxes (email, pass, and content)
    emailcontent = emailentrybox.get(0.0,200.0).strip()
    emailaddress = usernameentry.get()
    thepass = passwordentry.get()
    try: #error catch to catch if user made a mistake with password or email or connection and displays error message
        with smtplib.SMTP('smtp.gmail.com',587) as smtp: #establishes an smtp connection on port 587
            smtp.ehlo()
            smtp.starttls() 
            smtp.ehlo()
            smtp.login(emailaddress,thepass) #starts smtp session and logs in with users credentials

            subject = "Python Internet Radio - Station Suggestion"
            body = emailcontent
            msg = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(emailaddress,"pe.mascherin@gmail.com",msg) #sends email to me
    except:
        messagebox.showerror("Email Error","There was an error with either the email address, your password, or your connection. Please check to make sure all of correct and working")
    
#JSON DATA GRAB
datad = json.loads(rad.urls) #loads the JSON radiolist info into datad
channelnumber = 0
urlstore = [] #the array of urls for radio stations
stationstore = [] #the array of radio names for the radio stations
stationimagestore = []
for url in datad['stations']: #loops through the 'stations' object in datad JSON
    urlstore.append(url['radiourl']) #appends the radio station urls to urlstore
    stationstore.append(url['radioname']) #appends the radio station names to stationstore
    stationimagestore.append(url['stationimage']) #appends the radio station logo to stationimagestore
textblobjson = json.loads(rad.suggesiontext) #loads suggestionpagemessage JSON list
suggestionsmessagetext = textblobjson['textblob'] 


#WIDGET DECLARATION
root = tk.Tk()
homescreenframe = tk.Frame(root)
suggestionframe = tk.Frame(root)
fowardimage = tk.PhotoImage(file="RadioResources/fowardfinal.png")
backimage = tk.PhotoImage(file="RadioResources/backfinal.png")
stopimage = tk.PhotoImage(file="RadioResources/stopfinal.png")
pauseimage = tk.PhotoImage(file="RadioResources/pausefinal.png")
playimage = tk.PhotoImage(file="RadioResources/playfinal.png")
suggestionimage = tk.PhotoImage(file="RadioResources/sbubble2.png")
homebuttonimage = tk.PhotoImage(file="RadioResources/homebutton.png")
stationimage = tk.PhotoImage()
stationfont = Font(family="Bahnschrift SemiBold",size=36)
statusfont = Font(family="Bahnschrift SemiBold",size=12)
suggestionfont = Font(family="Bahnschrift SemiBold",size=10)
playbutton = tk.Button(homescreenframe,image=playimage,command=lambda:playmedia(),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0)
pausebutton = tk.Button(homescreenframe,image=pauseimage,command=lambda:pausemedia(),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0)
stopbutton = tk.Button(homescreenframe,image=stopimage,command=lambda:stopmedia(),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0)
nextbutton = tk.Button(homescreenframe,image=fowardimage,command=lambda:switchstation(1),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0)
previousbutton = tk.Button(homescreenframe,image=backimage,command=lambda:switchstation(-1),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0)
volumeslider = tk.Scale(homescreenframe,from_=0,to=100,tickinterval=0,orient=HORIZONTAL,label="Volume",bg=basebgcolour,fg=stationtextcolour,command=volumecontrol)
radionametext = tk.Label(homescreenframe,text="Python Internet Radio",font=stationfont,fg=stationtextcolour,bg=basebgcolour)
statustext = tk.Label(homescreenframe,text="Ready to Play",font=statusfont,fg=statustextcolour,bg=basebgcolour)
stationimagelabel = tk.Label(homescreenframe,bg=basebgcolour,image=stationimage)
homefromsuggestion = tk.Button(suggestionframe,bg=basebgcolour,activebackground=basebgcolour,command=lambda:switchframe(homescreenframe),bd=0,height=50,image=homebuttonimage)
suggestionsbutton = tk.Button(homescreenframe,command=lambda:switchframe(suggestionframe),bg=basebgcolour,activebackground=basebgcolour,height=50,bd=0,image=suggestionimage)
stopfromsuggestion = tk.Button(suggestionframe,bg=basebgcolour,activebackground=basebgcolour,image=stopimage,height=50,command=lambda:stopmedia(),bd=0)
suggestionstitle = tk.Label(suggestionframe,text="Suggestions",font=stationfont,bg=basebgcolour,fg=stationtextcolour)
suggestionsmessage = tk.Message(suggestionframe,text=suggestionsmessagetext,bg=basebgcolour,fg=stationtextcolour,font=suggestionfont,width=300)
usernamelabelframe = tk.LabelFrame(suggestionframe,text="Email Address",width=100,height=40,fg=statustextcolour,bg=basebgcolour,bd=0)
passwordlabelframe = tk.LabelFrame(suggestionframe,text="Password",width=100,height=40,fg=statustextcolour,bg=basebgcolour,bd=0)
emailboxframe = tk.LabelFrame(suggestionframe,text="Email Content",width=130,height=40,fg=statustextcolour,bg=basebgcolour,bd=0)
usernameentry = tk.Entry(usernamelabelframe,bg=entryboxcolour,fg=statustextcolour,insertbackground=statustextcolour,font=suggestionfont,bd=0,width=30)
passwordentry = tk.Entry(passwordlabelframe,show="*",bg=entryboxcolour,fg=statustextcolour,insertbackground=statustextcolour,font=suggestionfont,bd=0,width=30)
emailentrybox = tk.Text(emailboxframe,fg=statustextcolour,bg=entryboxcolour,insertbackground=statustextcolour,width=30,height=3,font=suggestionfont,bd=0)
submitemailbutton = tk.Button(suggestionframe,text="Send!",bg=basebgcolour,fg=statustextcolour,activebackground=basebgcolour,activeforeground=statustextcolour,command=lambda: sendemail(),bd=0,font=statusfont)


#WIDGET PLACEMENT
playbutton.grid(row=3,column=1,sticky=(S,W,E),padx=4,pady=10)
pausebutton.grid(row=3,column=2,sticky=(S,E,W),pady=10,padx=2)
stopbutton.grid(row=3,column=0,sticky=(S,E,W),pady=10,padx=2)
nextbutton.grid(row=2,column=2,sticky=(E,W),pady=25,padx=6,rowspan=3)
previousbutton.grid(row=2,column=0,sticky=(E,W),pady=25,padx=6,rowspan=3)
volumeslider.grid(row=2,column=1,sticky=(N,E,W),padx=5,pady=50,rowspan=2)
radionametext.grid(row=0,column=0,sticky=(N,W,S),padx=10,pady=0,columnspan=3)
statustext.grid(row=1,column=0,sticky=(N,W),pady=0,padx=15,columnspan=3)
stationimagelabel.grid(row=0,column=2,sticky=(N,E,W),pady=10,rowspan=3)
suggestionsbutton.grid(row=1,column=2,sticky=(S,E,W),rowspan=2)
homefromsuggestion.grid(row=1,column=2,sticky=(N,S,E,W))
stopfromsuggestion.grid(row=2,column=2,sticky=(N,S,E,W))
suggestionstitle.grid(row=0,column=0,sticky=(N,W),padx=10,pady=5,columnspan=3)
suggestionsmessage.grid(row=0,column=2,sticky=(E,N,W),pady=10,padx=5,rowspan=3)
usernamelabelframe.grid(row=1,column=0,sticky=(E,W),pady=10,padx=10)
passwordlabelframe.grid(row=2,column=0,sticky=(N,E,W),padx=10,pady=10)
usernameentry.grid(row=0,column=0)
passwordentry.grid(row=0,column=0)
emailboxframe.grid(row=1,column=1,sticky=(S,E,W))
emailentrybox.grid(row=0,column=0)
submitemailbutton.grid(row=2,column=1,sticky=(N,W),padx=5,pady=5)

#VLC MEDIA CONFIGURATION 
theaudio = vlc.Media(urlstore[channelnumber])
player = vlc.MediaPlayer()
player.audio_set_volume(75)
volumeslider.configure(activebackground=basebgcolour,
    troughcolor=stationtextcolour,highlightthickness=0,length=50,font=statusfont,sliderrelief=FLAT,bd=0)
volumeslider.set(75)



#HOMESCREEN CONFIGURATION
homescreenframe.rowconfigure((0,1,2,3),weight=1)
homescreenframe.columnconfigure((0,1,2),weight=1)
homescreenframe.configure(bg=basebgcolour,width=750,height=300)
homescreenframe.grid(row=0,column=0,sticky=(N,S,E,W))
switchframe(homescreenframe)

#SETTINGS SCREEN CONFIGURATION
suggestionframe.rowconfigure((0,1,2,3),weight=1)
suggestionframe.columnconfigure((0,1,2),weight=1)
suggestionframe.configure(bg=basebgcolour,width=750,height=300)
suggestionframe.grid(row=0,column=0,sticky=(N,S,E,W))

#ROOT CONFIGURATION
root.rowconfigure((0),weight=1)
root.columnconfigure((0),weight=1)
root.configure(bg=basebgcolour)
root.resizable(FALSE,FALSE)
root.iconbitmap(r"RadioResources\radioicon.ico")
root.title("Internet Radio")
root.geometry("750x300+400+300")
root.mainloop()