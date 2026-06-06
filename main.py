from Operations import *

while True:

    print("\n")
    print("=" * 40)
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")