import tkinter as tk
import numpy as np
import PIL as pil
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import simpledialog

def save(matPix, filename):
    Image.fromarray(matPix).save(filename)

def load(filename):
    return np.array(Image.open(filename))

create = True
nomImgCourante = ""
nomImgDebut = ""

def charger(widg):
    global create
    global photo
    global img 
    global canvas 
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename = filedialog.askopenfile(mode = "rb", title = "Choose a file")
    img = Image.open(filename)
    nomImgCourante = filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(widg)
    if create:
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0, 0, anchor = tk.NW, image = photo)
        canvas.grid(row = 0, column = 1, rowspan = 4, columnspan = 2)
        create = False
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0, 0, anchor = tk.NW, image = photo)
        canvas.grid(row = 0, column = 1, rowspan = 4, columnspan = 2)

def modifier(matrice):
    global imgModif
    global nomImgCourante
    save(matrice, "modif.png")
    imgModif = ImageTk.PhotoImage(file = "modif.png")
    canvas.itemconfigure()