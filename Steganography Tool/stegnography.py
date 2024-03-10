from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

current_directory = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title("Stego - Hide Secret Message")
root.geometry("705x580+150+185")
root.resizable(False, False)
root.configure(bg="#394240")  # Updated background color


def showimage():
    global filename
    print("")
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetype=(("PNG File", "*.png"), ("JPG FIle", "*.jpg"), ("All Files", "*.txt")),
    )

    img = Image.open(filename)
    img = img.resize((335, 275))  # Resize the image to fit the frame1
    img_tk = ImageTk.PhotoImage(img)
    lbl.img_tk = img_tk
    lbl.configure(image=img_tk, width=340, height=280)


def hidedata():
    global secret
    print("")
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
 

def showdata():
    print("")
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def saveimage():
    hidden_filename = "hidden.png"
    hidden_path = os.path.join(current_directory, hidden_filename)
    secret.save("hidden.png")

# Main icon
icon_path = os.path.join(current_directory, "hacker.png")
image_icon = PhotoImage(file=icon_path)
root.iconphoto(False, image_icon)

# Logo
image_icon = image_icon.subsample(5)
Label(root, image=image_icon, bg="#394240").place(x=10, y=10)

Label(
    root,
    text="Hide Your Secret Message",
    bg="#394240",
    fg="#F2EFEF",
    font="arial 25 bold",
).place(x=130, y=60)

# First frame
f = Frame(root, bg="#4F5B66", width=340, height=280, relief=GROOVE)
f.place(x=10, y=140)

lbl = Label(f, bg="#4F5B66", fg="#F2EFEF")
lbl.place(x=2, y=2)

# Second frame
frame2 = Frame(root, bd=3, bg="#4F5B66", width=340, height=280, relief=GROOVE)
frame2.place(x=355, y=140)

text1 = Text(
    frame2, font="Roboto 20", bg="#F2EFEF", fg="#394240", relief=GROOVE, wrap=WORD
)
text1.place(x=0, y=0, width=330, height=280)

Scrollbar_1 = Scrollbar(frame2)
Scrollbar_1.place(x=320, y=0, height=278)

Scrollbar_1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar_1.set)

# Third frame
frame3 = Frame(root, bd=3, bg="#394240", width=340, height=105, relief=GROOVE)
frame3.place(x=10, y=430)

# Buttons in frame3
Button(
    frame3,
    text="Open Image",
    width=12,
    height=2,
    font="arial 14 bold",
    bg="#5E7F5E",
    fg="#F2EFEF",
    command=showimage,
).place(x=10, y=26)

Button(
    frame3,
    text="Save Image",
    width=12,
    height=2,
    font="arial 14 bold",
    bg="#5E7F5E",
    fg="#F2EFEF",
    command=saveimage,
).place(x=170, y=26)

Label(frame3, text="Picture, Image, Photo File", bg="#394240", fg="#F2EFEF").place(
    x=10, y=3
)

# Fourth frame
frame4 = Frame(root, bd=3, bg="#394240", width=340, height=105, relief=GROOVE)
frame4.place(x=355, y=430)

# Buttons in frame4
Button(
    frame4,
    text="Hide Data",
    width=12,
    height=2,
    font="arial 14 bold",
    bg="#5E7F5E",
    fg="#F2EFEF",
    command=hidedata,
).place(x=10, y=26)

Button(
    frame4,
    text="Show Data",
    width=12,
    height=2,
    font="arial 14 bold",
    bg="#5E7F5E",
    fg="#F2EFEF",
    command=showdata,
).place(x=170, y=26)

Label(frame4, text="Picture, Image, Photo File", bg="#394240", fg="#F2EFEF").place(
    x=10, y=3
)

root.mainloop()

