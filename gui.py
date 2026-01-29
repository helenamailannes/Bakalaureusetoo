import tkinter as tk
from tkinter import *

main = tk.Tk()
main.title("Main Window")
main.attributes('-fullscreen', True)

"""Funktsioon, millega loome uue ekraani, kui vajutada, et soovid muuta SemuBoti näoilmet"""
def open_change_face():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, kuidas mida soovid näo juures muuta").pack(pady=20)
    
    """Nupp, millega saab hakata valima näoilmeid tervikuna"""
    face_full = Button(new_window, text="Terve näoilme", command=open_face_full)
    face_full.place(x=20, y=50, width=150, height=150)

    "Nupp, millega saab valida silmi"
    face_full = Button(new_window, text="Silmad", command=open_eyes)
    face_full.place(x=190, y=50, width=150, height=150)

    "Nupp, millega saab valida kulme"
    face_full = Button(new_window, text="Kulmud", command=open_brows)
    face_full.place(x=360, y=50, width=150, height=150)

    "Nupp, millega saab valida nina"
    face_full = Button(new_window, text="Nina", command=open_nose)
    face_full.place(x=530, y=50, width=150, height=150)

    "Nupp, millega saab valida suud"
    face_full = Button(new_window, text="Suu", command=open_mouth)
    face_full.place(x=700, y=50, width=150, height=150)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)



"""Funktsioon, millega saab avada valiku tervikutest näoilmetest"""
def open_face_full():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv näoilme").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest silmadest"""
def open_eyes():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobivad silmad").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest kulmudest"""
def open_brows():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobivad kulmud").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest ninadest"""
def open_nose():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv nina").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest suudest"""
def open_mouth():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv suu").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    face_full = Button(new_window, text="Tagasi", command=new_window.destroy)
    face_full.place(x=20, y=20, width=75, height=20)



Label(main, text='Mida soovid teha?').pack(pady=10)
"""Nupp, millega avatakse uus akend, kus saab hakata näoilmeid valima"""
SB_face = Button(main, text="SemuBoti näoilmed", command=open_change_face)
SB_face.place(x=20, y=50, width=150, height=150)
main.mainloop()