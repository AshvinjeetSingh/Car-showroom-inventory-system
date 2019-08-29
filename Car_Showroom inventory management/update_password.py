from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

import self as self
import tkinter as tk




class Updatepassword:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title("Registration")
        self.my_frame.geometry('1366x768')
        self.my_frame.config(background="white")

        self.label_0 = Label(self.my_frame, text="Create employee", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1 = Label(self.my_frame, text="Username", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.usernamebox = Entry(self.my_frame)
        self.usernamebox.place(x=240, y=130)

        self.label_2 = Label(self.my_frame, text="Password", width=20, font=("bold", 10))
        self.label_2.place(x=68, y=180)

        entryText = tk.StringVar()

        self.passwordbox = Entry(self.my_frame,textvariable=entryText)
        entryText.set("enter your new password")
        self.passwordbox.place(x=240, y=180)

        self.saveButton = Button(self.my_frame, text='search', width=15, bg='brown', fg='white',
                                 command=self.fetchdata)
        self.saveButton.place(x=240, y=220)
    def fetchdata(self):
        #
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:

                query = "select * from login where Username=%s"
                try:
                    myconnectionobj.execute(query, (self.usernamebox.get()))
                    result = myconnectionobj.fetchone()

                    if result is not None:


                        self.passwordbox.insert(0, str(result[1]))
                        self.passwordbox.delete(0, END)

                    else:
                        messagebox.showerror("WRONG INPUT","Username Incorrect",parent=self.my_frame)



                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.my_frame)

    # def updatedata(self):
    #     connectionobj = pymysql.connect(host='localhost', user='root',
    #                                     password='', db='automobile')
    #
    #     try:
    #         with connectionobj.cursor() as myconnection:
    #             query = "update login set Password=%s, " \
    #                     " where Username=%s"
    #             try:
    #                 myconnection.execute(query, (self.passwordbox.get(),
    #                                              self.usernamebox.get()))
    #                 connectionobj.commit()
    #
    #                 messagebox.showinfo("Success", "Product Updated Successfully",parent=self.my_frame)
    #
    #             except Exception as ex:
    #                 messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.my_frame)
    #     except Exception as ex:
    #         messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.my_frame)

