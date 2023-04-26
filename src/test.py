from tkinter import *

class MyWindow:
    # constructor dari class dan akan dijalankan saat objek dari class dibuat
    def __init__(self, master):
        self.master = master
        master.title("My Window")

        # membuat widget Entry dan menempatkannya di jendela tkinter
        self.entry1 = Entry(master)
        self.entry1.pack()

        self.entry2 = Entry(master)
        self.entry2.pack()

        self.entry3 = Entry(master)
        self.entry3.pack()

        # membuat variabel untuk menyimpan nilai dari setiap Entry
        self.var1 = StringVar()
        self.int1 = IntVar()
        self.int2 = IntVar()

        # menghubungkan variabel dengan masing-masing widget Entry
        self.entry1.config(textvariable=self.var1)
        self.entry2.config(textvariable=self.int1)
        self.entry3.config(textvariable=self.int2)

        # mengambil nilai dari setiap Entry dan menampilkannya
        def get_entry_values():
            value1 = self.var1.get()
            value2 = self.int1.get()
            value3 = self.int2.get()
            print(value1, value2, value3)

        self.button = Button(master, text="Get Entry Values", command=get_entry_values)
        self.button.pack()

root = Tk()
my_window = MyWindow(root)
root.mainloop()
