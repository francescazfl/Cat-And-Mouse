# add a new window about the project unter the file tab

from tkinter import *
from PIL import Image, ImageTk

def newwindow():

    filename = "mouse-and-cat.jpg"
    im = Image.open(filename)
    im = im.resize((200, 250), Image.ANTIALIAS)

    tk2 = Toplevel()
    windowname = 'About the Turtle Arena'
    tk2.title(windowname)
    caption = Label(tk2,text="FZL's Fun Proj: A Cat-And-Mouse Game!").pack(side=TOP)
    img = ImageTk.PhotoImage(im)  # <--- results of PhotoImage() must be stored
    # img = PhotoImage(im)  # <--- results of PhotoImage() must be stored

    image_label = Label(image=img) # <--- will not work if 'image = ImageTk.PhotoImage(im)'
    image_label.image = img

    ok = Button(tk2, text='OK', command=tk2.destroy).pack(side=BOTTOM)
    canvas = Canvas(tk2,width=600, height=400)
    canvas.create_text(300,10,text="Click 'run' to start a default case. More clicks on 'run' would accelerate the process.")
    canvas.create_text(184,30,text="The 'step' button moves the game step by step.")
    canvas.create_text(278,50,text="Hit the 'stop' button and then you can drag and move around the orange cat!")
    canvas.create_text(276,70,text="Feel free to hit 'reset' if you are not satisfied with how the cat is performing.")
    canvas.create_text(183,90,text="Double click 'quit' when you are ready to leave.")
    canvas.create_text(109,110,text="Good luck and have fun!")
    canvas.create_text(300,390,font ="Times 8 italic", text="The image comes from online open source.")
    canvas.pack()
    canvas.create_image((300, 250), image = img, state = "normal")


    tk2.mainloop()


if __name__ == '__main__':
    newwindow()
