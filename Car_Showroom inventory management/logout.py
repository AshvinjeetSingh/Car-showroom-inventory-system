from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import pymysql


class ChangePass:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Change Password")
        width = 500
        height = 300

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.uname=Entry(self.root).place(x=150,y=50)

        lb1=Label(self.root, text="Current Password")
        lb2=Label(self.root, text="New Password")
        lb3=Label(self.root, text="Confirm Password")
        lb4=Label(self.root, text="Username")

        self.currentpassbox = Entry(self.root)
        self.currentpassbox.focus()
        self.newpassbox = Entry(self.root,show="*")
        self.confirmpassbox = Entry(self.root,show="*")
        create_btn=Button(self.root, text="Change Password", command=self.changepassword)
        self.btn2 = Button(self.root,text="check", padx=10, command=self.fetchdata, font="georgia")
        self.btn2.place(x=250,y=50)
        self.root.resizable(0, 0)
        lb4.place(x=50,y=50)
        lb1.place(x=50,y=100)
        lb2.place(x=50,y=150)
        lb3.place(x=50,y=200)
        self.currentpassbox.place(x=150,y=100)
        self.newpassbox.place(x=150,y=150)
        self.confirmpassbox.place(x=150,y=200)
        create_btn.place(x=150,y=250)
        #messagebox.showinfo("Important Info", "Running Software for first time, please create Admin Account First")
        self.root.mainloop()

    def fetchdata(self):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from login where Username=%s"
                try:
                    myconnectionobj.execute(query,self.uname.get())
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.currentpassbox.delete(0, END)
                        self.currentpassbox.insert(0, result[1])

                    else:
                        messagebox.showerror("WRONG INPUT","Username Incorrect",parent=self.root)



                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.root)
        except Exception as ex:
            messagebox.showerror("Connection Error1", "Error in Connection due to " + str(ex),parent=self.root)

    def changepassword(self):

        if self.newpassbox.get() == self.confirmpassbox.get():
            try:
                    myobj=pymysql.connect(host="localhost", user="root",
                                          password="", db="automobile")
                    try:
                        with myobj.cursor() as myconn:

                            affected_rows = myconn.execute("update login "
                                           "set Password=%s "
                                           "where Username=%s "
                                           "and Password=%s",
                                           (self.confirmpassbox.get(), self.uname.get(), self.currentpassbox.get()))


                            myobj.commit()
                            if affected_rows > 0:
                                messagebox.showinfo("Success", "Password updated Successfully", parent=self.root)
                            else:
                                messagebox.showwarning("Warning", "Old Password is wrong", parent=self.root)



                    except Exception as ex:
                            messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                    finally:
                            myobj.close()
            except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))
        else:
            messagebox.showwarning("Warning", "Password does not match")