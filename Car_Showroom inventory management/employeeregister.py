import time
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

import pymysql
from tkinter import messagebox, ttk,Tk,Canvas
from tkinter.messagebox import askquestion

from PIL import ImageTk
from PIL import ImageTk
from PIL import Image
from tkinter.filedialog import askopenfilename







class Myeregistration:


    def __init__(self):
        self.my_frame = tk.Toplevel()

        self.my_frame.title(" Employee Registration")
        self.my_frame.geometry('1366x768')




        self.imagelb1=Label(self.my_frame,text="Employee Login",font=("georgia",50,"bold"))
        self.lb1 = Label(self.my_frame, text="Employee Username")
        self.lb2 = Label(self.my_frame, text="Employee Name")
        self.lb3 = Label(self.my_frame, text="Employee Address")
        self.lb4 = Label(self.my_frame, text="Employee City")
        self.lb5 = Label(self.my_frame, text="Employee Date Of Birth")
        self.lb6 = Label(self.my_frame, text="Employee Phone Number")
        self.lb7 = Label(self.my_frame, text="Gender")


        self.ment=StringVar()
        self.t1 = Entry(self.my_frame, width=40,textvariable=self.ment)
        self.t2 = Entry(self.my_frame,width=40 )
        self.t3 = Entry(self.my_frame, width=40)
        self.t4 = Entry(self.my_frame, width=40)
        self.t5 = Entry(self.my_frame, width=40)
        self.t6 = Entry(self.my_frame, width=40)


        self.t1.focus()





        self.list=["Male","Female","Others"]
        self.gender = ttk.Combobox(self.my_frame)
        self.gender.config(values=self.list, state="readonly")
        self.gender.set("Choose gender")
        self.gender.place(x=220, y=260)







        self.btn1 = Button(self.my_frame, text="Save", padx=10,font=("georgia",8,"bold"), command=self.savedata, width=240)
        self.saveicon = PhotoImage(file="save.png")
        self.saveiconsmall = self.saveicon.subsample(1, 1)
        self.btn1.config(image=self.saveiconsmall, compound=RIGHT)


        self.lb4.place(x=50, y=140)
        self.t4.place(x=220, y=140)
        self.lb1.place(x=50, y=20)
        self.t1.place(x=220, y=20)
        self.lb2.place(x=50, y=60)
        self.t2.place(x=220, y=60)
        self.lb3.place(x=50, y=100)
        self.t3.place(x=220, y=100)
        self.lb5.place(x=50, y=180)
        self.t5.place(x=220, y=180)

        self.lb6.place(x=50, y=220)
        self.t6.place(x=220, y=220)
        self.lb7.place(x=50, y=260)

        self.btn1.place(x=170, y=360)
        self.imageuploadbtn = Button(self.my_frame, text="Upload Photo",width=30,padx=10,font=("georgia",8,"bold"), command=self.imageupload).place(x=170, y=310)





        self.imglabel = Label(self.my_frame, borderwidth=1, text="", width=200, height=200)
        self.imglabel.place(x=1050, y=20)











        self.my_frame.mainloop()
    def savedata(self):


        try:
            myobj=pymysql.connect(host="localhost", user="root",
                              password="", db="automobile")

            with myobj.cursor() as myconn:


                myconn.execute("insert into "
                           "employeetable(eusername,ename,eadress, ecity,edob,egender,ephone) "
                           "values(%s,%s,%s,%s,%s,%s,%s)",

                     (self.t1.get(), self.t2.get(), self.t3.get(),
                      self.t4.get(),self.t5.get(),self.gender.get(),self.t6.get()))

                if (self.t1.get() == "") or (self.t2.get() == "") or (self.t3.get() == "") or (self.t4.get() == "") or (self.gender.get() == "") or (self.t6.get() == "") :
                    messagebox.showerror("fill box", "complete the entries", parent=self.my_frame)
                #
                #
                else:

                    myobj.commit()
                    myobj.close()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.my_frame)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex),parent=self.my_frame)

    def imageupload(self):
        self.filename = askopenfilename(
            filetypes=[(("Picture Files",
                         "*.jpg;*.png;*.gif"))])  # show an "Open" dialog box and return the path to the selected file
        img = Image.open(self.filename)
        self.finalname = str(int(time.time()))
        img.save("userimages//" + self.finalname + ".jpg")
        tkimage = ImageTk.PhotoImage(img)
        self.imglabel.configure(image=tkimage)
        self.imglabel.image = tkimage