# Tutorial Number 1
# Goal: Basic setup of tkinter, showing text, etc.

# importing the modules
from tkinter import ttk
from tkinter import *

# root is the main window. Doesnt have to be named such but is very common.
root = Tk()
theLabel = Label(root, text="This is too easy")
theLabel.pack()

# keep the program running until closes.
root.mainloop()
