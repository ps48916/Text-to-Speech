from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pyttsx3

def play():
    #command to convert Text into Audio
    audio=data.get("1.0", tk.END)
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def pop_up():
    #Command to Save file
    def save_file():
        audio2=data.get("1.0", tk.END)
        engine=pyttsx3.init()
        fnam=enter.get()
        engine.save_to_file(audio2,fnam+".mp3")
        engine.runAndWait()
        win.destroy()
        
    #GUI for popup
    win=tk.Toplevel()
    win.wm_title("Save Audio")
    l=tk.Label(win,text="File Name :")
    l.grid(row=0, column=0)
    enter=tk.Entry(win)
    enter.grid(row=0, column=1, padx=2)
    b3=ttk.Button(win,text="Save", command=save_file)
    b3.grid(row=1, column=0,padx=5, pady=5)
    b4=ttk.Button(win, text="Cancel", command=win.destroy)
    b4.grid(row=1, column=1,padx=5, pady=5)

#Main GUI    
root=tk.Tk()
root.title("Text to speech")
root.geometry("800x500")
label=tk.Label(text="Enter Your Text Below:-")
label.pack()
label.config(fon=("Times",20,"bold"))
data=ScrolledText(root)
data.pack()
b1=tk.Button(text="Play", command=play)
b1.pack(side='left',padx=40, pady=10)
b2=tk.Button(text="Save Audio", command=pop_up)
b2.pack(side='left', pady=10)
b3=tk.Button(text="Exit", command=root.destroy)
b3.pack(side='left',padx=40, pady=10)

root.mainloop()
