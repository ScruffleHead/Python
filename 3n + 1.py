from tkinter import *
import random

while True:
    inpt = input("input a positive integer pls: ")
    try:
        inpt = int(inpt)
    except:
        print("thats not an integer")
    else:
        inpt = int(inpt)
        if inpt > 0:
            break
        else:
            print("thats not positive")

allnums = [0, inpt]
while True:
    if inpt == 1:
        break
    if inpt % 2 == 0:
        inpt = int(inpt / 2)
    else:
        inpt = int(inpt * 3 + 1)
    allnums.append(inpt)

tk = Tk()
tk.title = "3n + 1"
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=300, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

currentnumber = -1
while True:
    currentnumber = currentnumber + 1
    canvas.create_line(500/len(allnums)*currentnumber, 300-(300/max(allnums)*allnums[currentnumber]), 500/len(allnums)*(currentnumber+1), 300-(300/max(allnums)*allnums[currentnumber+1]))
    tk.update()
    if currentnumber+2 == len(allnums):
        break
print("Done. There were a total of %s different generated numbers." % str(len(allnums)-2))
print("The highest of these numbers was %s." % str(max(allnums)))
