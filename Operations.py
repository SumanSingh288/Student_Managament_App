import json

FILE_NAME = "Students.json"


def load_students():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def view_students():
    students = load_students()

    print("\nSTUDENT RECORDS")
    print("-" * 60)

    for student in students:
        print(
            f"ID:{student['id']} | "
            f"Name:{student['name']} | "
            f"Age:{student['age']} | "
            f"Subject:{student['subject']} | "
            f"Marks:{student['marks']}"
        )


def add_student():
    students = load_students()

    new_student = {
        "id": int(input("Enter ID: ")),
        "name": input("Enter Name: "),
        "age": int(input("Enter Age: ")),
        "subject": input("Enter Subject: "),
        "marks": int(input("Enter Marks: "))
    }

    students.append(new_student)
    save_students(students)

    print("Student Added Successfully")


def search_student():
    sid = int(input("Enter Student ID: "))

    students = load_students()

    for student in students:
        if student["id"] == sid:
            print(student)
            return

    print("Student Not Found")


def update_student():
    sid = int(input("Enter Student ID: "))

    students = load_students()

    for student in students:
        if student["id"] == sid:
            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["subject"] = input("New Subject: ")
            student["marks"] = int(input("New Marks: "))

            save_students(students)

            print("Record Updated")
            return

    print("Student Not Found")


def delete_student():
    sid = int(input("Enter Student ID: "))

    students = load_students()

    for student in students:
        if student["id"] == sid:
            students.remove(student)

            save_students(students)

            print("Record Deleted")
            return

    print("Student Not Found")