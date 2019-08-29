from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion
from tkinter.ttk import Combobox

import pymysql
import  tkinter as tk


class UpdateProduct:
    def __init__(self):
        self.root = tk.Toplevel()
        width = 1300
        height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.label_0 = Label(self.root, text="Update Product", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1 = Label(self.root, text="Category Name", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')
        self.categories=[]
        try:
            with self.connectionobj.cursor() as myconnection:
                query = "select * from category"
                try:
                    myconnection.execute(query)
                    result = myconnection.fetchall()
                    if result is not None:
                        for row in result:
                            self.categories.append(row[0])
                    else:
                        messagebox.showerror("No Records", "Categories not added")
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

        self.categorybox = Combobox(self.root)
        self.categorybox.config(values=self.categories)
        self.categorybox.set("Choose Category")
        self.categorybox.place(x=240, y=130)

        self.label_2 = Label(self.root, text="Sub Category Name", width=20, font=("bold", 10))
        self.label_2.place(x=80, y=160)

        self.subcategorybox = Combobox(self.root)
        self.subcategorybox.set("Choose Category first")
        self.subcategorybox.place(x=240, y=160)

        self.label_3 = Label(self.root, text="Product ID", width=20, font=("bold", 10))
        self.label_3.place(x=80, y=200)

        self.productidbox = Entry(self.root)
        self.label_4 = Label(self.root, text="Product Name", width=20, font=("bold", 10))
        self.label_4.place(x=80, y=240)
        self.productnamebox = Entry(self.root)
        self.label_5 = Label(self.root, text="Price", width=20, font=("bold", 10))
        self.label_5.place(x=80, y=280)
        self.pricebox = Entry(self.root)
        self.label_6 = Label(self.root, text="Qty", width=20, font=("bold", 10))
        self.label_6.place(x=80, y=320)

        self.fetchButton = Button(self.root, text='Search', width=10, bg='brown', fg='white', command=self.fetchinfo)
        self.saveicon = PhotoImage(file="magnifier.png")

        self.fetchButton.place(x=400, y=200)

        self.searchbox = Entry(self.root, width=40)
        self.searchbox.place(x=700, y=400)
        self.searchbutton = Button(self.root, text="Search", command=self.showrecords,width=60)
        self.searchbutton.place(x=600, y=400)
        self.saveicon = PhotoImage(file="magnifier.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.searchbutton.config(image=self.saveiconsmall, compound=LEFT)

        self.qtybox = Entry(self.root)
        self.productidbox.place(x=240, y=200)
        self.productnamebox.place(x=240, y=240)
        self.pricebox.place(x=240, y=280)
        self.qtybox.place(x=240, y=320)
        self.categorybox.bind("<<ComboboxSelected>>", self.fetch_subcategories)
        self.updateButton = Button(self.root, text='Update Product', width=20, bg='brown', fg='white', command=self.updateinfo)
        self.updateButton.place(x=240, y=400)

        self.deleteButton = Button(self.root, text='Delete Product', width=20, bg='brown', fg='white',
                                   command=self.deleteinfo)
        self.deleteButton.place(x=240, y=440)

        self.mytablearea = Frame(self.root, width=300, height=50)
        self.scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.tree = ttk.Treeview(self.mytablearea, columns=(
            "pid", "partname", "price", "qty", "categoryname","subcategoryname"),
                                 yscrollcommand=self.scrollbary.set,
                                 xscrollcommand=self.scrollbarx.set)
        self.tree['show'] = 'headings'
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.tree.heading("pid", text="Product ID")
        self.tree.heading("partname", text="Product Name")
        self.tree.heading("price", text="Price")
        self.tree.heading("qty", text="Quantity")
        self.tree.heading("categoryname", text="Category")
        self.tree.heading("subcategoryname", text=" Sub Category")

        self.tree.column('#1', stretch=NO, minwidth=0, width=70)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=70)
        self.tree.column('#4', stretch=NO, minwidth=0, width=70)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)

        try:
            self.connectionobj = pymysql.connect(host='localhost', user='root',
                                                 password='', db='automobile')
            with self.connectionobj.cursor() as myconnection:
                query = "select pid,partname,price,qty,categoryname,subcategoryname " \
                        "from categorytable "
                try:
                    myconnection.execute(query)
                    result = myconnection.fetchall()
                    if result is not None:
                        for row in result:
                            self.tree.insert('', END, values=(row))
                    else:
                        messagebox.showerror("No Records", "Products not found")
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

        self.mytablearea.place(x=500, y=150)
        self.tree.pack()
        self.tree.bind("<ButtonRelease-1>", self.fetchinfo2)
        self.root.mainloop()

    def fetchinfo(self):

        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from categorytable where pid=%s"
                try:
                    myconnectionobj.execute(query, (self.productidbox.get()))
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.productnamebox.delete(0,END)
                        self.productnamebox.insert(0, str(result[3]))
                        self.pricebox.delete(0,END)
                        self.pricebox.insert(0, str(result[4]))
                        self.qtybox.delete(0,END)
                        self.qtybox.insert(0, str(result[5]))

                        self.categorybox.set(str(result[1]))
                        self.fetch_subcategories2()
                        self.subcategorybox.set(str(result[2]))
                    else:
                        messagebox.showerror("No Records", "Sub Categories not added")

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

    def fetchinfo2(self,e):
        selectedrow = self.tree.focus()
        contents = self.tree.item(selectedrow)
        rowcontent = contents['values']
        # messagebox.showinfo("Product ID", rowcontent[0], parent=self.root)



        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                          password='', db='automobile')
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from categorytable where pid=%s"
                try:
                    myconnectionobj.execute(query, (rowcontent[0]))
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.productnamebox.delete(0,END)
                        self.productnamebox.insert(0, str(result[3]))

                        self.productidbox.delete(0, END)
                        self.productidbox.insert(0, str(result[0]))

                        self.pricebox.delete(0,END)
                        self.pricebox.insert(0, str(result[4]))
                        self.qtybox.delete(0,END)
                        self.qtybox.insert(0, str(result[5]))

                        self.categorybox.set(str(result[1]))
                        self.fetch_subcategories2()
                        self.subcategorybox.set(str(result[2]))
                    else:
                        messagebox.showerror("No Records", "Sub Categories not added")

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))


    def fetch_subcategories(self, detail):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                             password='', db='automobile')
        self.subcategories = []
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from combobox where categoryname=%s"
                try:
                    myconnectionobj.execute(query,(self.categorybox.get()))
                    result = myconnectionobj.fetchall()
                    self.subcategorybox.set("Choose Sub Category now")
                    if result is not None:
                        for row in result:
                            self.subcategories.append(row[1])
                    else:
                        messagebox.showerror("No Records", "Sub Categories not added")
                    self.subcategorybox.config(values=self.subcategories)
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

    def fetch_subcategories2(self):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                             password='', db='automobile')
        self.subcategories = []
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from combobox where categoryname=%s"
                try:
                    myconnectionobj.execute(query,(self.categorybox.get()))
                    result = myconnectionobj.fetchall()
                    self.subcategorybox.set("Choose Sub Category now")
                    if result is not None:
                        for row in result:
                            self.subcategories.append(row[1])
                    else:
                        messagebox.showerror("No Records", "Sub Categories not added")
                    self.subcategorybox.config(values=self.subcategories)
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))


    def updateinfo(self):
        connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')

        try:
            with connectionobj.cursor() as myconnection:
                query = "update categorytable set categoryname=%s, " \
                        "subcategoryname=%s, " \
                        "partname=%s, price=%s, qty=%s where pid=%s"
                try:
                    myconnection.execute(query, (self.categorybox.get(),
                                                 self.subcategorybox.get(),
                                                 self.productnamebox.get(),
                                                 self.pricebox.get(),
                                                 self.qtybox.get(),
                                                 self.productidbox.get()))
                    connectionobj.commit()

                    messagebox.showinfo("Success", "Product Updated Successfully")

                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to "+ str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to "+ str(ex))

    def deleteinfo(self):

        answer = askquestion("Are you sure", "Do you really want to delete?",icon="warning")
        if answer=="yes":

            connectionobj = pymysql.connect(host='localhost', user='root',
                                            password='', db='automobile')

            try:
                with connectionobj.cursor() as myconnection:
                    query = "delete from categorytable where pid=%s"
                    try:
                        myconnection.execute(query, (self.productidbox.get()))
                        connectionobj.commit()

                        messagebox.showinfo("Success", "Product Deleted Successfully")
                        self.productnamebox.delete(0,END)
                    except Exception as ex:
                        messagebox.showerror("Error in Query", "Error in Query due to "+ str(ex))
            except Exception as ex:
                messagebox.showerror("Connection Error", "Error in Connection due to "+ str(ex))

    def showrecords(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root",
                                password="", db="automobile")

            with myobj.cursor() as myconn:
                sql_query = "select pid,partname,price,qty,categoryname,subcategoryname " \
                        "from categorytable where partname like %s"
                try:

                    myconn.execute(sql_query, "%" + self.productnamebox.get() + "%")
                    result = myconn.fetchall()
                    self.tree.delete(*self.tree.get_children())
                    if len(result) > 0:
                        for myrow in result:
                            self.tree.insert('', END, values=(myrow))
                    else:
                        messagebox.showinfo("No Result", "No Records found")
                    myobj.commit()
                    myobj.close()

                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))