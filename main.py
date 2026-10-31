
from student import Student
from s_management import StudentManagementSystem
from login import Login
from validation import get_integer, get_marks,get_name,get_course

def main():
    sms = StudentManagementSystem()
    sms.load_students()
    
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student By Roll Number")
        print('4. Search Student By Name')
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Generate Report Card")
        print("8. Sort Students By Marks")
        print("9. Show Student Rankings")
        print("10. Show Class Statistics")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                while True:
                    roll = get_integer("Roll number: ")

                    if sms.roll_exists(roll):
                        print("Roll number already exists! Enter another.")
                    else:
                        break
                age = get_integer('Age: ')

                name = get_name("Name: ")
                course = get_course("Course: ")

                marks = []
                for i in range(3):
                    mark = get_marks(f'Marks for subject {i + 1}: ')

                    marks.append(mark)
                else:
                    student = Student(
                        roll, name, age, course, marks
                    )
                    sms.add_student(student)

            except ValueError:
                print("Please enter valid numeric values.")

        elif choice == '2':
            sms.view_students()

        elif choice == '3':
                roll = get_integer('Enter the roll number: ')
                sms.search_student(roll)

        elif choice == '4':
                    name = get_name('Enter student name: ')
                    sms.search_by_name(name)
        
        elif choice == '5':
                roll = int(input("Enter roll number to update: "))
                sms.update_student(roll)

        elif choice == '6':
                roll = int(input("Enter roll number to delete: "))
                sms.delete_student(roll)

        elif choice == "7":
            roll = get_integer("Enter roll number: ")
            sms.generate_report_card(roll)

        elif choice == '8':
            sms.sort_students_by_marks()

        elif choice == '9':
            sms.show_student_rankings()

        elif choice == '10':
            sms.show_class_statistics()

        elif choice == '11':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    user = Login()

    if user.login():
        main()
    else:
        print("Access denied!")
