import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x650")
        self.root.configure(bg="lightblue")

        title = tk.Label(root, text="Student Management System",
                         font=("Arial", 18, "bold"), bg="lightblue")
        title.pack(pady=10)

        form_frame = tk.Frame(root, bg="lightblue")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Student ID:", bg="white",
                 font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.student_id = tk.Entry(form_frame, font=("Arial", 12))
        self.student_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Student Name:", bg="lightblue",
                 font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.student_name = tk.Entry(form_frame, font=("Arial", 12))
        self.student_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Student Course:", bg="lightblue",
                 font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.student_course = tk.Entry(form_frame, font=("Arial", 12))
        self.student_course.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Student Phone:", bg="lightblue",
                 font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.student_phone = tk.Entry(form_frame, font=("Arial", 12))
        self.student_phone.grid(row=3, column=1, padx=10, pady=5)

        # ===== Buttons =====
        button_frame = tk.Frame(root, bg="lightblue")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Student",
                  font=("Arial", 12), bg="green", fg="white",
                  command=self.add_student).grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Search Student",
                  font=("Arial", 12), bg="blue", fg="white",
                  command=self.search_student).grid(row=0, column=1, padx=10)

        tk.Button(button_frame, text="Clear Fields",
                  font=("Arial", 12), bg="orange", fg="white",
                  command=self.clear_fields).grid(row=0, column=2, padx=10)

        # ===== Table =====
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Phone"),
                                 show="headings")

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Course", text="Student Course")
        self.tree.heading("Phone", text="Student Phone")

        self.tree.pack(pady=20, fill="both", expand=True)

    # ===== Add Student =====
    def add_student(self):
        if (self.student_id.get() == "" or
            self.student_name.get() == "" or
            self.student_course.get() == "" or
            self.student_phone.get() == ""):

            messagebox.showwarning("Input Error", "All fields are required!")
            return

        self.tree.insert("", "end", values=(
            self.student_id.get(),
            self.student_name.get(),
            self.student_course.get(),
            self.student_phone.get()
        ))

        messagebox.showinfo("Success", "Student added successfully!")
        self.clear_fields()

    # ===== Search Student =====
    def search_student(self):
        search_id = self.student_id.get()

        if search_id == "":
            messagebox.showwarning("Input Error", "Enter Student ID to search!")
            return

        found = False

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")

            if values[0] == search_id:  # Compare Student ID
                self.tree.selection_set(item)
                self.tree.focus(item)
                self.tree.see(item)
                found = True
                break

        if not found:
            messagebox.showinfo("Not Found", "Student not found.")

    # ===== Clear Fields =====
    def clear_fields(self):
        self.student_id.delete(0, tk.END)
        self.student_name.delete(0, tk.END)
        self.student_course.delete(0, tk.END)
        self.student_phone.delete(0, tk.END)


# ===== Run Application =====
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSystem(root)
    root.mainloop()