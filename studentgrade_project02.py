#open a  dictionary
student_grade={}



#fuctions for execute your choice
def add_student(name, marks):
    student_grade[name]=marks
    print(f"New students {name}has been added!")

def update_student(name,marks):
    if name in student_grade:
        student_grade[name]=marks
        print(f"{name}'s Grade has been updated")
    else:
        print("Name not found")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print("Student name deleted")
    else:
        print("Name not found")

def view_student():
    if student_grade:
        for name , marks in student_grade.items():
            print(f"{name} : {marks}")

    else:
        print("No student found")
    
#main part
def main():
    while True:
        print("\n\n\n{{{{{{{{Welcome to GRADELIST}}}}}}}}")
        print("\n1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit\n")

        number = int(input('Enter your choice: '))


        if number == 1:
            name = input("Enter student name: ")
            marks = int(input("Enter grade: "))
            add_student(name,marks)
        elif number == 2:
            name = input("Enter student name: ")
            marks = int(input("Enter grade: "))
            update_student(name,marks)
        elif number == 3:
            name = input('Enter student name: ')
            delete_student(name)

        elif number ==4:
            view_student()

        elif number ==5:
            print("Closing program........")
            break
        else:
            print("Invalid choice")



    
if __name__ == "__main__":
    main()




    
   
    

 
