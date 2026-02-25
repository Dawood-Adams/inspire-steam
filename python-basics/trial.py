import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "students.json"

# ----------------------------
# Load Students from File
# ----------------------------
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# ----------------------------
# Save Students to File
# ----------------------------
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# ----------------------------
# Register Student
# ----------------------------
def register_student():
    name = name_entry.get()
    student_id = id_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if not name or not student_id or not phone or not course:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    for student in students:
        if student["id"] == student_id:
            messagebox.showerror("Error", "Student ID already exists!")
            return

    student = {
        "name": name,
        "id": student_id,
        "phone": phone,
        "course": course
    }

    students.append(student)
    save_students()
    refresh_table()
    clear_fields()

    messagebox.showinfo("Success", "Student Registered Successfully!")
    
# ----------------------------
# Delete Student
# ----------------------------
def delete_student():
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")

    if not confirm:
        return

    item = tree.item(selected_item)
    student_id = item["values"][1]  # ID is second column

    # Remove student from list
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            break

    save_students()
    refresh_table()

    messagebox.showinfo("Deleted", "Student deleted successfully.")
# ----------------------------
# Search Student
# ----------------------------
def search_student():
    search_id = search_entry.get()

    for row in tree.get_children():
        tree.delete(row)

    for student in students:
        if student["id"] == search_id:
            tree.insert("", tk.END, values=(
                student["name"],
                student["id"],
                student["phone"],
                student["course"]
            ))
            return

    messagebox.showerror("Not Found", "Student not found!")

# ----------------------------
# Refresh Table
# ----------------------------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for student in students:
        tree.insert("", tk.END, values=(
            student["name"],
            student["id"],
            student["phone"],
            student["course"]
        ))

# ----------------------------
# Clear Fields
# ----------------------------
def clear_fields():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("800x500")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")

# Load students
students = load_students()

# ----------------------------
# Frames
# ----------------------------
input_frame = ttk.LabelFrame(root, text="Register Student")
input_frame.place(x=20, y=20, width=350, height=300)

table_frame = ttk.LabelFrame(root, text="Student Records")
table_frame.place(x=400, y=20, width=370, height=440)

search_frame = ttk.LabelFrame(root, text="Search Student")
search_frame.place(x=20, y=340, width=350, height=120)

# ----------------------------
# Input Fields
# ----------------------------
ttk.Label(input_frame, text="Name:").pack(pady=5)
name_entry = ttk.Entry(input_frame)
name_entry.pack()

ttk.Label(input_frame, text="Student ID:").pack(pady=5)
id_entry = ttk.Entry(input_frame)
id_entry.pack()

ttk.Label(input_frame, text="Phone:").pack(pady=5)
phone_entry = ttk.Entry(input_frame)
phone_entry.pack()

ttk.Label(input_frame, text="Course:").pack(pady=5)
course_entry = ttk.Entry(input_frame)
course_entry.pack()

ttk.Button(input_frame, text="Register Student", command=register_student).pack(pady=10)
ttk.Button(table_frame, text="Delete Selected", command=delete_student).pack(pady=10)
# ----------------------------
# Search Section
# ----------------------------
ttk.Label(search_frame, text="Enter Student ID:").pack(pady=5)
search_entry = ttk.Entry(search_frame)
search_entry.pack()

ttk.Button(search_frame, text="Search", command=search_student).pack(pady=5)

# ----------------------------
# Table (Professional View)
# ----------------------------
columns = ("Name", "ID", "Phone", "Course")

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)

tree.pack(fill="both", expand=True)

# Load data into table at startup
refresh_table()

root.mainloop()