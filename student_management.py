import csv


def  add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student Name: ")
    age = input("Enter student Age: ")
    course = input("Enter student Course: ")
    email = input("Enter student Email: ")
    phone = input("Enter student Phone: ")

    with open("student.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course, email, phone])

    print("student added successfully!")



def view_students():
    with open("student.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def search_student():
    student_id = input("Enter student ID to search: ")

    with open("student.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == student_id:
                print("student found!")
                print("ID:", row["ID"])
                print("Name:", row["Name"])
                print("Age:", row["Age"])
                print("Course:", row["Course"])
                print("Email:", row["Email"])
                print("Phone:", row["Phone"])
                return
        print("student not found!")


def update_student():
    update_id = input("Enter student ID to update: ")

    students = []

    with open("student.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["ID"] == update_id:
                print("student found!")

                student["Name"] = input("Enter new Name: ")
                student["Age"] = input("Enter new Age: ")
                student["Course"] = input("Enter new Course: ")
                student["Email"] = input("Enter new Email: ")
                student["Phone"] = input("Enter new Phone: ")

                print("student updated successfully!")

            students.append(student)

    with open("student.csv", "w", newline="") as file:
        fieldnames = ["ID", "Name", "Age", "Course", "Email", "Phone"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def delete_student():
    delete_id = input("Enter student ID to delete: ")

    students = []
    found = False

    with open("student.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["ID"] == delete_id:
                found = True
                print("student found!")
                print("ID:", student["ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])
                print("Email:", student["Email"])
                print("Phone:", student["Phone"])
            else:
                students.append(student)

    if not found:
        print("student not found!")



while True:
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice! Please try again.")