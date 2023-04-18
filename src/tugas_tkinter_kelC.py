import tkinter as tk

root = tk.Tk()
root.geometry("852x480")
root.title("Aplikasi Kelompok C")

Frame = tk.Frame(root, bg = 'white')
Frame.place(relwidth =1, relheight =1)

#======================================================LABEL=============================================================
#Label judul
label1 = tk.Label(Frame, text="Selamat Datang di Aplikasi Kelompok C", font=("Helvencia 20 bold"), fg='blue', bg='white')
label1.pack()

line = tk.Canvas(Frame, width=530, height=2, bg='blue')
line.pack()
canvas_height=20
canvas_width=530
y = int(canvas_height/2)
line.create_line(0, y, canvas_width, y)

#label sub judul
label2 = tk.Label(Frame, text="Program Menggambar Objek 2D", font=("Helvencia 20"), height=3, fg='blue', bg='white')
label2.pack()

#=====================================================BUTTON=============================================================

#penengah bagian kiri
label_p = tk.Label(Frame, width=17, height=2, bg='white')
label_p.pack(side='left')

#button start
start_button = tk.Button(Frame, text="Start", font=("Helvencia 12 bold"), width=20, height=2, fg='blue', bg='#D9D9D9')
start_button.pack(side='left')

#penengah bagian kanan
label_p1 = tk.Label(Frame, width=17, height=2, fg='blue', bg='white')
label_p1.pack(side='right')

#button bujur sangkar
Exit_button = tk.Button(Frame, text="Exit", font=("Helvencia 12 bold"), width=20, height=2, fg='blue', bg='#D9D9D9')
Exit_button.pack(side='right')

root.mainloop()