from tkinter import *
import tkinter as tk

import pymysql
from tkinter import messagebox, ttk,Tk,Canvas
from tkinter.messagebox import askquestion

from PIL import ImageTk
from self import self

import elogin
import login


class MyLogin:
    def __init__(self ):
        self.root = Tk()
        self.root.title(" Welcome")
        width = 550
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.label_0 = Label(self.root, text="User Type", width=10, font=("bold", 50))
        self.label_0.place(x=90, y=120)
        self.btn1=Button(self.root,text="ADMIN",command=login.MyLogin,width="10",background="light yellow",).place(x=275,y=350)
        self.btn2 = Button(self.root, text="EMPLOYEE",command=elogin.MyLogin1 ,width="10", background="light yellow").place(x=185,y=350)

        self.root.mainloop()










