﻿from tkinter import Tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os

# This is a fork of Kicomav, an antivirus made in Python.
# New Author: RenderBr

#changing compass directions bcuz it's annoying
right = E
top = N
left = W
bottom = S

autoremove = None
autoupdate = None
languageList = []
languageList.append('English')
languageList.append('Chinese')
languageList.append('Spanish')
selectedLanguage = languageList[0]

root = Tk()

#Main frame
mainframe = Frame(root, height=500, width=1000, bg="black", relief=SUNKEN)
mainframe.pack()

#
#Configuring root and Top Window
#
root.wm_title("Uni Antivirus")
root.resizable(0,0)

def scanCertainFile():
    file = askopenfilename()

def quickScan():
    print("Scanning")
    tkinter.messagebox.showinfo("Scan complete", "The scan has been completed!")

def optionsWindow():
    options = Toplevel()

    autoRemove = Checkbutton(options, text="Automatically remove found threats.", variable=autoremove)
    autoRemove.pack()

    autoUpdate = Checkbutton(options, text="Automatically update definitions while computer is in idle state.", variable=autoupdate)
    autoUpdate.pack()

    language = OptionMenu(options, selectedLanguage, *languageList)
    language.pack()

    options.resizable(0,0)
    options.wm_title("Settings")



title = Label(mainframe, text="Uni Antivirus", fg="white", bg="black")
title.config(font=("Arial", 44))
title.pack(side=TOP)
runQuickScan = Button(mainframe, text="Quick Scan", command=quickScan, fg="white", bg="gray")
runQuickScan.pack(side=LEFT)
runDirScan = Button(mainframe, text="Scan in a certain directory", command=quickScan, fg="white", bg="gray")
runDirScan.pack(side=LEFT)
runOneFileScan = Button(mainframe, text="Scan one file", command=scanCertainFile, fg="white", bg="gray")
runOneFileScan.pack(side=LEFT)
settingsButton = Button(mainframe, text="Settings", command=optionsWindow, fg="white", bg="gray")
settingsButton.pack(side=LEFT)





root.mainloop()