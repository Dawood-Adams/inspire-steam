import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ DATABASE ------------------

def init_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        employee_id TEXT UNIQUE,
        national_id TEXT,
        phone TEXT,
        email TEXT,
        department TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ------------------ FUNCTIONS ------------------

def add_employee():
    try:
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employees 
        (first_name, last_name, employee_id, national_id, phone, email, department)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            first_name_var.get(),
            last_name_var.get(),
            employee_id_var.get(),
            national_id_var.get(),
            phone_var.get(),
            email_var.get(),
            department_var.get()
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Employee Added")
        clear_fields()
        load_data()

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Employee ID already exists")

def load_data():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()

def search_employee():
    search_term = search_var.get()

    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM employees 
        WHERE first_name LIKE ? 
        OR last_name LIKE ?
        OR employee_id LIKE ?
    """, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()

def clear_fields():
    first_name_var.set("")
    last_name_var.set("")
    employee_id_var.set("")
    national_id_var.set("")
    phone_var.set("")
    email_var.set("")
    department_var.set("")

def select_record(event):
    selected = tree.focus()
    values = tree.item(selected, "values")

    if values:
        selected_id.set(values[0])
        first_name_var.set(values[1])
        last_name_var.set(values[2])
        employee_id_var.set(values[3])
        national_id_var.set(values[4])
        phone_var.set(values[5])
        email_var.set(values[6])
        department_var.set(values[7])

def update_employee():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees SET
        first_name=?,
        last_name=?,
        employee_id=?,
        national_id=?,
        phone=?,
        email=?,
        department=?
    WHERE id=?
    """, (
        first_name_var.get(),
        last_name_var.get(),
        employee_id_var.get(),
        national_id_var.get(),
        phone_var.get(),
        email_var.get(),
        department_var.get(),
        selected_id.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Updated", "Employee Updated")
    clear_fields()
    load_data()

def delete_employee():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=?", (selected_id.get(),))

    conn.commit()
    conn.close()

    messagebox.showinfo("Deleted", "Employee Deleted")
    clear_fields()
    load_data()

# ------------------ UI DESIGN ------------------

root = tk.Tk()
root.title("Employee Management System")
root.geometry("1000x600")
root.configure(bg="#f4f6f9")

selected_id = tk.IntVar()

first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
employee_id_var = tk.StringVar()
national_id_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
department_var = tk.StringVar()
search_var = tk.StringVar()

# -------- Form Frame --------
form_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
form_frame.place(x=20, y=20, width=350, height=550)

labels = ["First Name", "Last Name", "Employee ID", "National ID", "Phone", "Email", "Department"]
variables = [first_name_var, last_name_var, employee_id_var, national_id_var,
             phone_var, email_var, department_var]

for i, (label, var) in enumerate(zip(labels, variables)):
    tk.Label(form_frame, text=label, bg="white").grid(row=i, column=0, padx=10, pady=8, sticky="w")
    tk.Entry(form_frame, textvariable=var).grid(row=i, column=1, padx=10)

tk.Button(form_frame, text="Add", bg="#28a745", fg="white", width=10, command=add_employee).grid(row=8, column=0, pady=20)
tk.Button(form_frame, text="Update", bg="#ffc107", width=10, command=update_employee).grid(row=8, column=1)
tk.Button(form_frame, text="Delete", bg="#dc3545", fg="white", width=10, command=delete_employee).grid(row=9, column=0)
tk.Button(form_frame, text="Clear", width=10, command=clear_fields).grid(row=9, column=1)

# -------- Table Frame --------
table_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
table_frame.place(x=400, y=20, width=570, height=550)

tk.Label(table_frame, text="Search", bg="white").pack(anchor="w", padx=10)
tk.Entry(table_frame, textvariable=search_var).pack(padx=10, fill="x")
tk.Button(table_frame, text="Search", command=search_employee).pack(pady=5)

columns = ("ID", "First Name", "Last Name", "Emp ID", "National ID", "Phone", "Email", "Department")

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)

tree.pack(fill="both", expand=True)

tree.bind("<ButtonRelease-1>", select_record)

load_data()

root.mainloop()