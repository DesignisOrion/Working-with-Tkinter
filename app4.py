# Tutorial #4 / 5
# Grid Layout
# In this lets create a User name and password (login screen)
# The Grid layout is similar to excel when dealing with rows and columns.

from tkinter import *

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

# What and where do we place it label. No more packing, we will use grid now.
# Sticky is what aligns the widgets / labels.
# The letter E stands for East. Think of it like a map.
# N = Up, S= Down, E= Right, W= Left.

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# creating a checkbox
# use columnspan to take over columns

c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)

root.mainloop()
