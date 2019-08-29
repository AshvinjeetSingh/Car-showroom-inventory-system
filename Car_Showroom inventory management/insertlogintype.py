
from tkinter import *
import tkinter as tk

import pymysql
from tkinter import messagebox, ttk,Tk,Canvas
from tkinter.messagebox import askquestion

from PIL import ImageTk







class Add_Category:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Add Login Type")
        width = 400
        height = 200
        screen_width = self.my_frame.winfo_screenwidth()
        screen_height = self.my_frame.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.my_frame.geometry("%dx%d+%d+%d" % (width, height, x, y))




        self.imagelb1=Label(self.my_frame,text="Add Ctegory",font=("georgia",50,"bold"))
        self.lb1 = Label(self.my_frame, text="Category")




        self.ment=StringVar()
        self.t1 = Entry(self.my_frame, width=20,textvariable=self.ment)




        self.t1.focus()








        self.btn1 = Button(self.my_frame, text="Save", padx=10, command=self.savedata, width=30)

        self.lb1.place(x=50, y=70)
        self.t1.place(x=150, y=70)






        self.btn1.place(x=100, y=100)

#btn2.place(x=170, y=500)


        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\costum.png')
        self.imagelabel2 = Label(self.my_frame, image=self.myimage1)
        self.imagelabel2.place(x=650,y=190)
        self.imagelb1.place(x=610,y=50)

        self.my_frame.mainloop()
    def savedata(self):


        try:
            myobj=pymysql.connect(host="localhost", user="root",
                              password="", db="automobile")

            with myobj.cursor() as myconn:


                myconn.execute("insert into "
                           "logmain(logintype) "
                           "values(%s)",

                     (self.t1.get()))

                if (self.t1.get() == "") :
                    messagebox.showerror("fill box", "complete the entries", parent=self.my_frame)
                #
                #
                else:

                    myobj.commit()
                    myobj.close()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)

