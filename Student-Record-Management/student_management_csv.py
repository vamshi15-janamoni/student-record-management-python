import csv
import os

CSV_FILE = "students.csv"
FIELDS = ["id", "name", "age", "course"]


def load_students():
    if not os.path.exists(CSV_FILE):
        return []

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except OSError as error:
        print(f"File error: {error}")
        return []


def save_students(students):
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)
    except OSError as error:
        print(f"Unable to save records: {error}")


def add_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID: "))

        if any(int(s["id"]) == student_id for s in students):
            print("Student ID already exists.")
            return

        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        course = input("Enter Course: ").strip()

        if not name or not course or age <= 0:
            print("Please enter valid student details.")
            return

        students.append({
            "id": str(student_id),
            "name": name,
            "age": str(age),
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
            if int(student["id"]) == student_id:
                name = input(f"New name [{student['name']}]: ").strip()
                age = input(f"New age [{student['age']}]: ").strip()
                course = input(f"New course [{student['course']}]: ").strip()

                if name:
                    student["name"] = name
                if age:
                    student["age"] = str(int(age))
                if course:
                    student["course"] = course

                save_students(students)
                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter valid values.")


def delete_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        updated = [s for s in students if int(s["id"]) != student_id]

        if len(updated) == len(students):
            print("Student not found.")
            return

        save_students(updated)
        print("Student deleted successfully.")

    except ValueError:
        print("Please enter a valid Student ID.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM (CSV) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

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
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
