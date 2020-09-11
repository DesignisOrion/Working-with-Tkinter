# Tutorial 9
# Drop down menus, toolbar and status bar ... YAY!
# This is the basic frame work of programs.


from tkinter import *


def doNothing():
    print("ok ok I won't....")


root = Tk()

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

root.mainloop()
