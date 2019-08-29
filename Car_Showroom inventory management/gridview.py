from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

my_frame = Tk()
my_frame.geometry("%dx%d+%d+%d" % (1000, 600, 0, 0))

mytablearea = Frame(my_frame)
scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

mytable = ttk.Treeview(mytablearea, columns = ('srno', 'name', 'phone', 'address',
                                               'gender', 'sclass'),
                       xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
scrollbarx.config(command=mytable.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
scrollbary.config(command=mytable.yview)
scrollbary.pack(side=RIGHT, fill=Y)

mytable.heading('srno', text="Serial No")
mytable.heading('name', text="Student Name")
mytable.heading('phone', text="Phone")
mytable.heading('address', text="Address")
mytable.heading('gender', text="Gender")
mytable.heading('sclass', text="Class")
# mytable['show']='headings'

mytable.column('#0', stretch=NO, minwidth=0, width=0)
mytable.column('#1', stretch=NO, minwidth=0, width=100)
mytable.column('#2', stretch=NO, minwidth=0, width=150)
mytable.column('#3', stretch=NO, minwidth=0, width=120)
mytable.column('#4', stretch=NO, minwidth=0, width=120)
mytable.column('#5', stretch=NO, minwidth=0, width=120)
mytable.pack()
mytablearea.pack()

try:
        myobj=pymysql.connect(host="localhost", user="root",
                              password="", db="automobile")

        with myobj.cursor() as myconn:
            sql_query="select cid,cname,cadress,cgender,ccity,cphone from costumertable"
            try:
                myconn.execute(sql_query)
                result = myconn.fetchall()
                for myrow in result:
                    mytable.insert('',END,values=(myrow))

                myobj.commit()
                myobj.close()


            except Exception as ex:
                messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))

except Exception as ex:
        messagebox.showerror("Error Occured", "Error occured due to " + str(ex))


my_frame.mainloop()