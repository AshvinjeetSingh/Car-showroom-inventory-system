from tkinter import Tk, ttk, Frame, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, X, Y, RIGHT, messagebox, END, NO, Entry, \
    Button

import pymysql
import tkinter as tk




class ProductsList:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("List of Costumers")
        width = 550
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
        self.label1= tk.Label(self.root,text="Customer List",font=("georgia",30,"bold"))
        self.label1.place(x=300,y=60)
        self.mytablearea = Frame(self.root, width=600, height=50)
        self.scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.tree = ttk.Treeview(self.mytablearea, columns=(
            "cid", "cname", "cadress", "cgender","ccity", "cphone"),
                                 yscrollcommand=self.scrollbary.set,
                                 xscrollcommand=self.scrollbarx.set)
        self.tree['show'] = 'headings'
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.tree.heading("cid", text="Customer ID")
        self.tree.heading("cname", text="Customer Name")
        self.tree.heading("cadress", text="Address")
        self.tree.heading("cgender", text="Gender")
        self.tree.heading("ccity", text="City")
        self.tree.heading("cphone", text="Phone Number")


        self.tree.column('#1', stretch=NO, minwidth=0, width=70)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=70)
        self.tree.column('#4', stretch=NO, minwidth=0, width=70)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)

        self.searchbox = Entry(self.root, width=40)
        self.searchbox.place(x=250, y=400)
        self.searchbutton = Button(self.root, text=" Search", command=self.showrecords,font=("georgia",10,"bold"))
        self.searchbutton.place(x=500, y=400)
        self.saveicon = tk.PhotoImage(file="magnifier.png")
        self.saveiconsmall = self.saveicon.subsample(1,1)
        self.searchbutton.config(image=self.saveiconsmall, compound=tk.RIGHT)
        self.myimage1 = tk.PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\costum.png')
        self.imagelabel2 = tk.Label(self.root, image=self.myimage1)
        self.imagelabel2.place(x=850, y=100)

        try:
            self.connectionobj = pymysql.connect(host='localhost', user='root',
                                                 password='', db='automobile')
            with self.connectionobj.cursor() as myconnection:
                query = "select cid, cname,cadress,cgender,ccity,cphone from costumertable"
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

        self.mytablearea.place(x=200, y=150)
        self.tree.pack()
        self.root.mainloop()

    def showrecords(self):
        try:
                myobj=pymysql.connect(host="localhost", user="root",
                                      password="", db="automobile")

                with myobj.cursor() as myconn:
                    sql_query="select cid,cname,cadress,cgender,ccity,cphone " \
                              "from costumertable where cname like %s"
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