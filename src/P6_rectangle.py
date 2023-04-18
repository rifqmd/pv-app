import numpy as np
import matplotlib.pyplot as plt
from lib_groupC import buat_garis

#SETTING THE SIZE OF THE CANVAS
row = int(1000)
col = int(1000)
print('col, row =', col, ',', row)

# MAIN PROGRAM
# USER ENTRY
#THE USER INFORES THE COORDINATE OF THE TWO POINT FOR THE LINE.
y1 = 200; x1 = 100
y2 = 200; x2 = 800

#THE USER DECIDES THE POINT (VERTEX) DIAMETER AND COLOR
pd = int(1); pr = 0; pg = 0; pb = 255

#THE USER DECIDE THE LINE WIDTH AND COLOR
lw = int(10); lr = 0; lg = 0; lb = 255
hd = int(pd/2) #calculate the half point diameter
hw = int(lw/2) #calculate the half-half line width

#ARRAY UNTUK GAMBAR
gambar = np.zeros(shape=(row, col, 3), dtype=np.int16) #latar hitam
gambar[:,:,:] = 255                                     #latar putih

while y1 <= 401:
    y1 += 1
    y2 += 1
    hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lg, lb)
    gambar = hasil

plt.figure("Rectangle")
plt.imshow(hasil)
plt.show()