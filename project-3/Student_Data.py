#Collection Manipulator.....

students = []
subjects_set = set()

print("\nWelcome to the Student Data Oraganizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student Data")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        print("\nEnter student details:")
        student = {
            "stid" : int(input("Enter student ID: ")),
            "student_tuple" : ("stid",),
            "name" : input("Name: "),
            "age" : int(input("Age: ")),
            "grade" : input("Grade: "),
            "subjects" : input("Subjects: ").split(",")
        }
        students.append(student)

        for sub in student["subjects"] :
            subjects_set.add(sub)

        print("\n--Student added successfully!--")
    
    elif choice==2:
        print("\n---Display All Students---")

        for student in students:
            subjects_str = ", ".join(student['subjects'])

            print(f"Student ID: {student['stid']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {subjects_str}")
        
    elif choice==3:
        stid = int(input("\nEnter Student ID To Update: "))
        for student in students:
            if student["stid"]==stid:
                student['name'] = input("Enter new student name: ")
                student['age'] = int(input("Enter new student age: "))
                student['grade'] = input("Enter new student grade: ")
                student['subjects'] = input("Enter new student subjects: ").split(",")

                print("\n--Student Updated Successfully!--")
                break
        else:
            print("Student ID is Not Found")

    elif choice==4:
        stid = int(input("\nEnter Student ID To Delete Record: "))
        for student in students:
            if student["stid"]==stid:
                students.remove(student)
                print("\n--Student Record Delete Successfully!--")
                break
        else:
            print("Student ID is Not Found")

    elif choice==5:
        print("\n--Display Subjects Offered--")

        unique_subjects = set()

        for student in students:
            for sub in student['subjects']:
                unique_subjects.add(sub.strip().title())
        
        print(", ".join(unique_subjects))

    elif choice==6:
        print("\nThank you for using the Student Data Organizer!")
        print("Goodbye! Have a great day.\n")
        break

    else:
        print("Invalid Choice!")

   
        




    