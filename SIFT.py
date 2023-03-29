import tkinter
from tkinter import *
from tkinter import ttk
import cv2
import tkinter.filedialog as fd
from PIL import Image, ImageTk

images = {}


def choose_file():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    images['filename'] = filename
    image = Image.open(images['filename'])
    resize_image = image.resize((540, 360))
    img = ImageTk.PhotoImage(resize_image)
    images['image'] = img

    label = Label(frame1, image=images['image'])
    label.pack()


def save_file():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    save_path = fd.asksaveasfilename(title="Сохранить", initialdir="/",
                                     filetypes=filetypes, defaultextension=".jpeg")
    images['save_path'] = save_path
    cv2.imwrite(images['save_path'], images['sift_image'])


def sift():
    # reading the image
    img = cv2.imread(images['filename'])
    # convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # create SIFT feature extractor
    sift = cv2.xfeatures2d.SIFT_create()
    # detect features from the image
    keypoints, descriptors = sift.detectAndCompute(img, None)
    # draw the detected key points
    sift_image = cv2.drawKeypoints(gray, keypoints, img)
    images['sift_image'] = sift_image
    # show the image
    cv2.imshow('image', sift_image)
    # save the image
    cv2.imwrite("table-sift.jpg", sift_image)


window = Tk()
window.title("SIFT")
window.geometry("1080x720")
frame1 = tkinter.Frame(master=window)
frame1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
frame2 = tkinter.Frame(master=window, width=93)
frame2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)
open_button = tkinter.Button(frame1, text='Выбрать файл', command=choose_file)
open_button.place(anchor=NW)
window.mainloop()
