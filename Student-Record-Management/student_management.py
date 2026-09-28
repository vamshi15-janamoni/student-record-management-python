import json
import os

JSON_FILE = "students.json"


def load_students():
    try:
        if not os.path.exists(JSON_FILE):
            return []

        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid JSON structure. Starting with an empty list.")
            return []

        return data

    except json.JSONDecodeError:
        print("Error: students.json is corrupted.")
        return []
    except OSError as error:
        print(f"File error: {error}")
        return []


def save_students(students):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError as error:
        print(f"Unable to save records: {error}")


def add_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID: "))
        if any(student["id"] == student_id for student in students):
            print("Student ID already exists.")
            return

        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        course = input("Enter Course: ").strip()

        if not name or not course:
            print("Name and course cannot be empty.")
            return
        if age <= 0:
            print("Age must be greater than zero.")
            return

        students.append({
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        })

        save_students(students)
        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numeric values.")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 65)
    print("STUDENT RECORDS")
    print("=" * 65)

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def update_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to update: "))

        for student in students:
            if student["id"] == student_id:
                name = input(f"New name [{student['name']}]: ").strip()
                age_input = input(f"New age [{student['age']}]: ").strip()
                course = input(f"New course [{student['course']}]: ").strip()

                if name:
                    student["name"] = name
                if age_input:
                    new_age = int(age_input)
                    if new_age <= 0:
                        print("Age must be greater than zero.")
                        return
                    student["age"] = new_age
                if course:
                    student["course"] = course

                save_students(students)
                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid number.")


def delete_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid Student ID.")


def search_student():
    students = load_students()
    keyword = input("Enter name or course to search: ").strip().lower()

    results = [
        student for student in students
        if keyword in student["name"].lower()
        or keyword in student["course"].lower()
    ]

    if not results:
        print("No matching students found.")
        return

    for student in results:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Thank you for using the Student Record Management System!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
