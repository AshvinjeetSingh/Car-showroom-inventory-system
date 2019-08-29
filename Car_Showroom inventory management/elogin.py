from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
import EmpParentFrame
import ParentFrame
import create_employee
import update_password


class MyLogin1:
    def __init__(self,):

        self.root = tk.Toplevel()
        self.root.title("Employee Login")
        self.width = 700
        self.height = 600
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))

        self.label_0 = Label(self.root, text="EMPLOYEE LOGIN", width=10, font=("bold", 10))
        self.label_0.place(x=150, y=220)

        self.label_1 = Label(self.root, text="USERNAME", width=10, font=("georgia", 15,"bold"))
        self.label_1.place(x=200, y=365)

        self.usernamebox = Entry(self.root)
        self.usernamebox.place(x=370, y=370)
        self.usernamebox.focus()


        self.label_2 = Label(self.root, text="PASSWORD", width=10, font=("georgia", 15,"bold"))
        self.label_2.place(x=200, y=395)

        self.passwordbox = Entry(self.root, show="*")
        self.passwordbox.place(x=370, y=400)
        self.root.bind_all('<Down>',lambda e:self.usernamebox.focus() if self.usernamebox.focus() is not None else self.passwordbox.focus())
        self.root.bind_all('<Up>', lambda e: self.passwordbox.focus() if self.passwordbox.focus() is not None else self.usernamebox.focus())
        self.root.bind_all('<Return>',lambda  e:self.dologin())
        self.saveButton = Button(self.root, text='Login', pady=2,padx=50, bg='brown', fg='white', command=self.dologin,font="georgia")
        self.saveButton.place(x=285, y=450)
        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\E.png')
        self.imagelabel2 = Label(self.root, image=self.myimage1)
        self.imagelabel2.place(x=150, y=100)




        self.root.mainloop()

    def dologin(self):
        connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')

        try:
            with connectionobj.cursor() as myconnection:
                query = "select * from login where Username =%s and Password=%s"
                try:
                    myconnection.execute(query, (self.usernamebox.get(),
                                                 self.passwordbox.get()))
                    result = myconnection.fetchone()
                    if result is not None:
                        self.root.withdraw()
                        self.root.destroy()
                        if result[2] == "Admin":
                            ParentFrame.ParentFrame()
                        else:
                            EmpParentFrame.EmpFrame()

                    else:
                        messagebox.showerror("Invalid", "Wrong username/password",parent=self.root)
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.root)
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.root)





