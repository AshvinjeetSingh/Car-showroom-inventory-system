from tkinter import Tk, ttk, Frame, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, X, Y, RIGHT, messagebox, END, NO, Entry, \
    Button

import pymysql
import tkinter as tk


class ProductsList:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("vechiles list")
        self.root.geometry('800x600')
        self.mytablearea = Frame(self.root, width=600, height=50)
        self.scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.tree = ttk.Treeview(self.mytablearea, columns=(
            "cnames", "vvechileno","vcompanyname","vcar", "vdate", "vdateupto","vfuel","vvechiletype" "vcapacity"),
                                 yscrollcommand=self.scrollbary.set,
                                 xscrollcommand=self.scrollbarx.set)
        self.tree['show'] = 'headings'
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.tree.heading("cnames", text="Costumer ID")
        self.tree.heading("vvechileno", text="Vechile Number")
        self.tree.heading("vcompanyname", text="Vechile Company Name")
        self.tree.heading("vcar", text="Vechile Name")
        self.tree.heading("vdate", text="Vechile Valid Date Starts From")
        self.tree.heading("vdateupto", text="Vechile Date Valid Upto")
        self.tree.heading("vvechiletype", text="Vechile Type")
        self.tree.heading("vfuel", text="Vechile Fuel Type")
        self.tree.heading("vcapacity", text="Vechile Capacity")

        self.tree.column('#1', stretch=NO, minwidth=0, width=70)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=70)
        self.tree.column('#4', stretch=NO, minwidth=0, width=70)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=100)
        self.tree.column('#8', stretch=NO, minwidth=0, width=100)
        self.tree.column('#9', stretch=NO, minwidth=0, width=100)

        self.searchbox = Entry(self.root, width=40)
        self.searchbox.place(x=250, y=500)
        self.searchbutton = Button(self.root, text=" search here", command=self.showrecords)
        self.searchbutton.place(x=100, y=500)
        try:
            self.connectionobj = pymysql.connect(host='localhost', user='root',
                                                 password='', db='automobile')
            with self.connectionobj.cursor() as myconnection:
                query = "select cnames, vvechileno,vcompanyname,vcar,vdate,vdateupto,vfuel,vvechiletype,vcapacity from vechiletable"
                try:
                    myconnection.execute(query)
                    result = myconnection.fetchall()
                    if result is not None:
                        for row in result:
                            self.tree.insert('', END, values=(row))
                    else:
                        messagebox.showerror("No Records", "Products not added")
                except Exception as ex:
                    messagebox.showerror("Error in Query", "Error in Query due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex))

        self.mytablearea.place(x=50, y=50)
        self.tree.pack()
        self.root.mainloop()

    def showrecords(self):
        try:
                myobj=pymysql.connect(host="localhost", user="root",
                                      password="", db="automobile")

                with myobj.cursor() as myconn:
                    sql_query="select cnames,vvechileno,vcompanyname,vcar,vdate,vdateupto,vfuel,vvechiletype,vcapacity " \
                              "from vechiletable where cnames like %s"
                    try:

                        myconn.execute(sql_query, "%"+self.searchbox.get() + "%")
                        result = myconn.fetchall()
                        self.tree.delete(*self.tree.get_children())
                        if len(result) > 0:
                            for myrow in result:
                                    self.tree.insert('',END,values=(myrow))
                        else:
                            messagebox.showinfo("No Result", "No Records found")
                        myobj.commit()
                        myobj.close()

                    except Exception as ex:
                        messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))

        except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured due to " + str(ex))