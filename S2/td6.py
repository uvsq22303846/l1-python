import tkinter as tk
import numpy as np
import PIL as pil
from PIL import Image, ImageTk
from tkinter import filedialog


def save(matPix, filename):
    Image.fromarray(matPix).save(filename)


def load(filename):
    return np.array(pil.Image.open(filename))


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
    filename = filedialog.askopenfile(mode="rb", title="Choose a file")
    img = Image.open(filename)
    nomImgCourante = filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:
        canvas = tk.Canvas(widg, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)
        create = False
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)


def modify(matrice):
    global imgModif
    global nomImgCourante
    save(matrice, "modif.png")
    imgModif = ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    canvas["width"] = imgModif.width()
    canvas["height"] = imgModif.height()
    nomImgCourante = "modif.png"


def derniers_bits(x, k):
    return x % (1 << k)


def encoder_kbits(x, y, k):
    return x - derniers_bits(x, k) + derniers_bits(y, k)


def encoder_entier(e, pixel):
    rouge = encoder_kbits(pixel[0], e, 3)
    vert = encoder_kbits(pixel[1], e >> 3, 3)
    bleu = encoder_kbits(pixel[2], e >> 6, 2)
    return (rouge, vert, bleu)


def coder():
    texte_a_cacher = entree.get()
    mat = load(nomImgCourante)
    mat[0, 0] = encoder_entier(len(texte_a_cacher), mat[0, 0])
    i = 1
    j = 0
    count = 0
    while count < len(texte_a_cacher):
        mat[i][j] = encoder_entier((ord(texte_a_cacher[count])), mat[i][j])
        j += 1
        count += 1
        if i >= mat.shape[0]:
            i = 0
            j += 1
    modify(mat)


def decoder_pixel(pixel):
    vr = derniers_bits(pixel[0], 3)
    vg = derniers_bits(pixel[1], 3)
    vb = derniers_bits(pixel[2], 2)
    return vr + (vg << 3) + (vb << 6)


def decoder():
    mat = load(nomImgCourante)
    sortie = ""
    taille_texte = decoder_pixel(mat[0, 0])

    i = 1
    j = 0
    count = 0
    while count < taille_texte:
        caractere = chr(decoder_pixel(mat[i, j]))
        sortie += caractere
        i += 1
        count += 1
        if i >= mat.shape[0]:
            i = 0
            j += 1
    label_decodage.config(text=sortie)


affi = tk.Tk()
affi.title("Stéganographie")


entree = tk.Entry(affi, width=20, font=("helvetica", "20"))
entree.grid(row=0, column=0)

bouton_coder = tk.Button(affi, text="Coder texte", fg="black", width=15, command=coder)
bouton_coder.grid(row=1, column=0)

bouton_decoder = tk.Button(affi, text="Décoder texte", fg="black", width=15, command=decoder)
bouton_decoder.grid(row=2, column=0)

label_decodage = tk.Label(affi, text="Décode moi !")
label_decodage.grid(row=3, column=0)

bouton = tk.Button(affi, text="Charger", fg="black", width=15, command=lambda: charger(affi))
bouton.grid(row=5, column=0)

btn = tk.Button(affi, text="Quitter", fg="black", width=8, command=affi.destroy)
btn.grid(row=5, column=2, sticky="E")

affi.mainloop()
