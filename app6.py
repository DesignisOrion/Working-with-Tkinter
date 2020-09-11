# Tutorial # 6
# Binding functions to Layouts aka connecting functions to widgets.


from tkinter import *

root = Tk()

'''
def printName():
    print('Hello, my name is Orion!')


button_1 = Button(root, text='Print Name', command=printName)
button_1.pack()
'''

# Second technique is using event and bind.
# event : something that occurs
# bind: takes the event and what function when it does occur.


def printName(event):
    print('Hello, Example for Events')


button_1 = Button(root, text="Print my name")
button_1.bind('<Button-1>', printName)
button_1.pack()
root.mainloop()
