import numpy as np
import matplotlib.pyplot as plt

# Import fungsi buat_persegi dari file persegi.py
from module import buat_persegi

#ARRAY UNTUK GAMBAR
gambar = np.zeros(shape=(1000, 1000, 3), dtype=np.int16) #latar hitam
gambar[:,:,:] = 255                                     #latar putih

# Meminta input dari user untuk nilai y1, y2, x1, dan x2
y1 = int(input("Masukkan nilai y1: "))
y2 = int(input("Masukkan nilai y2: "))
x1 = int(input("Masukkan nilai x1: "))
x2 = int(input("Masukkan nilai x2: "))
hd, hw, pr, pg, pb, lr, lg, lb = 0, 0, 0, 0, 0, 0, 0, 0

# Memanggil fungsi buat_persegi
buat_persegi(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)

# Menampilkan gambar
plt.show()