# Created by Calvin Dong - 12/28/2018
# Learning tkinter Library

from tkinter import *

def addBox():
    frame = Frame(root) # Creates a frame for the Entry boxes
    frame.pack()

    ent1 = Entry(frame) # Inserts entry boxes side by side (Grade, Weight)
    ent1.grid(row=0, column=0)
    ent2 = Entry(frame)
    ent2.grid(row=0, column=1)

    all_entries.append((ent1, ent2))  # Appends a list to access info in showEntries()

def showEntries():
    weighted = [] # List for weighted value
    total_ent2 = [] # List for weight value (second entry)
    for number, (ent1, ent2) in enumerate(all_entries): # Access all Entry values
        a = int(ent1.get())
        b = int(ent2.get())
        c = a*b # c = the weighted value
        weighted.append(int(c)) # Appends weighted value for to be put in the formula
        total_ent2.append(b) # Apends weight value for the formula

    if len(weighted) == 0:
        e = 0 # If user enters no grades
    else:
        e = round(sum(weighted) / sum(total_ent2), 2) # Formula for average

    var.set(e) # Updates the Grade label

all_entries = []
root = Tk()
root.title('Grade Calculator')
root.geometry("280x280")

topframe = Frame(root) # Frames to organize
topframe.pack(side=TOP)
middleframe=Frame(root)
middleframe.pack(side=TOP)
buttonframes=Frame(root)
buttonframes.pack(side=TOP)
gradeweightframe=Frame(root)
gradeweightframe.pack(side=TOP)

Class_Label = Label(topframe, text="Class: ", bg='yellow').pack(side=LEFT)
Class_Name = Entry(topframe).pack(side=LEFT)

var = StringVar() # To update the label constantly
var.set(0) # Default value

GPA_label=Label(middleframe, text='Grade:', bg='blue', fg='yellow').pack(side=LEFT)
GPA = Label(middleframe, textvariable = var).pack(side=LEFT)

showButton = Button(buttonframes, text='Calculate', command=showEntries) # Runs function if pressed
showButton.pack()

addboxButton = Button(buttonframes, text='<Add Grade>', fg="Red", command=addBox) # Runs function if pressed
addboxButton.pack()

grade_label = Label(gradeweightframe, text="Grade |").pack(side=LEFT)
weight_label = Label(gradeweightframe, text="| Weight").pack(side=RIGHT)

root.mainloop()
