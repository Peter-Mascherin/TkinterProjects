#A simple internet radio app where you can listen to your favourite stations as well as customize the theme of the app
#Built by peter mascherin

import tkinter as tk
from tkinter.constants import *

root = tk.Tk()

placeholderlabel = tk.Label(text="Placeholder text",bg="#3D3939",fg="#FFFFFF")
placeholderlabel.grid(row=1,column=1,sticky=(N,S,E,W))

root.rowconfigure((0,1,2),weight=1)
root.columnconfigure((0,1,2),weight=1)
root.configure(bg="#3D3939")
root.iconbitmap(r"RadioResources\radioicon.ico")
root.title("Internet Radio")
root.geometry("500x300")
root.mainloop()