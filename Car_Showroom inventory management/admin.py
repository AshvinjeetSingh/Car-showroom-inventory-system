from tkinter import *
from tkinter import messagebox
import pymysql


class CreateAdmin:
    def __init__(self):
        self.root = Tk()

        self.width = 550
        self.height = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))

        self.label_0 = Label(self.root, text="Create Admin", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.usernamebox = Entry(self.root)
        self.usernamebox.place(x=240, y=130)

        self.label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        self.label_2.place(x=68, y=180)

        self.passwordbox = Entry(self.root, show="*")
        self.passwordbox.place(x=240, y=180)

        self.saveButton = Button(self.root, text='Create Admin', width=15, bg='brown', fg='white', command=self.saveinfo)
        self.saveButton.place(x=240, y=220)
        self.root.mainloop()

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
                    messagebox.showinfo("User Created successfully", "User Created Successfully")

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to ", str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to ", ex)



