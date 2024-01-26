# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:50:35 2024

@author: User
"""

from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("smile.png")
out = img.filter(ImageFilter.BLUR)
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()