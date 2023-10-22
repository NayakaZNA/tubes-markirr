import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

# Ini jangan diotak-atik rek
import os
khongguan = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./Assets/")
def gambar(indomie: str) -> Path:
    return khongguan + indomie

# dictionary Data Tempat Parkir
tempat_parkir = {
    'motor': {
        'reguler': {
            'space': 20,
            'rate': 5000  # Tarif per hari
        },
        'VIP': {
            'space': 5,
            'rate': 10000  # Tarif per hari
        }
    },
    'mobil': {
        'reguler': {
            'space': 50,
            'rate': 10000  # Tarif per hari
        },
        'VIP': {
            'space': 10,
            'rate': 20000  # Tarif per hari
        }
    }
}

# Inisialisasi Data Tempat Parkir
vehicle_type    = ''

# Konfigurasi Window
window  = tk.Tk()
window.geometry("760x570")
window.resizable(False, False)
window.title("Markirr™")

# Halaman-Halaman
p1          = tk.Frame(window, width=760, height=570)
p2_motor    = tk.Frame(window, width=760, height=570)
p2_mobil    = tk.Frame(window, width=760, height=570)
p3          = tk.Frame(window, width=760, height=570)
p4          = tk.Frame(window, width=760, height=570)

for frame in (p1, p2_mobil, p2_motor, p3, p4):
    frame.grid(row=0, column=0, sticky='news')


# Halaman Utama
p1.configure(bg="#243447")
p1.place(anchor='center', relx=0.5, rely=0.5)

## Header
header_img  = ImageTk.PhotoImage(Image.open(gambar("header.png")))
header_l    = tk.Label(p1, image = header_img)
header_l.place(
    x       = 0,
    y       = -32,
    width   = 760,
    height  = 231
)

## Logo & Slogan
markirrw_img= ImageTk.PhotoImage(Image.open(gambar("markirr-white.png")))
markirrw_l  = tk.Label(p1, image = markirrw_img)
markirrw_l.place(
    x       = 264,
    y       = 42,
    width   = 257,
    height  = 98
)

## Instruksi
text1_img   = ImageTk.PhotoImage(Image.open(gambar("text1.png")))
text1_l     = tk.Label(p1, image = text1_img)
text1_l.place(
    x       = 208,
    y       = 231,
    width   = 343,
    height  = 22
)

## Mobil
mobil_img   = ImageTk.PhotoImage(Image.open(gambar("mobil.png")))
mobil_l     = tk.Button(
    p1, image = mobil_img, 
    command = lambda: [p2_mobil.tkraise(), lambda vehicle_type: ("mobil")])
mobil_l.place(
    x       = 116, 
    y       = 296,
    width   = 199,
    height  = 205
)
mobil_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

print(vehicle_type)

## Motor
motor_img   = ImageTk.PhotoImage(Image.open(gambar("motor.png")))
motor_l     = tk.Button(
    p1, image = motor_img, 
    command = lambda: [p2_motor.tkraise()]
    )
motor_l.place(
    x       = 444, 
    y       = 296,
    width   = 199,
    height  = 197
)
motor_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")


# Halaman 2 (Mobil)
p2_mobil.configure(bg="#243447")
p2_mobil.place(anchor='center', relx=0.5, rely=0.5)

## Tombol Home
home1_img   = ImageTk.PhotoImage(Image.open(gambar("home.png")))
home1_l     = tk.Button(
    p2_mobil, image = home1_img, 
    command = lambda: [p1.tkraise()])
home1_l.place(
    x       = 701,
    y       = 229,
    width   = 89,
    height  = 79
)
home1_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

## Layout Parkir
### Border
border_img  = ImageTk.PhotoImage(Image.open(gambar("parking_border.png")))
border_l    = tk.Label(
    p2_mobil, image = border_img
)
border_l.place(
    x       = 70,
    y       = 85,
    width   = 593,
    height  = 342
)
### Tersedia?
text2_img   = ImageTk.PhotoImage(Image.open(gambar("text2.png")))
text2_l     = tk.Label(
    p2_mobil, image = text2_img
)
text2_l.place(
    x       = 486,
    y       = 404,
    width   = 144,
    height  = 83
)
### Markirr Logo
markirrl_img= ImageTk.PhotoImage(Image.open(gambar("markirr_black.png")))
markirrl_l  = tk.Label(
    p2_mobil, image = markirrl_img
)
markirrl_l.place(
    x       = 26,
    y       = 506,
    width   = 125,
    height  = 42
)

### Button Parkir
{

}

# Halaman 2 (Motor)
p2_motor.configure(bg="#243447")
p2_motor.place(anchor='center', relx=0.5, rely=0.5)

## Tombol Home
home2_img   = ImageTk.PhotoImage(Image.open(gambar("home.png")))
home2_l     = tk.Button(
    p2_motor, image = home2_img,
    command = lambda: [p1.tkraise()])
home2_l.place(
    x       = 701,
    y       = 229,
    width   = 89,
    height  = 79
)
home2_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

# Eksekusi
p1.tkraise()
window.mainloop()
