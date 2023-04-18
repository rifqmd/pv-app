import matplotlib.pyplot as plt
import numpy as np

def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    if dy <= dx:
        my = dy / dx
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            if y % 50:
                print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            if x % 50:
                print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

def persegi_panjang(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb, pd, lw, e_size_outline, e_size_dot, e_x1, e_x2, e_y1, e_y2):
    row = int(1000)
    col = int(1000)

    x1, x2 = e_x1, e_x2
    y1, y2 = e_y1, e_y2
    # y1 = 200; x1 = 100
    # y2 = 200; x2 = 800
    
    #THE USER DECIDES THE POINT (VERTEX) DIAMETER AND COLOR
    pd = int(e_size_dot); pr = 0; pg = 0; pb = 255

    #THE USER DECIDE THE LINE WIDTH AND COLOR
    lw = int(e_size_outline); lr = 0; lg = 0; lb = 255
    hd = int(pd/2) #calculate the half point diameter
    hw = int(lw/2) #calculate the half-half line width

    #ARRAY UNTUK GAMBAR
    gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8) #latar hitam
    # gambar[:,:,:] = 255                                     #latar putih

    batas = (e_y1+e_y2)+1
    while y1 <= batas:
        y1 += 1
        y2 += 1
        hasil = buat_garis(gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lg, lb)
        gambar = hasil

    plt.figure("Rectangle")
    plt.imshow(hasil)
    plt.show()