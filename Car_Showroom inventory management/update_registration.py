from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

import self as self
import tkinter as tk




class UpdateRegistration:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Update Registration")
        self.my_frame.geometry('1366x768')


        self.lb1 = Label(self.my_frame, text="Customer ID")
        self.lb2 = Label(self.my_frame, text="Customer Name")
        self.lb3 = Label(self.my_frame, text="Customer Address")
        self.lb4 = Label(self.my_frame, text="Customer City")

        self.lb6 = Label(self.my_frame, text="Customer Phone Number")


        self.lb8 = Label(self.my_frame, text="Gender")



        self.t1 = Entry(self.my_frame,width=40)
        self.t2 = Entry(self.my_frame,width=40 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)

        self.t6 = Entry(self.my_frame, width=40)




        self.list=["Male","Female","Others"]



        self.gender = ttk.Combobox(self.my_frame)
        self.gender.config(values=self.list,state="readonly")
        self.gender.set("Choose gender")
        self.gender.place(x=220, y=230)



        self.btn1 = Button(self.my_frame, text="UPDATE", padx=10, command=self.updatedata, width=90,font="georgia")
        self.saveicon2 = PhotoImage(file="exchange.png")
        self.saveiconsmall2 = self.saveicon2.subsample(1, 1)

        self.btn1.config(image=self.saveiconsmall2, compound=LEFT)

        self.saveicon = PhotoImage(file="magnifier.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.btn2 = Button(self.my_frame, padx=10, command=self.fetchdata, width=25,font="georgia")
        self.btn2.config(image=self.saveiconsmall,compound=LEFT)
        # self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\be.png')
        # self.btn2.config(image=self.myimage1)
        self.btn3 = Button(self.my_frame, text="DELETE", padx=10, command=self.deletedata, width=90,font="georgia")
        self.saveicon1 = PhotoImage(file="rubbish.png")
        self.saveiconsmall1 = self.saveicon1.subsample(1, 1)

        self.btn3.config(image=self.saveiconsmall1, compound=LEFT)

        self.lb4.place(x=50, y=150)
        self.t4.place(x=220, y=150)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=110)
        self.t3.place(x=220, y=110)

        self.lb6.place(x=50, y=190)
        self.t6.place(x=220, y=190)

        self.lb8.place(x=50, y=230)





        self.btn1.place(x=150, y=330)
        self.btn2.place(x=490, y=20)
        self.btn3.place(x=290, y=330)
        self.btn1.config(background="lightyellow")
        self.btn2.config(background="lightyellow")
        self.btn3.config(background="lightyellow")

        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\costum.png')
        self.imagelabel2 = Label(self.my_frame, image=self.myimage1)
        self.imagelabel2.place(x=750, y=100)
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
                        self.t2.delete(0, END)
                        self.t2.insert(0, str(result[1]))
                        self.t3.delete(0, END)
                        self.t3.insert(0, str(result[2]))
                        self.t4.delete(0, END)
                        self.t4.insert(0, str(result[4]))

                        self.t6.delete(0, END)
                        self.t6.insert(0, str(result[5]))




                        self.gender.set(str(result[3]))
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
                query = "update costumertable set cname=%s, " \
                        "cadress=%s, " \
                        "cgender=%s, ccity=%s,cphone=%s where cid=%s"
                try:
                    myconnection.execute(query, (self.t2.get(),
                                                 self.t3.get(),
                                                 self.gender.get(),
                                                 self.t4.get(),

                                                 self.t6.get(),self.t1.get()))

                    if (self.t1.get() == "") or (self.t2.get() == "") or (self.t3.get() == "") or (
                            self.t4.get() == "") or (self.gender.get() == "") or (self.t6.get() == "") :
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
                    query = "delete from costumertable where cid=%s"
                    try:
                        myconnection.execute(query, (self.t1.get()))
                        connectionobj.commit()

                        messagebox.showinfo("Success", " information Deleted Successfully",parent=self.my_frame)
                        self.t1.delete(0, END)
                        self.t2.delete(0, END)
                        self.t3.delete(0, END)
                        self.t4.delete(0, END)
                        self.t6.delete(0, END)
                        self.gender.set("choose gender")

                    except Exception as ex:
                        messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
            except Exception as ex:
                messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.my_frame)