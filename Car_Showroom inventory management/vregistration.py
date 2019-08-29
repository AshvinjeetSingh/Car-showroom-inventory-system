import time
from tkinter import *
import tkinter as tk

import pymysql
from tkinter import messagebox, ttk,Tk,Canvas
from tkinter.messagebox import askquestion

from PIL import ImageTk
from self import self
from PIL import ImageTk
from PIL import Image
from tkinter.filedialog import askopenfilename


class Myvregistration:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Vechile Registration")
        self.my_frame.geometry('1366x768')
        # self.my_frame.config(background="white")




        self.lb2 = Label(self.my_frame, text="Costumer ID")
        self.lb1 = Label(self.my_frame, text="Vehicle Number")
        self.lb3 = Label(self.my_frame, text="Vehicle Date Of Registeration")
        self.lb4 = Label(self.my_frame, text="Date Of Registeration Valid Upto:")
        self.lb5 = Label(self.my_frame, text="Vehicle Capacity")
        self.lb6 = Label(self.my_frame, text="Vehicle FuelType")
        self.lb7 = Label(self.my_frame, text="Vehicle Company Name")
        self.lb8 = Label(self.my_frame, text="Vehicle Name")
        self.lb9 = Label(self.my_frame, text="Vehicle Type")


        self.t2 = Entry(self.my_frame, width=40)

        self.t1 = Entry(self.my_frame,width=40 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)
        self.t5 = Entry(self.my_frame, width=40)
        self.t7 = Entry(self.my_frame, width=40)
        self.t8 = Entry(self.my_frame, width=40)


        self.t1.focus()





        self.list=["Petrol","Diesel","Others"]
        self.list1=["Scooter Gearless","Scooter With Gear","Motorcycle","Car"]
        self.vechiletype = ttk.Combobox(self.my_frame)
        self.vechiletype.config(values=self.list1, state="readonly")
        self.vechiletype.set("Choose VechileType")
        self.lb9.place(x=50,y=350)
        self.vechiletype.place(x=220, y=350)


        self.fueltype = ttk.Combobox(self.my_frame)
        self.fueltype.config(values=self.list,state="readonly")
        self.fueltype.set("Choose FuelType")
        self.lb6.place(x=50,y=310)
        self.fueltype.place(x=220, y=310)



        self.btn1 = Button(self.my_frame, text="Save", padx=10, command=self.savedata, width=90,font=("georgia",15,"bold"))
        self.btn1.config(background="lightyellow")
        self.saveicon = PhotoImage(file="save.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.btn1.config(image=self.saveiconsmall, compound=RIGHT)


        self.lb4.place(x=50, y=150)
        self.t4.place(x=220, y=150)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=110)
        self.t3.place(x=220, y=110)
        self.lb5.place(x=50, y=190)
        self.t5.place(x=220, y=190)
        self.lb7.place(x=50, y=230)
        self.t7.place(x=220, y=230)
        self.lb8.place(x=50, y=270)
        self.t8.place(x=220, y=270)
        self.imageuploadbtn = Button(self.my_frame, text="Upload Photo", width=8,height=2,padx=20, background="light yellow",font=("georgia", 8, "bold"),
                                     command=self.imageupload).place(x=320,y=420)
        self.imglabel = Label(self.my_frame, borderwidth=1, text="", width=200, height=200)
        self.imglabel.place(x=950, y=150)



        self.btn1.place(x=170, y=420)






        self.my_frame.mainloop()


    def fetchdata(self):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from costumertable where cid=%s"
                try:
                    myconnectionobj.execute(query, (int(self.t1.get())))
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        answer = askquestion("Are you sure", "Do you really want to continue?", icon="warning",
                                             parent=self.my_frame)
                        if answer == "yes":
                            pass

                    else:
                        messagebox.showerror("WRONG INPUT","Costumer Vechile No. Incorrect",parent=self.my_frame)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)
        except Exception as ex:

            messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)


    def savedata(self,):
        try:
            myobj=pymysql.connect(host="localhost", user="root",
                              password="", db="automobile")

            with myobj.cursor() as myconn:


                myconn.execute("insert into "
                           "vechiletable(vvechileno,vcompanyname,vcar,vvechiletype,vdate,vdateupto,vfuel,vcapacity,cnames) "
                           "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                     (self.t1.get(),self.t7.get(),self.t8.get(),self.vechiletype.get(), self.t3.get(), self.t4.get(),
                      self.fueltype.get(),self.t5.get(),self.t2.get()))



                myobj.commit()
                myobj.close()
                messagebox.showinfo("Success", "Record Saved Successfully",parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)

    def checkdata(self ):
        try:
            myobj = pymysql.connect(host="localhost", user="root",
                                    password="", db="automobile")

            with myobj.cursor() as myconn:
                myconn.execute("insert into "
                               "vechiletable(vvechileno,vcompanyname,vcar,vvechiletype,vdate,vdateupto,vfuel,vcapacity,cnames) "
                               "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                               (self.t1.get(),self.t7.get(),self.t8.get(),self.vechiletype.get() ,self.t3.get(), self.t4.get(),
                                self.t5.get(), self.fueltype.get(), self.t2.get()))


        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex), parent=self.my_frame)

    def imageupload(self):
        self.filename = askopenfilename(
            filetypes=[(("Picture Files",
                         "*.jpg;*.png;*.gif"))],parent=self.my_frame)  # show an "Open" dialog box and return the path to the selected file
        img = Image.open(self.filename)
        self.finalname = str(int(time.time()))
        img.save("vechileimages//" + self.finalname + ".jpg")
        tkimage = ImageTk.PhotoImage(img)
        self.imglabel.configure(image=tkimage)
        self.imglabel.image = tkimage