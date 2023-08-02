# ----------------------------------------------------------------------------------
# Ryan (RM220507) - 2023
# Raspberry Pi Pinout Display
# A simple application in Tkinter to display an image of the RPi Pinout diagram
# ----------------------------------------------------------------------------------

# The Raspberry Pi is a trademark of the Raspberry Pi Foundation

import tkinter as tk
from PIL import Image, ImageTk
from os.path import dirname

root = tk.Tk()
root.geometry("1032x593")
root.resizable(False, False)

root.title("RPi Pinout")

icon = ImageTk.PhotoImage(file=dirname(__file__) + "/icon.png")
root.iconphoto(False, icon)

image = Image.open(dirname(__file__) + "/pinout.png")
resized = image.resize((1032, 593))
image_tk = ImageTk.PhotoImage(resized)

tk.Label(image=image_tk).place(x=0, y=0)

root.mainloop()