from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

class Student_system:
    def __init__(self,root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("600x450")
        self.root.configure(bg = "yellow", fg = "green")
        root = Tk()
        frame_one = Frame(root)
        frame_one.pack()
        # Creating the title
        heading = Tk.Label(root,text="Student Management System")
        def student():
            print(input("Enter student name:{name}"))

        button_one = Button(frame_one, text="Student",command = student)
        button_one.pack()
        root.mainloop()
