import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

main = tk.Tk()
main.title("Main Window")
main.attributes('-fullscreen', True)

"""Funktsioon, millega loome uue ekraani, kui vajutada, et soovid muuta SemuBoti näoilmet"""
def Open_ChangeFace():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, kuidas mida soovid näo juures muuta").pack(pady=20)
    
    """Nupp, millega saab hakata valima näoilmeid tervikuna"""
    face_full = Button(new_window, text="Terve näoilme", command=Open_ChangeFullFace)
    face_full.place(x=20, y=50, width=150, height=150)

    "Nupp, millega saab valida silmi"
    eyes = Button(new_window, text="Silmad", command=Open_ChangeEyes)
    eyes.place(x=190, y=50, width=150, height=150)

    "Nupp, millega saab valida kulme"
    brows = Button(new_window, text="Kulmud", command=Open_ChangeBrows)
    brows.place(x=360, y=50, width=150, height=150)

    "Nupp, millega saab valida nina"
    nose = Button(new_window, text="Nina", command=Open_ChangeNose)
    nose.place(x=530, y=50, width=150, height=150)

    "Nupp, millega saab valida suud"
    mouth = Button(new_window, text="Suu", command=Open_ChangeMouth)
    mouth.place(x=700, y=50, width=150, height=150)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back = Button(new_window, text="Tagasi", command=new_window.destroy)
    back.place(x=20, y=20, width=75, height=20)



"""Funktsioon, millega saab avada valiku tervikutest näoilmetest"""
def Open_ChangeFullFace():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv näoilme").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back_f = Button(new_window, text="Tagasi", command=new_window.destroy)
    back_f.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest silmadest"""
def Open_ChangeEyes():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobivad silmad").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back_e = Button(new_window, text="Tagasi", command=new_window.destroy)
    back_e.place(x=20, y=20, width=75, height=20)

    photo_e1 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_1.PNG")
    photo_e1 = photo_e1.resize((100,100))
    photoimage_e1 = ImageTk.PhotoImage(photo_e1)
    new_window.photoimage_e1 = photoimage_e1
    eyes_1 = Button(new_window, image=photoimage_e1, compound=TOP)
    eyes_1.place(x=20, y=50, width=150, height=150)

    photo_e2 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_2.PNG")
    photo_e2 = photo_e2.resize((100,100))
    photoimage_e2 = ImageTk.PhotoImage(photo_e2)
    new_window.photoimage_e2 = photoimage_e2
    eyes_2 = Button(new_window, image=photoimage_e2, compound=TOP)
    eyes_2.place(x=190, y=50, width=150, height=150)

    photo_e3 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_3.PNG")
    photo_e3 = photo_e3.resize((100,100))
    photoimage_e3 = ImageTk.PhotoImage(photo_e3)
    new_window.photoimage_e3 = photoimage_e3
    eyes_3 = Button(new_window, image=photoimage_e3, compound=TOP)
    eyes_3.place(x=360, y=50, width=150, height=150)

    photo_e4 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_4.PNG")
    photo_e4 = photo_e4.resize((100,100))
    photoimage_e4 = ImageTk.PhotoImage(photo_e4)
    new_window.photoimage_e4 = photoimage_e4
    eyes_4 = Button(new_window, image=photoimage_e4, compound=TOP)
    eyes_4.place(x=530, y=50, width=150, height=150)

    photo_e5 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_5.PNG")
    photo_e5 = photo_e5.resize((100,100))
    photoimage_e5 = ImageTk.PhotoImage(photo_e5)
    new_window.photoimage_e5 = photoimage_e5
    eyes_5 = Button(new_window, image=photoimage_e5, compound=TOP)
    eyes_5.place(x=700, y=50, width=150, height=150)

    photo_e6 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_6.PNG")
    photo_e6 = photo_e6.resize((100,100))
    photoimage_e6 = ImageTk.PhotoImage(photo_e6)
    new_window.photoimage_e6 = photoimage_e6
    eyes_6 = Button(new_window, image=photoimage_e6, compound=TOP)
    eyes_6.place(x=870, y=50, width=150, height=150)

    photo_e7 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_7.PNG")
    photo_e7 = photo_e7.resize((100,100))
    photoimage_e7 = ImageTk.PhotoImage(photo_e7)
    new_window.photoimage_e7 = photoimage_e7
    eyes_7 = Button(new_window, image=photoimage_e7, compound=TOP)
    eyes_7.place(x=1040, y=50, width=150, height=150)

    photo_e8 = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Naoilmed\Silmad_8.PNG")
    photo_e8 = photo_e8.resize((100,100))
    photoimage_e8 = ImageTk.PhotoImage(photo_e8)
    new_window.photoimage_e8 = photoimage_e8
    eyes_8 = Button(new_window, image=photoimage_e8, compound=TOP)
    eyes_8.place(x=20, y=220, width=150, height=150)


"""Funktsioon, millega saab avada valiku erinevatest kulmudest"""
def Open_ChangeBrows():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobivad kulmud").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back_b = Button(new_window, text="Tagasi", command=new_window.destroy)
    back_b.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest ninadest"""
def Open_ChangeNose():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv nina").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back_n = Button(new_window, text="Tagasi", command=new_window.destroy)
    back_n.place(x=20, y=20, width=75, height=20)


"""Funktsioon, millega saab avada valiku erinevatest suudest"""
def Open_ChangeMouth():
    new_window = Toplevel(main)
    new_window.title("New Window")
    new_window.attributes('-fullscreen', True) 
    Label(new_window, text="Vali, sobiv suu").pack(pady=20)

    "Nupp, millega saab minna tagasi eelmisele lehele"
    back_m = Button(new_window, text="Tagasi", command=new_window.destroy)
    back_m.place(x=20, y=20, width=75, height=20)



Label(main, text='Mida soovid teha?').pack(pady=10)
"""Nupp, millega avatakse uus akend, kus saab hakata näoilmeid valima"""
SB_face = Button(main, text="SemuBoti näoilmed", command=Open_ChangeFace)
SB_face.place(x=20, y=50, width=150, height=150)
main.mainloop()