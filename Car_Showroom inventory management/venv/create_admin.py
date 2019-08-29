from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk

class CreateAdmin:
    def __init__(self, root):
        self.label_0 = Label(root, text="Create Admin", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1 = Label(root, text="Username", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.usernamebox = Entry(root)
        self.usernamebox.place(x=240, y=130)


        self.label_2 = Label(root, text="Password", width=20, font=("bold", 10))
        self.label_2.place(x=68, y=180)

        self.passwordbox = Entry(root, show="*")
        self.passwordbox.place(x=240, y=180)

        self.saveButton = Button(root, text='Create Admin', width=15, bg='brown', fg='white', command=self.saveinfo)
        self.saveButton.place(x=240, y=220)

    def saveinfo(self):
        connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')

        try:
            with connectionobj.cursor() as myconnection:
                query = "insert into login values(%s,%s,%s)"
                try:
                    myconnection.execute(query, (self.usernamebox.get(),
                                                 self.passwordbox.get(),
                                                 "Admin"))
                    connectionobj.commit()
                    messagebox.showinfo("User Created successfully", "User Created Successfully",parent=self.my_frame)

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to "+str(ex),parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to "+ str(ex),parent=self.my_frame)


root = tk.Toplevel()
CreateAdmin(root)
root.geometry('500x500')
mainloop()