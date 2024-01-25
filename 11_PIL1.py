# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:53:18 2024

@author: User
"""

from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("smile.png")
out = img.rotate(45)
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()