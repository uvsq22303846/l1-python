import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import simpledialog

create = True

def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename = filedialog.askopenfile(mode= "rb", title = "Choose a file")
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0, 0, anchor = tk.NW, image = photo)
        canvas.pack()
        create = False
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0, 0, anchor = tk.NW, image = photo)
        canvas.pack()

root = tk.Tk()
root.title("J'apprends Tkinter")
bouton = tk.Canvas(root, text = "Charger", command = lambda: charger(canvas)).pack()
canvas = tk.Canvas(root, width = 300, height = 300).pack()


root.mainloop()