# Created by Calvin Dong - 12/28/2018
# Grade Calculator
# Learning tkinter Library

from tkinter import *

def addBox():
    # Creates a frame for the Entry boxes
    frame = Frame(root) 
    frame.pack()
    
    # Inserts entry boxes side by side (Grade, Weight)
    ent1 = Entry(frame) 
    ent1.grid(row=0, column=0)
    ent2 = Entry(frame)
    ent2.grid(row=0, column=1)
    
    # Appends a list to access info in showEntries()
    all_entries.append((ent1, ent2))  

def showEntries():
    # List for weighted value and second entry
    weighted = []  
    total_ent2 = []
    
    # Access all Entry values
    for number, (ent1, ent2) in enumerate(all_entries): 
        a = int(ent1.get())
        b = int(ent2.get())
        
        # c = the weighted value
        c = a*b 
        
        # Appends weighted value and weight value to be put in the formula
        weighted.append(int(c)) 
        total_ent2.append(b)
        
    # If user enters no grades, else, uses average formula
    if len(weighted) == 0:
        e = 0 
    else:
        e = round(sum(weighted) / sum(total_ent2), 2) 
        
    # Updates the Grade label
    var.set(e) 

all_entries = []
root = Tk()
root.title('Grade Calculator')
root.geometry("280x280")

# Frames to organize
topframe = Frame(root)
topframe.pack(side=TOP)
middleframe=Frame(root)
middleframe.pack(side=TOP)
buttonframes=Frame(root)
buttonframes.pack(side=TOP)
gradeweightframe=Frame(root)
gradeweightframe.pack(side=TOP)

Class_Label = Label(topframe, text="Class: ", bg='yellow').pack(side=LEFT)
Class_Name = Entry(topframe).pack(side=LEFT)

# To update the label constantly, set default as 0
var = StringVar() 
var.set(0)

GPA_label=Label(middleframe, text='Grade:', bg='blue', fg='yellow').pack(side=LEFT)
GPA = Label(middleframe, textvariable = var).pack(side=LEFT)

# Runs function if pressed
showButton = Button(buttonframes, text='Calculate', command=showEntries) 
showButton.pack()
addboxButton = Button(buttonframes, text='<Add Grade>', fg="Red", command=addBox) 
addboxButton.pack()

grade_label = Label(gradeweightframe, text="Grade |").pack(side=LEFT)
weight_label = Label(gradeweightframe, text="| Weight").pack(side=RIGHT)

root.mainloop()
