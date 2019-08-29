from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk

import pymysql

class Add_Sub_Category:
    def __init__(self):

        self.root = tk.Toplevel()
        self.root.title("Add Sub Category")
        width = 400
        height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x,y))

        lb1=Label(self.root, text="Category Name")
        lb2=Label(self.root, text="Sub Category Name")



        self.categorybox = ttk.Combobox(self.root)



        try:
            connection = pymysql.connect(host='localhost',user='root',password='',db='automobile')
            with connection.cursor() as cursor:
                sql = "SELECT * from category"
                try:
                    cursor.execute(sql)
                    categories=[]
                    result = cursor.fetchall()
                    if len(result)>0:
                        for row in result:
                            categories.append(str(row[0]))
                    else:
                        messagebox.showerror("No Category", "No Categories available")

                except Exception as ex:
                    print("Oops! Something wrong due to " + str(ex))

            connection.commit()
        finally:
            connection.close()
        self.categorybox.config(values=categories)
        self.categorybox.set("Choose category")

        self.subcatnamebox = Entry(self.root)

        create_btn=Button(self.root, text="Add Sub Category", command=self.addsubcategory)
        self.root.resizable(0, 0)
        lb1.place(x=50,y=50)
        lb2.place(x=50,y=100)
        self.categorybox.place(x=180,y=50)
        self.subcatnamebox.place(x=180,y=100)
        create_btn.place(x=180,y=150)

        self.root.mainloop()


    def addsubcategory(self):

        try:
                myobj=pymysql.connect(host="localhost", user="root",
                                      password="", db="automobile")
                try:
                    with myobj.cursor() as myconn:

                        myconn.execute("insert into "
                                       "combobox "
                                       "values(%s,%s)",(self.categorybox.get(), self.subcatnamebox.get()))
                        myobj.commit()
                        messagebox.showinfo("Success", "Sub Category created Successfully",parent=self.root)


                except Exception as ex:
                        messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex),parent=self.root)
                finally:
                        myobj.close()
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex),parent=self.root)