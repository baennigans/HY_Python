# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:08:58 2024

@author: User
"""

import tkinter as tk

def open():
    pass

def quit():
    window.quit()
    
window = tk.Tk()    
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)

menubar.add_cascade(label="파일", menu=filemenu)

window.config(menu=menubar)
window.mainloop()