import json

# File to store student data
FILE_NAME = "students.json"

# Load existing students from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Register a new student
def register_student(students):
    print("\n--- Register New Student ---")
    
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    phone = input("Enter phone number: ")
    course = input("Enter course applied for: ")

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student with this ID already exists!")
            return

    student = {
        "name": name,
        "id": student_id,
        "phone": phone,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student registered successfully!")

# View all students
def view_students(students):
    print("\n--- All Registered Students ---")
    
    if not students:
        print("No students registered yet.")
        return

    for student in students:
        print(f"""
Name: {student['name']}
ID: {student['id']}
Phone: {student['phone']}
Course: {student['course']}
-----------------------------""")

# Search student by ID
def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print(f"""
Name: {student['name']}
ID: {student['id']}
Phone: {student['phone']}
Course: {student['course']}
""")
            return

    print("Student not found.")

# Main menu
def main():
    students = load_students()

    while True:
        print("""
====== Student Management System ======
1. Register Student
2. View All Students
3. Search Student by ID
4. Exit
""")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            register_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()