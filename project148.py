# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:47:55 2022

@author: aarya_fhxkeec
"""

from tkinter import*
import random

root = Tk()
root.title("What to pack?")
root.geometry("800x600")

list_items = Label(root, text="Items To Take: Water, Basket, Food, Umbrella and more stuff")
item_pack = Label(root)

def what_item() : 
    rN = random.sample(range(1,5), 1)
    item_pack["text"] = "Item Number: " + str(rN)
    
btn = Button(root, text="Find Item Number To Pack", command=what_item)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

list_items.place(relx=0.5, rely=0.4, anchor=CENTER)
item_pack.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()