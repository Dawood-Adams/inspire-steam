import tkinter as tk
from tkinter import messagebox

# Store students in a list
students = []

# ----------------------------
# Register Student Function
# ----------------------------
def register_student():
    name = name_entry.get()
    student_id = id_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()

    if name == "" or student_id == "" or phone == "" or course == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Check if ID already exists
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
    messagebox.showinfo("Success", "Student Registered Successfully!")

    clear_fields()

# ----------------------------
# View All Students Function
# ----------------------------
def view_students():
    output.delete("1.0", tk.END)

    if not students:
        output.insert(tk.END, "No students registered yet.\n")
        return

    for student in students:
        output.insert(tk.END,
                      f"Name: {student['name']}\n"
                      f"ID: {student['id']}\n"
                      f"Phone: {student['phone']}\n"
                      f"Course: {student['course']}\n"
                      "----------------------\n")

# ----------------------------
# Search Student Function
# ----------------------------
def search_student():
    search_id = search_entry.get()

    if search_id == "":
        messagebox.showwarning("Input Error", "Please enter a Student ID to search!")
        return

    for student in students:
        if student["id"] == search_id:
            output.delete("1.0", tk.END)
            output.insert(tk.END,
                          f"Student Found:\n\n"
                          f"Name: {student['name']}\n"
                          f"ID: {student['id']}\n"
                          f"Phone: {student['phone']}\n"
                          f"Course: {student['course']}\n")
            return

    messagebox.showerror("Not Found", "Student not found!")

# ----------------------------
# Clear Input Fields
# ----------------------------
def clear_fields():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# ----------------------------
# Create Main Window
# ----------------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x550")

# ----------------------------
# Input Fields
# ----------------------------
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

# ----------------------------
# Buttons
# ----------------------------
tk.Button(root, text="Register Student", command=register_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)

# ----------------------------
# Search Section
# ----------------------------
tk.Label(root, text="Search by Student ID").pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search Student", command=search_student).pack(pady=5)

# ----------------------------
# Output Area
# ----------------------------
output = tk.Text(root, height=12)
output.pack(pady=10)

# Run the application
root.mainloop()