import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import colorchooser

color = None
window = tk.Tk()

def choose_color():
    global color
    color = tk.colorchooser.askcolor(title="Choose color")[0]

def tampilkan_gambar():
    canvas = np.zeros(shape=(500, 500, 3), dtype=np.uint8)

    for i in range(300, 400):
        for j in range(100, 400):
            canvas[i, j] = list(color)

    plt.figure()
    plt.imshow(canvas)
    plt.show()

text = tk.Label(text='Program Membuat Persegi Panjang')
text.pack()

choose_color_button = tk.Button(window, text='Pilih warna', command=choose_color)
choose_color_button.pack()

draw_button = tk.Button(window, text='Tampilkan gambar', command=tampilkan_gambar)
draw_button.pack()
window.resizable(0, 0)
window.mainloop()