# Tutorial # 8
# Using classes
# This will be the correct way to build all programs.

from tkinter import *

# Create a class
# This one is called OrionButtons lol.


class OrionButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(
            frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('Wow, this actually worked!')


root = Tk()
b = OrionButtons(root)
root.mainloop()
