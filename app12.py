# Tutorial 12
# MessageBox


from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo(
    'Window Title', 'You will become a great Software Developer')

answer = tkinter.messagebox.askquestion('Question 1', "Do you like Python?")

if answer == 'yes':
    print('YEAAAAAAHHHH. Go Py Devs!')
root.mainloop()
