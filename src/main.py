from src.models.student import Student
from src.services.student_service import StudentService
from src.utils.logger import setup_logging

setup_logging()
service = StudentService("data/students.json")


def ask_for_id(prompt):
    """Ask for a student ID. Returns an int, or None if it isn't a number."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Student ID must be a number.")
        return None


def display_students():
    students = service.get_all_students()
    if not students:
        print("No students found.")
        return

    for student in students:
        print()
        print(f"Name: {student.name}")
        print(f"ID: {student.student_id}")
        print(f"Course: {student.course}")
        print(f"Campus: {student.campus}")
        print(f"Scholar: {'Yes' if student.scholar else 'No'}")
        print()


def add_student():
    name = input("Enter student name: ")
    student_id = ask_for_id("Enter student ID: ")
    if student_id is None:
        return
    course = input("Enter student course: ")
    campus = input("Enter student campus: ")
    scholar = input("Is the student a scholar? (yes/no): ").strip().lower() in ("yes", "y")

    student = Student(name, student_id, course, campus, scholar)
    if service.add_student(student):
        print(f"Student {name} added successfully.")
    else:
        print(f"A student with ID {student_id} already exists.")


def update_student():
    student_id = ask_for_id("Enter the ID of the student to update: ")
    if student_id is None:
        return

    print("Press Enter to keep the current value.")
    name = input("New name: ").strip() or None
    course = input("New course: ").strip() or None
    campus = input("New campus: ").strip() or None

    scholar_input = input("Scholar? (yes/no): ").strip().lower()
    if scholar_input in ("yes", "y"):
        scholar = True
    elif scholar_input in ("no", "n"):
        scholar = False
    else:
        scholar = None   # blank or unclear: keep current value

    if service.update_student(student_id, name, course, campus, scholar):
        print(f"Student {student_id} updated.")
    else:
        print(f"No student found with ID {student_id}.")


def remove_student():
    student_id = ask_for_id("Enter the ID of the student to remove: ")
    if student_id is None:
        return

    if service.delete_student(student_id):
        print(f"Student with ID {student_id} has been removed.")
    else:
        print(f"No student found with ID {student_id}.")


def main():
    while True:
        print()
        print("STUDENT PROFILE MANAGEMENT")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Remove Student")
        print("5. Exit Program")
        print()
        choice = input("Pick an operation: ")

        if choice == "1":
            display_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please pick a valid operation.")


if __name__ == "__main__":
    main()