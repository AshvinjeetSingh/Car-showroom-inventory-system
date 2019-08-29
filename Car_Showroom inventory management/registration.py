
from tkinter import *
import tkinter as tk

import pymysql
from tkinter import messagebox, ttk,Tk,Canvas
from tkinter.messagebox import askquestion

from PIL import ImageTk







class Myregistration:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Registration")
        self.my_frame.geometry('1366x768')




        self.imagelb1=Label(self.my_frame,text="Customer Login",font=("georgia",50,"bold"))
        self.lb1 = Label(self.my_frame, text="Customer ID")
        self.lb2 = Label(self.my_frame, text="Customer Name")
        self.lb3 = Label(self.my_frame, text="Customer Address")
        self.lb4 = Label(self.my_frame, text="Customer City")

        self.lb6 = Label(self.my_frame, text="Customer Phone Number")


        self.lb8 = Label(self.my_frame, text="Gender")


        self.ment=StringVar()
        self.t1 = Entry(self.my_frame, width=40,textvariable=self.ment)

        self.t2 = Entry(self.my_frame,width=40 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)

        self.t6 = Entry(self.my_frame, width=40)


        self.t1.focus()





        self.list=["Male","Female","Others"]



        self.gender = ttk.Combobox(self.my_frame)
        self.gender.config(values=self.list,state="readonly")
        self.gender.set("Choose gender")
        self.gender.place(x=220, y=220)



        self.btn1 = Button(self.my_frame, text="Save", padx=10, command=self.savedata, width=160,font=("georgia",15,"bold"))
        self.btn1.config(background="lightyellow")
        self.saveicon = PhotoImage(file="save.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.btn1.config(image=self.saveiconsmall,compound=RIGHT)
#btn2 = Button(my_frame, text="Delete", padx=10, command=deletedata, width=30)

        self.lb4.place(x=50, y=140)
        self.t4.place(x=220, y=140)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=100)
        self.t3.place(x=220, y=100)

        self.lb6.place(x=50, y=180)
        self.t6.place(x=220, y=180)
        self.lb8.place(x=50, y=220)





        self.btn1.place(x=170, y=350)

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
                           "costumertable(cid,cname,cadress, ccity,cgender,cphone) "
                           "values(%s,%s,%s,%s,%s,%s)",

                     (self.t1.get(), self.t2.get(), self.t3.get(),
                      self.t4.get(),self.gender.get(),self.t6.get()))

                if (self.t1.get() == "") or (self.t2.get() == "") or (self.t3.get() == "") or (self.t4.get() == "") or (self.gender.get() == "") or (self.t6.get() == "") :
                    messagebox.showerror("fill box", "complete the entries", parent=self.my_frame)
                #
                #
                else:

                    myobj.commit()
                    myobj.close()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)

