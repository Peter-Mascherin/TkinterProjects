import firstfileResources.testclass as ts
import tkinter as tk
#the start of my tkinter projects
#MAIN RUN FILE MUST ALWAYS BE IN THE BASE WORKSPACE FOLDER (TkinterProjects) 
#ANYWHERE ELSE AND THE IMPORTS WONT WORK CORRECTLY FOR GOD KNOWS WHAT REASONS
print("hey buddy time to start tkinter")
def tkinterbuttons():
    labelappear = tk.Label(root,text=ts.Testmeplz.imatest(1))
    if(labelappear.winfo_exists):
        labelappear.pack()
    else:
        pass
    
    
    

root = tk.Tk()
text1 = tk.Label(root,text="hey buddy how ya doin in tkinter")
text1.pack()
firstbutton = tk.Button(root,text=ts.Testmeplz.imatest(2),command=tkinterbuttons,width=15,height=2)
firstbutton.pack()

#firstbutton.config(width=100,height=50)
root.geometry("600x500")
root.title("Tkinter Test Run")
root.mainloop()