import tkinter
from tkinter import *

def clear():
    var.set("")

def solve():
    try:
        var.set(eval(var.get()))
    except SyntaxError:
        var.set("You mad?")

def addChar(ch):
    currentVal = var.get()
    var.set(currentVal+ch)

def addNumButton(num,index):
    button = tkinter.Button(lowerFrame, text = num, command = lambda: addChar(str(num)))
    button.grid(row = 2 + (index // 3), column=1+(index % 3), sticky="ew")
    
root = tkinter.Tk()
upperFrame = Frame(root)
upperFrame.pack()
lowerFrame = Frame(root,width = 500)

lowerFrame.pack()

var = StringVar()
label = Message(upperFrame, textvariable = var, relief = RAISED, width = 500, bg = 'white')
var.set("")
label.pack()
col1 = 0 #base column for row1

clearButton = tkinter.Button(lowerFrame, text ="Clear", command = clear)
clearButton.grid(row=1, column=col1, sticky="ew"); col1+=1
plusButton = tkinter.Button(lowerFrame, text ="+", command = lambda: addChar("+"))
plusButton.grid(row=1, column=col1, sticky="ew"); col1+=1
minusButton = tkinter.Button(lowerFrame, text ="-", command = lambda: addChar("-"))
minusButton.grid(row=1, column=col1, sticky="ew"); col1+=1
nums = [7,8,9,4,5,6,1,2,3,0] # Wanted order for number buttons
numberButtons = [None]*10 # Number buttons
for i in range(10):
    addNumButton(nums[i],i)

equalsButton = tkinter.Button(lowerFrame, text ="=", command = solve)
equalsButton.grid(row=1, column=col1, sticky="ew"); col1+=1

root.mainloop()
