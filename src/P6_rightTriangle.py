import matplotlib.pyplot as plt
import numpy as np
import warnings

from module import buat_garis
print("\033c")
warnings.filterwarnings('ignore')

# coordinate lines
y1 = 100; x1 = 100 # segitiga 1 batas atas
y2 = 100; x2 = 400 # segitiga 1 batas bawah

 
# point (vertex) diameter and color
pd = int(3)  # ukuran titik
pr = 0
pg = 0
pb = 255
 
# line width and color
lw = int(10)
lr = 0
lg = 0
lb = 255
 
# setting size canvas
row = int(1000)
col = int(1000)
print('row, col = ', row, ',', col)
 
 
# MAIN PROGRAM
# preparing the black canvas
hd = int(pd/2)  # half point diameter
hw = int(lw/2)  # half line width
# preparing black canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
Gambar[:, :, :] = 255  # white canvas

while y1 <= 400:
    y1 += 1
    hasil = buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
    Gambar = hasil

plt.figure('Right Triangle')
plt.imshow(hasil)
plt.show()