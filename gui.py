### Work in Progress ###

from tkinter import *
 
def addBox():
    frame = Frame(root)
    frame.pack()

    ent1 = Entry(frame)
    ent1.grid(row=0, column=0)

    ent2 = Entry(frame)
    ent2.grid(row=0, column=1)

    all_entries.append((ent1, ent2))

def showEntries():
    total_weight = []
    total_ent2 = []
    for number, (ent1, ent2) in enumerate(all_entries):
        a = int(ent1.get())
        b = int(ent2.get())
        c = a*b
        total_weight.append(c)
        total_ent2.append(b)
        
    sum = 0
    
    for i in range(len(total_weight)):
        d = total_weight[i]/total_ent2[i]
        sum += d
        
    if len(total_weight) == 0:
        e = 0
    else:
        e = sum/len(total_weight)

    print (e)
    return e

all_entries = []
root = Tk()
root.geometry("280x280")

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

var = StringVar()
var.set(showEntries())

GPA_label=Label(middleframe, text='GPA:', bg='blue', fg='yellow').pack(side=LEFT)
GPA = Label(middleframe, textvariable = var).pack(side=LEFT)

showButton = Button(buttonframes, text='Calculate', command=showEntries)
showButton.pack()

addboxButton = Button(buttonframes, text='<Add Grade>', fg="Red", command=addBox)
addboxButton.pack()

grade_label = Label(gradeweightframe, text="Grade |").pack(side=LEFT)
weight_label = Label(gradeweightframe, text="| Weight").pack(side=RIGHT)

root.mainloop()
