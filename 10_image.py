# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:59:48 2024

@author: User
"""

from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file = path)
    imageLabel.configure(image = img)
    imageLabel.image = img

window = Tk()

photo = PhotoImage(file="orange.png")
imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='Submit', command=change_img)
button.pack()

window.mainloop()