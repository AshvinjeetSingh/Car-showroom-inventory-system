from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

import self as self
import tkinter as tk




class UpdatePassword:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Update Registration")
        width = 550
        height = 400
        screen_width = self.my_frame.winfo_screenwidth()
        screen_height = self.my_frame.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.my_frame.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.lb1 = Label(self.my_frame, text="Username")
        self.lb2 = Label(self.my_frame, text="Current Password")
        self.lb3 = Label(self.my_frame, text="New Password")
        self.lb4 = Label(self.my_frame, text="Confirm New Password")








        self.t1 = Entry(self.my_frame,width=40)
        self.t2 = Entry(self.my_frame,width=40 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)














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




        self.lb4.place(x=50, y=150)
        self.t4.place(x=220, y=150)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=110)
        self.t3.place(x=220, y=110)









        self.btn1.place(x=150, y=330)
        self.btn2.place(x=490, y=20)

        self.btn1.config(background="lightyellow")
        self.btn2.config(background="lightyellow")


        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\costum.png')
        self.imagelabel2 = Label(self.my_frame, image=self.myimage1)
        self.imagelabel2.place(x=750, y=100)
        self.my_frame.mainloop()

    def fetchdata(self):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from login where Username=%s"
                try:
                    myconnectionobj.execute(query, self.t1.get())
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.t2.delete(0, END)
                        self.t2.insert(0, str(result[1]))







                    else:
                        messagebox.showerror("WRONG INPUT","Costumer ID Incorrect",parent=self.my_frame)



                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Connection Error1", "Error in Connection due to " + str(ex),parent=self.my_frame)

    def updatedata(self):
        if self.t3.get() == self.t4.get():
            try:
                myobj = pymysql.connect(host="localhost", user="root",
                                        password="", db="automobile")
                try:
                    with myobj.cursor() as myconn:

                        affected_rows = myconn.execute("update login "
                                                       "set Password=%s "
                                                       "where Username=%s "
                                                       "and Password=%s",
                                                       (self.t4.get(), self.t1.get(),
                                                        self.t2.get()))

                        myobj.commit()
                        if affected_rows > 0:
                            messagebox.showinfo("Success", "Password updated Successfully", parent=self.my_frame)
                        else:
                            messagebox.showwarning("Warning", "Old Password is wrong", parent=self.my_frame)



                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                finally:
                    myobj.close()
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))
        else:
            messagebox.showwarning("Warning", "Password does not match")

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