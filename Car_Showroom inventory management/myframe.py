from tkinter import *


import  combobox


class ParentFrame:
    def __init__(self):
        self.my_frame = Tk()
        self.my_frame.geometry("1024x700")
        self.my_frame.title("Automobile Shop Automation System :: Developed by Ashvinjeet Singh")
        self.my_frame.option_add("*tearOff", False)
        self.mymenubar = Menu(self.my_frame)
        self.my_frame.config(menu=self.mymenubar)

        self.stockmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.stockmenu, label="Vechile")  # object link

        self.stockmenu.add_command(label='Vechile number', command=lambda: print("Vechile no. clicked"))
        self.stockmenu.add_command(label="Company name", command=lambda: print("company name clicked"))
        self.stockmenu.add_separator()
        self.stockmenu.add_command(label='product', command=lambda: print("product clicked"))

        self.empmenu = Menu(self.mymenubar)  # object creation
        self.mymenubar.add_cascade(menu=self.empmenu, label="Employee")
        self.empmenu.add_command(label='employee name', command=lambda: print("details clicked"))
        self.empmenu.add_command(label='employee id', command=lambda: print("details clicked"))
        self.empmenu.add_command(label='employee date of registration', command=lambda: print("details clicked"))

        self.my_frame.mainloop()