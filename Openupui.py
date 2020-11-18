import tkinter as tk
import VideoRecognition as VR
import FindBurglar as Burglar
from PIL import Image,ImageTk



from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = '700700.png'
WIDTH, HEIGTH = 500, 500

root = tk.Tk()
root.iconbitmap('UIimageee.ico')

root.title('Select any mode')
root.geometry('{}x{}'.format(WIDTH, HEIGTH))

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)


button1=tk.Button(root, text="Gun Detect mode", bg='gray',fg='red',command=VR.ItgoesOn)
button1win = canvas.create_window(10, 10, anchor=tk.N, window=button1)
button1.place(x=170,y=200)

button2=tk.Button(root, text="Home eye ", bg='gray',fg='red',command=Burglar.DetectBurglar)
button2win=canvas.create_window(10, 10, anchor=tk.N, window=button2)
button2.place(x=170,y=250)







root.mainloop()


