from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.ttk import Progressbar
import time
import tkinter.font

from tkinter import colorchooser

# librarty bangun ruang
from module import buat_persegi

import matplotlib.pyplot as plt
import numpy as np

# from functools import partial

# def changeFont():
#     changeFont = tkinter.font.Font(size=20)

class FirstPage:
    def __init__(self, parent, title):
        self.parent = parent
        self.settingWindow(title)
        self.settingComponent()

    def settingWindow(self, title):
        # atur ukuran window
        self.parent.geometry('500x300')
        
        # atur title
        self.parent.title(title)
        
    def settingComponent(self):
        main_frame = Frame(self.parent, bd=5)
        main_frame.pack(fill=BOTH, expand=YES)
        # start = partial(SecondPage, main_frame)

        Label(main_frame, text="Selamat Datang di Aplikasi Kelompok C").place(x=130, y=30)
        
        self.btn_start = Button(main_frame, text='Start', command=self.onKlikStart, activeforeground='red', width=23, bd=5)
        self.btn_exit = Button(main_frame, text='Exit', command=self.onKlikKeluar, activeforeground='red', width=23, bd=5)
        
        self.btn_start.pack(side='left')
        self.btn_exit.pack(side='right')
        
    def onKlikKeluar(self, event=None):
        if messagebox.askyesno('Konfirmasi', 'Keluar dari program?', parent=self.parent):
            self.parent.destroy()

    def onKlikStart(self):
        self.parent.destroy()
        root = Tk()
        app = SecondPage(root)
        root.mainloop()
    
class SecondPage:
    def __init__(self, parent):
        self.parent = parent
        self.settingWindow()
        self.settingComponent()

    def settingWindow(self):
        self.parent.geometry('500x150')
        self.parent.resizable(0, 0)
        self.parent.title('::Pilih Jenis Objek Bangun Ruang 2D::')
        
    def settingComponent(self):
        main_frame = Frame(self.parent, bd=5)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # set back button
        self.btn_back = Button(main_frame, text='Kembali', command=self.kembali, activeforeground='red', width=5)
        self.btn_back.place(x=20,)
        
        Label(main_frame, text='Select bangun ruang yang diinginkan').pack()
        
        # 48x48 icon logo
        
        # set button square
        self.imgSquare = PhotoImage(file='img/square.png')
        self.btnSquare = Button(main_frame, text='Square', image=self.imgSquare, compound='top', command=self.onKlikSquare, width=70)
        # self.btnSquare.pack(side='left', fill=Y)
        self.btnSquare.place(x=10, y=40)
        
        # set button rectangle
        self.imgRectangle = PhotoImage(file='img/rectangle.png')
        self.btnRectangle = Button(main_frame, text='Rectangle', image=self.imgRectangle, compound='top', command=self.onKlikRectangle, width=70)
        self.btnRectangle.place(x=90, y=40)
        
        # set button circle
        self.imgCircle = PhotoImage(file='img/circle.png')
        self.btnCircle = Button(main_frame, text='Circle', image=self.imgCircle, compound='top', command=self.onKlikCircle, width=70)
        self.btnCircle.place(x=170, y=40)

        # set button tringle
        self.imgTriangle = PhotoImage(file='img/triangle.png')
        self.btnTriangle = Button(main_frame, text='Triangle', image=self.imgTriangle, compound='top', command=self.onKlikTriangle, width=70)
        self.btnTriangle.place(x=250, y=40)

        # set button tringle
        self.imgPentagon = PhotoImage(file='img/pentagon.png')
        self.btnPentagon = Button(main_frame, text='Pentagon', image=self.imgPentagon, compound='top', command=self.onKlikPentagon, width=70)
        self.btnPentagon.place(x=330, y=40)
        
        # set button hexagon
        self.imgHexagon = PhotoImage(file='img/hexagon.png')
        self.btnTriangle = Button(main_frame, text='Hexagon', image=self.imgHexagon, compound='top', command=self.onKlikHexagon, width=70)
        self.btnTriangle.place(x=410, y=40)
        
    def onKlikSquare(self, event=None):
        root = Tk()
        root.geometry('350x500')
        root.title('::Bangun Ruang Persegi::')\
            
        def choose_color():
            global color
            color = colorchooser.askcolor(title="Choose color")[0]
            # colorchooser.askcolor()
        
        def tampilkan_gambar():
            # Buat gambar persegi dengan titik awal (200, 100) dan titik akhir (200, 800)
            gambar = np.zeros((1000, 1000, 3), dtype=np.int16)
            y1, x1 = 200, 100
            y2, x2 = 200, 600
            hd, hw, pr, pg, pb, lr, lg, lb = 0, 0, 0, 0, 0, 0, 0, 0
            buat_persegi(gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)
            
        # def process():
        #     # pass
        #     x1 = int(e_x1.get())
        #     x2 = int(e_x2.get())
        #     y1 = int(e_y1.get())
        #     y2 = int(e_y2.get())
        #     outline = int(e_size_outline.get())
        #     fill = int(e_size_dot.get())
        #     view = persegi_panjang(x1, x2, y1, y2, outline, fill)
            
            # class orang:
            #     def __init__(self, size_outline, size_dot, x1, x2, y1, y2):
            #         self.size_outline = size_outline
            #         self.size_dot = size_dot
            #         self.x1 = x1
            #         self.x2 = x2
            #         self.y1 = y1
            #         self.y2 = y2
            
            # ditampilkan = persegi_panjang(e_size_outline.get(), e_size_dot.get(), e_x1.get(), e_x2.get(), e_y1.get(), e_y2.get())

        judul = Label(root, text="Menentukan Ukuran Dan Warna").place(x=70, y=10)
        size_outline = Label(root, text="‣ Ukuran Outline").place(x=20, y=50)
        e_size_outline = Entry(root, width=10).place(x=20, y=75)
        
        size_dot = Label(root, text="‣ Ukuran Titik").place(x=200, y=50)
        e_size_dot = Entry(root, width=10).place(x=200, y=75)
        
        color_outline = Label(root, text="‣ Warna Outline").place(x=20, y=115)
        # btn_warna_outline = Button(root, text='Click', command=choose_color).place(x=20, y=140)
        
        color_fill = Label(root, text="‣ Warna Fill").place(x=200, y=115)
        # btn_warna_fill = Button(root, text='Click', command=choose_color).place(x=200, y=140)
        
        judul = Label(root, text="Menentukan Ukuran Dan Warna").place(x=70, y=200)
        x1 = Label(root, text="‣ Ukuran X-1").place(x=20, y=240)
        e_x1 = Entry(root, width=10).place(x=20, y=265)
        
        x2 = Label(root, text="‣ Ukuran X-2").place(x=200, y=240)
        e_x2 = Entry(root, width=10).place(x=200, y=265)
        
        y1 = Label(root, text="‣ Ukuran Y-1").place(x=20, y=305)
        e_y1 = Entry(root, width=10).place(x=20, y=330)
        
        y2 = Label(root, text="‣ Ukuran Y-2").place(x=200, y=305)
        e_y2 = Entry(root, width=10).place(x=200, y=330)
        
        choose_color_button = Button(root, text='Pilih warna', command=choose_color)
        choose_color_button.pack()
        
        btn_process = Button(root, text='Proses', command=tampilkan_gambar)
        # btn_process = Button(root, text='PROCESS', command=process)
        btn_process.place(x=200, y=400)
        # process = rectangle(e_size_outline, e_size_dot, e_x1, e_x2, e_y1, e_y2, btn_warna_outline, btn_warna_fill)
        
        
        # self.parent.destroy()
        root.mainloop()

    def onKlikRectangle(self):
        root = Tk()
        root.geometry('350x500')
        root.title('::Bangun Ruang Persegi Panjang::')\
            
        def choose_color():
            colorchooser.askcolor()

        judul = Label(root, text="Menentukan Ukuran Dan Warna").place(x=70, y=10)
        size_outline = Label(root, text="‣ Ukuran Outline").place(x=20, y=50)
        e_size_outline = Entry(root, width=10).place(x=20, y=75)
        
        size_dot = Label(root, text="‣ Ukuran Titik").place(x=200, y=50)
        e_size_dot = Entry(root, width=10).place(x=200, y=75)
        
        color_outline = Label(root, text="‣ Warna Outline").place(x=20, y=115)
        btn_warna_outline = Button(root, text='Click', command=choose_color).place(x=20, y=140)
        
        color_fill = Label(root, text="‣ Warna Fill").place(x=200, y=115)
        btn_warna_fill = Button(root, text='Click', command=choose_color).place(x=200, y=140)
        
        judul = Label(root, text="Menentukan Ukuran Dan Warna").place(x=70, y=200)
        x1 = Label(root, text="‣ Ukuran X-1").place(x=20, y=240)
        e_x1 = Entry(root, width=10).place(x=20, y=265)
        
        x2 = Label(root, text="‣ Ukuran X-2").place(x=200, y=240)
        e_x2 = Entry(root, width=10).place(x=200, y=265)
        
        y1 = Label(root, text="‣ Ukuran Y-1").place(x=20, y=305)
        e_y1 = Entry(root, width=10).place(x=20, y=330)
        
        y2 = Label(root, text="‣ Ukuran Y-2").place(x=200, y=305)
        e_y2 = Entry(root, width=10).place(x=200, y=330)
        
        btn_process = Button(root, text='PROCESS').place(x=200, y=400)

        
        
        self.parent.destroy()
        root.mainloop()

    def onKlikCircle(self, event=None):
        messagebox.showinfo('Informasi', 'create circle', parent=self.parent)
    
    def onKlikTriangle(self, event=None):
        root = Tk()
        root.geometry('350x500')
        root.title('::COBA PROSES BAR::')
        
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
        
        # self.parent.destroy()
        root.mainloop()
    
    def onKlikPentagon(self, event=None):
        pass
    
    def onKlikHexagon(self, event=None):
        pass
    
    def kembali(self):
        self.parent.destroy()
        # if messagebox.askyesno('Kembali', 'Yakin ingin kembali?', parent=self.parent):
        #     self.parent.destroy()
        root = Tk()
        app = FirstPage(root, 'Halaman Pertama')
        root.mainloop()

# call main function
if __name__ == '__main__':
    root = Tk()
    # app = FirstPage(root, ':: First Page ::')
    app = SecondPage(root)
    root.resizable(0, 0) # resizeable 0 maka tidak dapat di resize kembali (FIX)
    root.mainloop()