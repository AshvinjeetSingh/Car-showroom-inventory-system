from tkinter import Tk, ttk, Frame, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, X, Y, RIGHT, messagebox, END, NO, Entry, \
    Button

import pymysql
import tkinter as tk


class ProductsList:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("List of Vechiles")
        width = 550
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
        self.mytablearea = Frame(self.root, width=600, height=50)
        self.scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.tree = ttk.Treeview(self.mytablearea, columns=(
            "cnames", "vvechileno", "vcompanyname", "vcar","vdate", "vdateupto","vfuel","vcapacity","vvechiletype"),
                                 yscrollcommand=self.scrollbary.set,
                                 xscrollcommand=self.scrollbarx.set)
        self.tree['show'] = 'headings'
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.lb1= tk.Label(self.root,text="Vechiles List",font=("georgia",40,"bold")).place(x=390,y=50)


        self.tree.heading("cnames", text="Costumer ID")
        self.tree.heading("vvechileno", text="Vechile Number")
        self.tree.heading("vcompanyname", text="Company")
        self.tree.heading("vcar", text="Vechile Name")
        self.tree.heading("vdate", text="Valid Date Starts From")
        self.tree.heading("vdateupto", text="Valid Upto Date")
        self.tree.heading("vfuel", text="Fuel Type")
        self.tree.heading("vcapacity", text="Capacity")
        self.tree.heading("vvechiletype", text="Vechile Type")

        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=90)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=75)
        self.tree.column('#8', stretch=NO, minwidth=0, width=75)
        self.tree.column('#9', stretch=NO, minwidth=0, width=100)

        self.searchbox = Entry(self.root, width=40)
        self.searchbox.place(x=490, y=490)
        self.searchbutton = Button(self.root, text=" Search", command=self.showrecords,font=("georgia",10,"bold"))
        self.saveicon = tk.PhotoImage(file="magnifier.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)

        self.searchbutton.config(image=self.saveiconsmall, compound=tk.LEFT)
        self.searchbutton.place(x=400, y=490)

        self.myimage1 = tk.PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\rr.png')
        self.imagelabel2 = tk.Label(self.root, image=self.myimage1)
        self.imagelabel2.place(x=950, y=170)



        try:
            self.connectionobj = pymysql.connect(host='localhost', user='root',
                                                 password='', db='automobile')
            with self.connectionobj.cursor() as myconnection:
                query = "select cnames,vvechileno,vcompanyname,vcar,vdate,vdateupto,vfuel,vcapacity,vvechiletype from vechiletable"
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

        self.mytablearea.place(x=100, y=200)
        self.tree.pack()
        self.root.mainloop()

    def showrecords(self):
        try:
                myobj=pymysql.connect(host="localhost", user="root",
                                      password="", db="automobile")

                with myobj.cursor() as myconn:
                    sql_query="select cnames,vvechileno,vcompanyname,vcar,vdate,vdateupto,vfuel,vcapacity,vvechiletype " \
                              "from vechiletable where vvechileno like %s"
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