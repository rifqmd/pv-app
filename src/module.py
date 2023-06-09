import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# prgress bar
from tkinter.ttk import Progressbar
import time

def buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    if dy <= dx:
        my = dy / dx
        # if dy != 0:
        #     my = dy / dx
        # else:
        #     print("Tidak bisa membagi dengan nol.")
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            # if y % 50:
            #     print('x, y = ', x, ',', y)
            print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            # if x % 50:
                # print('x, y = ', x, ',', y)
            print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb
    return gambar

def buat_titik(gambar, r, x, y, pr, pg, pb,):
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if ((i - x) ** 2 + (j - y) ** 2) <= (r ** 2):
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb
    return gambar
  
def buat_persegi(gambar, y1, x1, y2, x2, pd, pw, pr, pg, pb, lr, lg, lb):
    hd = int(pd/2)
    hw = int(pw/2)
    
    batas  = (y1+y2) + 1
    while y1 <= batas:
        y1 += 1
        y2 += 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
        
    plt.figure("Rectangle")
    plt.imshow(hasil)
    plt.show()

def buat_segilima(gambar, y1, x1, y2, x2, pd, pw, pr, pg, pb, lr, lg, lb):
    hd = int(pd/2)
    hw = int(pw/2)
    
    batas_a = y1 * 2
    while y1 <= batas_a:
        y2 += 1
        y1 += 1
        x2 += 1
        x1 -= 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
    
    selisih = batas_a / 2
    batas_b = batas_a + selisih
    while y1 <= batas_b:
        y2 += 2
        y1 += 2
        x2 -= 1
        x1 += 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
    
    plt.figure("Hexagon")
    plt.imshow(hasil)
    plt.show()

def buat_segienam(gambar, y1, x1, y2, x2, pd, pw, pr, pg, pb, lr, lg, lb):
    hd = int(pd/2)
    hw = int(pw/2)
    
    batas_a = y1 * 2
    while y1 <= batas_a:
        y2 += 2
        y1 += 2
        x2 += 1
        x1 -= 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
    
    selisih = batas_a / 2
    batas_b = batas_a + selisih
    while y1 <= batas_b:
        y2 += 2
        y1 += 2
        x2 -= 1
        x1 += 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
    
    plt.figure("Hexagon")
    plt.imshow(hasil)
    plt.show()

def buat_segitiga(gambar, y1, x1, y2, x2, pd, pw, pr, pg, pb, lr, lg, lb):
    hd = int(pd/2)
    hw = int(pw/2)
    
    batas_a = y1 * 2
    while y1 <= batas_a:
        y2 += 1
        y1 += 1
        x2 += 1
        x1 -= 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        gambar = hasil
    
    plt.figure("Segitiga")
    plt.imshow(hasil)
    plt.show()
def buat_lingkaran(gambar, r, x, y, pr, pg, pb):
    hasil = buat_titik(gambar, r, x, y, pr, pg, pb)
    
    plt.figure("Lingkaran")
    plt.imshow(hasil)
    plt.show()

def progress_bar():
    
    progress = Progressbar(root, length=280, orient='horizontal', mode='determinate')
    progress.grid(row=0, )
    jumlah = Label(root, text=' ')
    jumlah.grid(row=1)
    
    def count():
        return f"progress : {progress['value']}%"

    def start():
        while progress['value'] < 100:
            progress['value'] += 1
            jumlah['text'] = count()
            time.sleep(0.05)
            root.update_idletasks()

    btn = Button(root, text='start', command=start)
    btn.grid()