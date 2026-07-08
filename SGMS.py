import os
import math
def percentage(mathematics,physics,english):
    marks_obtained = mathematics + physics + english
    total_marks = 300
    percentage_obtained = (marks_obtained/total_marks)*100
    return percentage_obtained

path = "C:\\abc\\SGMS.txt"
print("====== Student Management System ======")
print("1. add student"
      "\n2. view student"
      "\n3. search student"
      "\n4. delete student"
      "\n5. save data"
      "\n6. exit")
while True:
    choice = input("Enter your choice: ").lower()
    if choice == "1" or choice == "add student":
      student_name = input("Enter student name: ")
      student_age = input("Enter student age: ")
      student_class = input("Enter student class: ")
      mathematics = int(input("Enter mathematics marks: "))
      physics = int(input("Enter physics marks: "))
      english = int(input("Enter english marks: "))
      percentage = percentage(mathematics, physics, english)
    elif choice == "2" or choice == "view student":
        with open(path) as file:
            print(file.read())
    elif choice == "3" or choice == "search student":
        student_name = input("Enter student name: ")
        search_student = student_name
        with open(path) as file:
            content = file.read()
            if search_student in content:
                print(f"Student {student_name} is present in the database")
            else:
                print(f"Student {student_name} is not present in the database")
    elif choice == "4" or choice == "delete student":
        student_name = input("Enter student name: ")
        delete_student = student_name
        with open(path) as file:
            content = file.read()
            if student_name in content:
                with open(path,'w') :
                    file.write(" ")






