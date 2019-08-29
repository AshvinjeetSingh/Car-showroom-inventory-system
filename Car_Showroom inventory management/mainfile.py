import pymysql
from tkinter import messagebox, ttk

import login
import admin
import mainpage


class mainFile:
    def __init__(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root",
                                    password="", db="automobile")

            with myobj.cursor() as myconn:
                sql_query = "select * from login"
                try:
                    myconn.execute(sql_query)
                    result = myconn.fetchone()
                    if result is not None:
                        mainpage.MyLogin()
                    else:
                        admin.CreateAdmin()


                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in MainFile due to " + str(ex))
                finally:
                    myobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error in connection due to " + str(ex))


obj = mainFile()




