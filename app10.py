# Tutorial #10 / 11
# Goals: Learning toolbars and status bars

from tkinter import *


def doNothing():
    print("ok ok I won't....")


root = Tk()

# ----- Main Menu -------

# Creating a menu

menu = Menu(root)

# configuring the menu
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ---- Creating the toolbar ----
# These are typically shown of icons... which we willlearn next.

toolbar = Frame(root, bg='blue')

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)


# displaying the toolbar
toolbar.pack(side=TOP, fill=X)


# ------- Status Bar --------
# bd = border
# relief
# anchor

status = Label(root, text="Preparing to do nothing...",
               bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()
