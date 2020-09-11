# Tutorial Number 2
# Goal: Widgets, Containers, Buttons

# importing the modules
from tkinter import ttk
from tkinter import *

root = Tk()

# making top frame
topFrame = Frame(root)
topFrame.pack()

# making bottom frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Adding widgets

# buttons
# We will do 3 buttons on the top and 1 on the bottom.

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

# This is what makes the widgets / labels show.
# On default, everything is stacked on top of each other.
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
