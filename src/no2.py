print("\033c");
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# SETTING THE SIZE OF THE CANVAS
rowMax = int(1000)
colMax = int(1000)
print('col, row =', colMax, ',', rowMax)

# THE USER DECIDE THE LINE WIDTH AND COLOR
lw = int(10); lr = 0; lg = 0; lb = 255
hw = int(lw/2) #calculate the half-half line width

# THE USER DECIDES THE POINT (VERTEX) DIAMETER AND COLOR
pd = int(1); pr = 255; pg = 255; pb = 255
hd = int(pd/2) #calculate the half point diameter

# USER ENTRY
# Lngkaran
y1, x2 = None, None
radiusMax = int(150)
batasStart = int(0.2*radiusMax)
batasEnd = int(0.6*radiusMax)

# Hexagon
y1 = 400; x1 = 285
x1a = float(x1) - 0.29
y2 = 400; x2 = 400
x2a = float(x2) + 0.29

# Polygon
y2_p, x2_p = 601, 600
y1_p, x1_p = 600, 600

Gambar = np.zeros(shape=(rowMax+1, colMax+1, 3), dtype=np.uint8)

def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
   # draw the first point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    # draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    # draw the horizontal line
    if dy <= dx:
        my = dy / dx
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            # if y % 50:
            #     print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    # draw the vertical line
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            # if x % 50:
            #     print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

def buatLingkaran(Gambar, y1, x1, radiusMax):
    for i in range(0, rowMax+1):
        # print('Loading...')
        for j in range(0, colMax+1):
            if ((i-y1)**2 + (j-x1)**2) >= 0 and ((i-y1)**2 + (j-x1)**2) < batasStart**2:
                Gambar[i, j, 2] = 255
            if ((i-y1)**2 + (j-x1)**2) >= batasStart**2 and ((i-y1)**2 + (j-x1)**2) < batasEnd**2:
                Gambar[i, j, 2] = 255 

def buatSegilima(Gambar, y1_p, x1_p, y2_p, x2_p, hd, hw, pr, pg, pb, lr, lg, lb):
    while y1_p <= 700:
        y2_p += 1
        y1_p += 1
        x2_p += 1
        x1_p -= 1
        hasil = buat_garis(Gambar, y1_p, x1_p, y2_p, x2_p, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil
 
    while y1_p <= 800:
        y2_p += 2
        y1_p += 2
        x2_p -= 1
        x1_p += 1
        hasil = buat_garis(Gambar, y1_p, x1_p, y2_p, x2_p, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil
    
def buatSegienam(Gambar, y1, x1, x1a, y2, x2, x2a, hd, hw, pr, pg, pb, lr, lg, lb):
    while y1 <= 500:
        y2 += 2
        y1 += 2
        x2 += 1
        x1 -= 1
        hasil = buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil
 
    while y1 <= 600:
        y2 += 2
        y1 += 2
        x2 -= 1
        x1 += 1
        hasil = buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil
        
hasil = buatLingkaran(Gambar, 200, 200, radiusMax)
hasil = buatSegilima(Gambar, y1_p, x1_p, y2_p, x2_p, hd, hw, pr, pg, pb, lr, lg, lb)
hasil = buatSegienam(Gambar, y1, x1, x1a, y2, x2, x2a, hd, hw, pr, pg, pb, lr, lg, lb)

print('Finish')

plt.figure("Jawaban Soal No 2")
plt.imshow(Gambar)
plt.show()