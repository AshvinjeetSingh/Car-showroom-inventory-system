from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

import self as self
import tkinter as tk




class UpdatevRegistration:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Update Vechile Registration")
        self.my_frame.geometry('1366x768')


        self.lb2 = Label(self.my_frame, text="Costumer ID")
        self.lb1 = Label(self.my_frame, text="Vechile Number")
        self.lb3 = Label(self.my_frame, text="Vechile Date Of Registeration")
        self.lb4 = Label(self.my_frame, text="Date Of Registeration Valid Upto:")
        self.lb5 = Label(self.my_frame, text="Vechile Capacity")
        self.lb6 = Label(self.my_frame, text="Vechile FuelType")
        self.lb7 = Label(self.my_frame, text="Vechile Company Name")
        self.lb8 = Label(self.my_frame, text="Vechile Name")
        self.lb9 = Label(self.my_frame, text="Vechile Type")


        self.t2 = Entry(self.my_frame, width=40)

        self.t1 = Entry(self.my_frame,width=20 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)
        self.t5 = Entry(self.my_frame, width=40)
        self.t7 = Entry(self.my_frame, width=40)
        self.t8 = Entry(self.my_frame, width=40)

        self.t2.focus()





        self.list=["Petrol","Diesel","Others"]



        self.fueltype = ttk.Combobox(self.my_frame)
        self.fueltype.config(values=self.list,state="readonly")
        self.fueltype.set("Choose FuelType")
        self.lb6.place(x=50,y=310)
        self.fueltype.place(x=220, y=310)

        self.list1 = ["Scooter Gearless", "Scooter With Gear", "Motorcycle", "Car"]
        self.vechiletype = ttk.Combobox(self.my_frame)
        self.vechiletype.config(values=self.list1, state="readonly")
        self.vechiletype.set("Choose VechileType")
        self.lb9.place(x=50, y=350)
        self.vechiletype.place(x=220, y=350)

        self.btn1 = Button(self.my_frame, padx=10, command=self.fetchdata, width=30)
        self.saveicon = PhotoImage(file="magnifier.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.btn1.config(image=self.saveiconsmall, compound=LEFT)
        self.btn2 = Button(self.my_frame, text="Update", padx=10, command=self.updatedata, width=90,font=("georgia",15,"bold"))
        self.saveicon2 = PhotoImage(file="exchange.png")
        self.saveiconsmall2 = self.saveicon2.subsample(1, 1)
        self.btn2.config(background="lightyellow",image=self.saveiconsmall2, compound=LEFT)
        self.btn3 = Button(self.my_frame, text="Delete", padx=10, command=self.deletedata, width=90,font=("georgia",15,"bold"))
        self.saveicon1 = PhotoImage(file="rubbish.png")
        self.saveiconsmall1 = self.saveicon1.subsample(1, 1)
        self.btn3.config(background="lightyellow",image=self.saveiconsmall1, compound=LEFT)

        self.lb4.place(x=50, y=140)
        self.t4.place(x=220, y=140)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=100)
        self.t3.place(x=220, y=100)
        self.lb5.place(x=50, y=190)
        self.t5.place(x=220, y=190)
        self.lb7.place(x=50, y=230)
        self.t7.place(x=220, y=230)
        self.lb8.place(x=50, y=270)
        self.t8.place(x=220, y=270)



        self.btn1.place(x=490, y=60)

        self.btn2.place(x=220, y=390)
        self.btn3.place(x=350, y=390)


        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\rr.png')
        self.imagelabel2 = Label(self.my_frame, image=self.myimage1)
        self.imagelabel2.place(x=550,y=100)

        self.my_frame.mainloop()

    def fetchdata(self):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from vechiletable where cnames=%s"
                try:
                    myconnectionobj.execute(query, (int(self.t2.get())))
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.t1.delete(0, END)
                        self.t1.insert(0, str(result[0]))
                        self.t3.delete(0, END)
                        self.t3.insert(0, str(result[3]))
                        self.t4.delete(0, END)
                        self.t4.insert(0, str(result[4]))
                        self.t5.delete(0, END)
                        self.t5.insert(0, str(result[7]))
                        self.t7.delete(0, END)
                        self.t7.insert(0, str(result[1]))
                        self.t8.delete(0, END)
                        self.t8.insert(0, str(result[2]))





                        self.vechiletype.set(str(result[6]))
                        self.fueltype.set(str(result[5]))
                    else:
                        messagebox.showerror("WRONG INPUT","Costumer ID Incorrect",parent=self.my_frame)



                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Connection Error1", "Error in Connection due to " + str(ex),parent=self.my_frame)

    def updatedata(self):
        connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')

        try:
            with connectionobj.cursor() as myconnection:
                query = "update vechiletable set vvechileno=%s,vcompanyname=%s ,vcar=%s,vdate=%s, " \
                        "vdateupto=%s, " \
                        "vfuel=%s, vvechiletype=%s,vcapacity=%s where cnames=%s"
                try:
                    myconnection.execute(query, (self.t1.get(),self.t7.get(),self.t8.get(),
                                                 self.t3.get(),self.t4.get(),
                                                 self.fueltype.get(),self.vechiletype.get(),

                                                 self.t5.get(),self.t2.get()))

                    if (self.t1.get() == "") or (self.t2.get() == "") or (self.t3.get() == "") or (
                            self.t4.get() == "") or (self.t5.get() == "") or (self.fueltype.get() == "")or (self.vechiletype.get() == "")or (self.t7.get()=="")or (self.t8.get()=="") :
                        messagebox.showerror("fill box", "complete the entries", parent=self.my_frame)
                    else:
                        connectionobj.commit()
                        messagebox.showinfo("Success", "Product Updated Successfully",parent=self.my_frame)

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.my_frame)

    def deletedata(self):

        answer = askquestion("Are you sure", "Do you really want to delete?", icon="warning",parent=self.my_frame)
        if answer == "yes":

            connectionobj = pymysql.connect(host='localhost', user='root',
                                            password='', db='automobile')

            try:
                with connectionobj.cursor() as myconnection:
                    query = "delete from vechiletable where cnames=%s"
                    try:
                        myconnection.execute(query, (self.t2.get()))
                        connectionobj.commit()

                        messagebox.showinfo("Success", " information Deleted Successfully",parent=self.my_frame)
                        self.t1.delete(0, END)
                        self.t2.delete(0, END)
                        self.t3.delete(0, END)
                        self.t4.delete(0, END)
                        self.t5.delete(0, END)
                        self.t7.delete(0, END)
                        self.t8.delete(0, END)
                        self.fueltype.set("Choose Fuel Type")
                        self.vechiletype.set("Choose Vechile Type")
                    except Exception as ex:
                        messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
            except Exception as ex:
                messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.my_frame)