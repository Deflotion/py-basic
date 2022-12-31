
#? GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#$ Init
window = tk.Tk()
window.configure(bg="white")
window.resizable(False,False)
window.geometry("300x200")
window.title("Turu gan awikwok")

#$ Variable dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    #cat Fungsi ini akan dipanggil oleh tombol
    pesan = f"Halo, {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Hasil",message=pesan)

#$ Frame input
input_frame = ttk.Frame(window)

#* penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#* komponen-komponen
#& 1. Label nama depan
nama_label_depan = ttk.Label(input_frame,text="Nama Depan: ")
nama_label_depan.pack(padx=10,fill="x",expand=True)

#& 2. Entri nama depan
nama_label_entry = ttk.Entry(input_frame,textvariable= NAMA_DEPAN)
nama_label_entry.pack(padx=10,fill="x",expand=True)

#& 3. Label nama belakang
nama_label_belakang = ttk.Label(input_frame,text="Nama belakang: ")
nama_label_belakang.pack(padx=10,fill="x",expand=True)

#& 4. Entri nama belakang
nama_label_entry = ttk.Entry(input_frame,textvariable= NAMA_BELAKANG)
nama_label_entry.pack(padx=10,fill="x",expand=True)

#& 5. Tombol
tombol_save = ttk.Button(input_frame,text="Save",command=tombol_click)
tombol_save.pack(padx=10,pady=10,fill="x",expand=True)

#$ Main Loop window
window.mainloop()