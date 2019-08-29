from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import pymysql


class Add_Product:
    def __init__(self):

        self.root = tk.Toplevel()
        self.root.title("Add Product")
        width = 400
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        lb1 = Label(self.root, text="Category Name")
        lb2 = Label(self.root, text="Sub Category Name")
        lb3 = Label(self.root, text="Product Name")
        lb4 = Label(self.root, text="Price")
        lb5 = Label(self.root, text="Quantity")
        self.label_3 = Label(self.root, text="Product ID", width=20, font=("bold", 10))
        self.label_3.place(x=10, y=20)



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
        self.categorybox.bind("<<ComboboxSelected>>", self.getsubcategories)

        self.subcategorybox = ttk.Combobox(self.root)
        self.subcategorybox.set("Choose category first")

        self.productidbox = Entry(self.root)
        self.productnamebox = Entry(self.root)
        self.pricebox = Entry(self.root)
        self.qtybox = Entry(self.root)

        create_btn = Button(self.root, text="Add Product", command=self.addproduct)
        self.root.resizable(0, 0)
        lb1.place(x=50, y=60)
        lb2.place(x=50, y=100)
        lb3.place(x=50, y=150)
        lb4.place(x=50, y=200)
        lb5.place(x=50, y=250)

        self.categorybox.place(x=180, y=60)
        self.subcategorybox.place(x=180, y=100)
        self.productidbox.place(x=180, y=20)
        self.productnamebox.place(x=180, y=150)
        self.pricebox.place(x=180, y=200)
        self.qtybox.place(x=180, y=250)
        create_btn.place(x=180, y=300)

        self.root.mainloop()

    def addproduct(self):

        try:
            myobj = pymysql.connect(host="localhost", user="root",
                                    password="", db="automobile")
            try:
                with myobj.cursor() as myconn:

                    myconn.execute("insert into "
                                   "categorytable "
                                   "values(%s,%s,%s,%s,%s,%s)", (
                                   self.productidbox.get(),self.categorybox.get(), self.subcategorybox.get(), self.productnamebox.get(),
                                   self.pricebox.get(), self.qtybox.get()))
                    myobj.commit()
                    messagebox.showinfo("Success", "Product created Successfully",parent=self.root)


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
            finally:
                myobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))

    def getsubcategories(self, e):
        try:
            connection = pymysql.connect(host='localhost', user='root', password='', db='automobile')
            with connection.cursor() as cursor:
                sql = "SELECT * from combobox where categoryname=%s"
                try:
                    cursor.execute(sql, self.categorybox.get())
                    subcategories = []
                    self.subcategorybox.set("Choose Sub Category Now")
                    result = cursor.fetchall()
                    if len(result) > 0:
                        for row in result:
                            subcategories.append(str(row[1]))
                    else:
                        messagebox.showerror("No Category", "No Sub Categories available")
                    self.subcategorybox.config(values=subcategories)
                except Exception as ex:
                    print("Oops! Something wrong in query due to " + str(ex))
                finally:
                    connection.close()
        except Exception as ex:
            print("Oops! Something wrong in connection due to " + str(ex))