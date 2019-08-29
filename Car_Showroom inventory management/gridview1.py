from tkinter import *
import pymysql
from tkinter import messagebox, ttk
from tkinter.messagebox import askquestion

my_frame = Tk()

mytablearea = Frame(my_frame)
scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

mytable = ttk.Treeview(mytablearea, columns = ('id', 'name',  'address',
                                               'gender','city','phone'),
                       xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

# def showsrno(e):
#     curitem=mytable.focus()
#     contents=(mytable.item(curitem))
#     row = contents['values']
#     fetchdata(str(row[0]))
#
scrollbarx.config(command=mytable.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
scrollbary.config(command=mytable.yview)
scrollbary.pack(side=RIGHT, fill=Y)

mytable.heading('id', text="Costumer ID")
mytable.heading('name', text="Costumer Name")

mytable.heading('address', text="Address")
mytable.heading('gender', text="Gender")
mytable.heading('city', text="City")
mytable.heading('phone', text="Phone")
# mytable['show']='headings'

mytable.column('#0', stretch=NO, minwidth=0, width=0)
mytable.column('#1', stretch=NO, minwidth=0, width=50)
mytable.column('#2', stretch=NO, minwidth=0, width=100)
mytable.column('#3', stretch=NO, minwidth=0, width=100)
mytable.column('#4', stretch=NO, minwidth=0, width=100)
mytable.column('#5', stretch=NO, minwidth=0, width=100)
mytable.column('#6', stretch=NO, minwidth=0, width=100)


def showrecords():
    try:
            myobj=pymysql.connect(host="localhost", user="root",
                                  password="", db="automobile")

            with myobj.cursor() as myconn:
                sql_query="select cid,cname,cadress,cgender,ccity,,cphone " \
                          "from costumertable "
                try:

                    myconn.execute(sql_query)
                    result = myconn.fetchall()
                    mytable.delete(*mytable.get_children())
                    if len(result) > 0:
                        for myrow in result:
                                mytable.insert('',END,values=(myrow))
                    else:
                        messagebox.showinfo("No Result", "No Records found")
                    myobj.commit()
                    myobj.close()

                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))

    except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

#
# mytable.bind("<ButtonRelease-1>", showsrno)




mytable.pack()
mytablearea.place(x=375, y=100)




my_frame.mainloop()
