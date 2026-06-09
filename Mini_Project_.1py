import pandas as pd
import os

class Student:
    def __init__(self, name, age, course, student_id):
        self.name = name
        self.age = age
        self.course = course
        self.student_id = student_id

    def display_info(self):
        print("\nStudent Details:")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Student ID : {self.student_id}")


def save_data(students):
    data = []

    for student in students:
        data.append({
            "Name": student.name,
            "Age": student.age,
            "Course": student.course,
            "Student ID": student.student_id
        })

    pd.DataFrame(data).to_csv("data.csv", index=False)


def load_data():
    students = []

    if os.path.exists("data.csv"):
        df = pd.read_csv("data.csv")

        for _, row in df.iterrows():
            students.append(
                Student(
                    str(row["Name"]),
                    str(row["Age"]),
                    str(row["Course"]),
                    str(row["Student ID"])
                )
            )

    return students


students = load_data()

print("===== Welcome to Student Management System =====")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Show All Students")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            student_id = input("Enter Student ID: ")

            if student_id in [s.student_id for s in students]:
                print("Student ID already exists!")
                continue

            students.append(Student(name, age, course, student_id))
            save_data(students)

            print("Student Added Successfully!")

        case '2':
            student_id = input("Enter Student ID to Search: ")

            found = False

            for student in students:
                if student.student_id == student_id:
                    print("\nStudent Found!")
                    student.display_info()
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        case '3':
            student_id = input("Enter Student ID to Update: ")

            found = False

            for student in students:
                if student.student_id == student_id:

                    print("\nEnter New Details")
                    student.name = input("Enter New Name: ")
                    student.age = input("Enter New Age: ")
                    student.course = input("Enter New Course: ")

                    save_data(students)

                    print("Student Updated Successfully!")
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        case '4':
            if not students:
                print("No Students Found!")

            else:
                data = []

                for student in students:
                    data.append({
                        "Name": student.name,
                        "Age": student.age,
                        "Course": student.course,
                        "Student ID": student.student_id
                    })

                df = pd.DataFrame(data)

                print("\n===== All Students =====")
                print(df.to_string(index=False))

        case '5':
            student_id = input("Enter Student ID to Delete: ")

            found = False

            for student in students:
                if student.student_id == student_id:
                    students.remove(student)

                    save_data(students)

                    print("Student Deleted Successfully!")
                    found = True
                    break

            if not found:
                print("Student Not Found!")

        case '6':
            print("Exiting Student Management System...")
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice! Please Try Again.")