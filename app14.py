# Tutorial 14
# Adding Icons & Images
# Must set the photos in a label first, then you can place in main window(root)

from tkinter import *

root = Tk()

photo = PhotoImage(file='MeOrion.png')
label = Label(root, image=photo)
label.pack()

root.mainloop()
