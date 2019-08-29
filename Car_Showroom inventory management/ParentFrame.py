from tkinter import *

import tkinter as tk
from tkinter.messagebox import askquestion

import SALESCAR
import add_parts
import category
import create_employee
import ctreeview
import dynamicbox
import employeeregister
import etreeview
import insertlogintype
import purchasep

import registration
import treeview
import update_employee
import update_product
import update_registration
import vregistration
import vregistrationupdate
import vtreeview
import SALES

class ParentFrame:
    def __init__(self):
        self.my_frame = tk.Toplevel()
        self.my_frame.focus_force()
        width = 550
        height = 400
        screen_width = self.my_frame.winfo_screenwidth()
        screen_height = self.my_frame.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.my_frame.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
        self.my_frame.title("Automobile Shop Automation System :: Developed by Ashvinjeet Singh")
        self.my_frame.option_add("*tearOff", False)
        self.mymenubar = Menu(self.my_frame)
        self.my_frame.config(menu=self.mymenubar)

        self.registration = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.registration, label="Registration")  # object link

        self.registration.add_command(label='New Registration', command=lambda: registration.Myregistration())
        self.registration.add_separator()
        # self.registration.add_command(label="Display Registration", command=lambda:)
        self.registration.entryconfig('New Registration', accelerator='ctrl+r')
        self.my_frame.bind_all('<Control-r>', lambda e: registration.Myregistration())
        self.registration.add_command(label='Update  Registration',accelerator="ctrl+u", command=lambda: update_registration.UpdateRegistration())
        self.my_frame.bind_all('<Control-u>', lambda e:update_registration.UpdateRegistration())
        self.registration.add_command(label='Display Costumers',command=lambda : treeview.ProductsList())
        self.registration.entryconfig('Display Costumers', accelerator='ctrl+d')
        self.my_frame.bind_all('<Control-d>', lambda e: treeview.ProductsList())

        self.my_frame.bind_all('<Control-d>', lambda e: ctreeview.ProductsList())



        self.empmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.empmenu, label="Employee")  # object link
        self.empmenu.add_command(label='Add New Employee', command=lambda: create_employee.Createemployee())
        self.empmenu.add_cascade(label='Add Employee Details', command=lambda: employeeregister.Myeregistration())
        self.empmenu.add_cascade(label='Update Employee Details', command=lambda: update_employee.UpdateRegistration())

        self.empmenu.add_cascade(label='Display Employee Details', command=lambda: etreeview.ProductsList())
        self.empmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.empmenu, label="Automobile")
        self.empmenu.add_cascade(label='add new vehicle registeration',command=lambda :vregistration.Myvregistration())# object link
        self.empmenu.add_cascade(label='Update Vehicle List', command=lambda: vregistrationupdate.UpdatevRegistration())
        self.empmenu.add_cascade(label='Display Vehicle List', command=lambda: vtreeview.ProductsList())

        self.empmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.empmenu, label="Sales")  # object link
        self.empmenu.add_cascade(label='Product Sales', command=lambda: SALES.Sales())
        self.empmenu.add_cascade(label='Sales Car', command=lambda: SALESCAR.Sales())
        self.empmenu.add_separator()
        self.empmenu.add_cascade(label='Product Purchase', command=lambda: purchasep.Purchase())
        self.empmenu = Menu(self.mymenubar)  # object creation

        self.empmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.empmenu, label="Parts")  # object link

        self.empmenu.add_cascade(label='Add Category', command=lambda:category.Add_Category ())
        self.empmenu.add_cascade(label='Add SubCategory', command=lambda: dynamicbox.Add_Sub_Category())
        self.empmenu.add_cascade(label='Add Parts', command=lambda: add_parts.Add_Product())
        self.empmenu.add_separator()
        self.empmenu.add_cascade(label='Update Parts', command=lambda: update_product.UpdateProduct())
        self.btn1=Button(self.my_frame,text="Logout",font=("georgia","15","bold"),command=self.logout,background="light yellow",width=10).place(x=1150,y=50)



        self.myimage1 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\W.png')
        self.imagelabel2 = Label(self.my_frame, image=self.myimage1)
        self.imagelabel2.pack()
        self.myimage13 = PhotoImage(file='C:\\Users\\ashvi\PycharmProjects\\automobile_management\\k3.png')
        self.imagelabel23 = Label(self.my_frame, image=self.myimage13)
        self.imagelabel23.pack()

        self.my_frame.mainloop()

    def logout(self):
        answer = askquestion("Are you sure", "Do you really want to Quit?", icon="warning",parent=self.my_frame)
        if answer == "yes":
            self.my_frame.destroy()

