from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open(r"C:\Users\helen\Desktop\Bakalaureusetoo\Näoilmed\Silmad_1.PNG")
img = img.resize((100,100))

photo = ImageTk.PhotoImage(img)

btn = Button(root, text="Click Me!", image=photo, compound=TOP)
btn.image = photo
btn.pack()

root.mainloop()