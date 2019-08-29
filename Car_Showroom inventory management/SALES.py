from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox
import tkinter as tk

import pymysql


class Sales:
    def __init__(self):

        self.root = tk.Toplevel()
        self.root.title("Sales")
        width = 900
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        mytablearea=Frame(self.root)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)
        self.tree = ttk.Treeview(mytablearea, columns=("id","Name", "Price", "Qty", "TotalCost"),
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree["show"]="headings"
        self.tree.heading('id', text="Product ID", anchor=W)
        self.tree.heading('Name', text="Product Name",anchor=W)
        self.tree.heading('Price', text="Price",anchor=W)
        self.tree.heading('Qty', text="Quantity",anchor=W)
        self.tree.heading('TotalCost', text="Total Cost",anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=250)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.pack()

        lb4 = Label(self.root, text="Price")
        self.productid_label = Label(self.root, text="Product ID")
        self.productidbox = Label(self.root, text="0")

        self.oldqty_label = Label(self.root, text="Old Qty")
        self.oldqtybox = Label(self.root, text="0")

        billnolabel = Label(self.root, text="Bill No")
        self.billnobox = Label(self.root, text="0")
        lb5 = Label(self.root, text="Qty")
        lb6 = Label(self.root, text="Date of Purchase")
        grandtotal_lbl = Label(self.root, text="Grand Total")
        self.grandtotalamt_lbl = Label(self.root, text="0")
        lb7 = Label(self.root, text="Buyer Name")

        self.categorybox = ttk.Combobox(self.root)
        try:
            connection = pymysql.connect(host='localhost', user='root', password='', db='automobile')
            with connection.cursor() as cursor:
                sql = "SELECT * from category"
                try:
                    cursor.execute(sql)
                    categories = []
                    result = cursor.fetchall()
                    if len(result) > 0:
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
        self.categorybox.bind("<<ComboboxSelected>>", self.fetch_subcategories)

        self.subcategorybox = ttk.Combobox(self.root)
        self.subcategorybox.set("Choose category first")
        self.subcategorybox.bind("<<ComboboxSelected>>", self.fetch_products)

        self.productnamebox = ttk.Combobox(self.root, width=35)
        self.productnamebox.set("Choose sub category first")
        self.productnamebox.bind("<<ComboboxSelected>>", self.fetch_productdetail)

        self.datebox=Entry(self.root)
        self.customerbox=Entry(self.root, width=30)
        self.pricebox = Entry(self.root)
        self.qtybox = Entry(self.root, width=10)
        self.addbtn=Button(self.root, text="Add", command=self.addtocart)
        self.remove_btn = Button(self.root, text="Remove", command=self.removeitem)
        self.grandtotal_btn = Button(self.root, text="Grand Total", command=self.calculategrandtotal)
        self.savebtn=Button(self.root,text="Save", command=self.saveinfo)
        self.root.resizable(0, 0)

        billnolabel.place(x=30, y=30)
        self.billnobox.place(x=80, y=30)

        lb6.place(x=50, y=50)
        lb7.place(x=300, y=50)
        self.generatebillno()
        self.datebox.place(x=150, y=50)
        self.customerbox.place(x=400, y=50)

        self.productid_label.place(x=600, y=50)
        self.productidbox.place(x=700, y=50)
        self.categorybox.place(x=50, y=100)
        self.subcategorybox.place(x=200, y=100)
        self.productnamebox.place(x=350, y=100)
        lb4.place(x=600, y=80)
        self.pricebox.place(x=600, y=100)
        lb5.place(x=750, y=80)
        self.qtybox.place(x=750, y=100)

        self.oldqty_label.place(x=750, y=120)
        self.oldqtybox.place(x=800, y=120)

        self.addbtn.place(x=830, y=95)
        mytablearea.place(x=50, y=150)
        self.remove_btn.place(x=450, y=450)
        self.grandtotal_btn.place(x=650, y=450)
        grandtotal_lbl.place(x=550, y=400)
        self.grandtotalamt_lbl.place(x=650, y=400)
        self.savebtn.place(x=650,y=500)

    #    self.pricebox.place(x=180, y=200)
    #    self.qtybox.place(x=180, y=250)
     #   create_btn.place(x=180, y=300)

        self.root.mainloop()

    def calculategrandtotal(self):
        sum=0
        allrows = self.tree.get_children()
        for content in allrows:
            allcontents = self.tree.item(content)
            row = allcontents['values']
            sum += int(row[4])
        self.grandtotalamt_lbl.config(text=str(sum))

    def generatebillno(self):
        try:
            self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                              password='', db='automobile')
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select max(billno) from salestable"
                try:
                    myconnectionobj.execute(query)
                    result = myconnectionobj.fetchone()
                    if result is not None:
                        if result[0] is None:
                            self.billnobox.config(text="1000")
                        else:
                            oldbillno = result[0]
                            newbillno = oldbillno + 1
                            self.billnobox.config(text=newbillno)



                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

    def removeitem(self):
        selectedrow = self.tree.focus()
        self.tree.delete(selectedrow)

    def addtocart(self):

        if int(self.qtybox.get()) <= int(self.oldqtybox.cget("text")):
            try:
                myrows = []
                myrows.append(self.productidbox.cget("text"))
                myrows.append(self.productnamebox.get())
                myrows.append(self.pricebox.get())
                myrows.append(self.qtybox.get())
                myrows.append(int(self.pricebox.get()) * int(self.qtybox.get()))
                self.tree.insert('',END,values=(myrows))

            except Exception as e:
                messagebox.showerror("Error in Query", "Error in Query due to " + str(e))
        else:
            messagebox.showerror("Not Enough Quantity", "Please check quantity")

    def fetch_productdetail(self, detail):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                             password='', db='automobile')
        self.products = []
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from categorytable where partname=%s"
                try:
                    myconnectionobj.execute(query,(self.productnamebox.get()))
                    result = myconnectionobj.fetchone()

                    if result is not None:
                        self.productidbox.config(text=result[0])
                        self.oldqtybox.config(text=result[5])

                    else:
                        messagebox.showerror("No Records", "Products not added")

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

    def fetch_products(self, detail):
        self.pymysqlobj = pymysql.connect(host='localhost', user='root',
                                             password='', db='automobile')
        self.products = []
        try:
            with self.pymysqlobj.cursor() as myconnectionobj:
                query = "select * from categorytable where subcategoryname=%s"
                try:
                    myconnectionobj.execute(query,(self.subcategorybox.get()))
                    result = myconnectionobj.fetchall()
                    self.productnamebox.set("Choose Product now")
                    if result is not None:
                        for row in result:
                            self.products.append(row[3])
                    else:
                        messagebox.showerror("No Records", "Products not added")
                    self.productnamebox.config(values=self.products)
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))


    def saveinfo(self):
        connectionobj = pymysql.connect(host='localhost', user='root',
                                        password='', db='automobile')

        try:
            with connectionobj.cursor() as myconnection:
                query = "insert into salestable values(%s, %s,%s,%s)"
                try:
                    myconnection.execute(query, (self.billnobox.cget("text"),
                                                 self.customerbox.get(),
                                                 self.datebox.get(),
                                                 self.grandtotalamt_lbl.cget("text")
                                                ))
                    connectionobj.commit()



                    allrows = self.tree.get_children()
                    for content in allrows:
                        allcontent = self.tree.item(content)
                        row = allcontent['values']
                        pid = row[0]
                        pname = row[1]
                        price = row[2]
                        qty = row[3]
                        tc = row[4]

                        query = "insert into salesdetail values(%s,%s,%s,%s,%s,%s)"
                        try:
                            myconnection.execute(query, (self.billnobox.cget("text"),
                                                         pid,
                                                         pname, price, qty, tc
                                                         ))
                            connectionobj.commit()
                            query = "delete from categorytable set qty=qty-%s where pid=%s"
                            try:
                                myconnection.execute(query, (int(qty),
                                                             pid
                                                             ))
                                connectionobj.commit()
                                messagebox.showinfo("Success", "Sales Added Successfully")
                            except Exception as ex:
                                messagebox.showerror("Error in Query 3", "Error in Query due to " + str(ex))

                        except Exception as ex:
                            messagebox.showerror("Error in Query 2", "Error in Query due to " + str(ex))


                except Exception as ex:
                    messagebox.showerror("Error in Query 1", "Error in Query due to "+ str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to "+ str(ex))
