import firstfileResources.testclass as ts
import tkinter as tk
#the start of my tkinter projects
#MAIN RUN FILE MUST ALWAYS BE IN THE BASE WORKSPACE FOLDER (TkinterProjects) 
#ANYWHERE ELSE AND THE IMPORTS WONT WORK CORRECTLY FOR GOD KNOWS WHAT REASONS
print("hey buddy time to start tkinter")
ts.Testmeplz.imatest()
number = 1
def tkinterbuttons():
    print("you made it")
    labelappear = tk.Label(root,text="big boi label has appeared")
    if(labelappear.winfo_exists):
        labelappear.pack()
    else:
        pass
    
    
    

root = tk.Tk()
text1 = tk.Label(root,text="hey buddy how ya doin in tkinter")
text1.pack()
firstbutton = tk.Button(root,text="big boy button",command=tkinterbuttons)
firstbutton.pack()

root.geometry("500x760")
root.mainloop()