#OOP Wrapper

print("\n--- Python OOP Project: Employee Management System ---")

class Employee:
    def __init__(self,emp_id,name,age,salary):
        self._emp_id = emp_id
        self.name = name
        self.age = age
        self._salary = 20000

    def setter(self,emp_id,salary):
        self._emp_id = emp_id
        self._salary = salary

    def get_emp_id(self):
        return self._emp_id

    def get_salary(self):
        return self._salary

    def display(self):
        print("\nEmployee Details:")
        print("Employee Id :", self._emp_id)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self._salary)

    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self,emp_id,name,age,salary,department):
        super().__init__(emp_id,name,age,salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Manager Id :", self._emp_id)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self._salary)
        print("Department :", self.department)

class Developer(Employee):
    def __init__(self,emp_id,name,age,salary,language):
        super().__init__(emp_id,name,age,salary)
        self.language = language

    def display(self):
        print("\nDeveloper Details:")
        print("Developer Id :", self._emp_id)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self._salary)
        print("Programming Language :", self.language)

eobj = None
mobj = None
dobj = None

while True:
    
    print("\nChoose an operation:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice==1:
        
        emp_id = input("\nEnter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))

        eobj = Employee(emp_id,name,age,salary)

        print(f"\nEmployee created with ID: {eobj.get_emp_id()}, Name: {eobj.name}, Age: {eobj.age}, Salary: ${eobj.get_salary()}.")

        print("\n--- Choose another operation ---")

    elif choice==2:

        emp_id = input("\nEnter Manager ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        department = input("Enter Department: ")

        mobj = Manager(emp_id,name,age,salary,department)

        print(f"\nManager created with ID: {mobj.get_emp_id()}, Name: {mobj.name}, Age: {mobj.age}, Salary: ${mobj.get_salary()}, And Department: {mobj.department}.")

        print("\n--- Choose another operation ---")

    elif choice==3:

        emp_id = input("\nEnter Developer ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        dobj = Developer(emp_id,name,age,salary,language)

        print(f"\nDeveloper created with ID: {dobj.get_emp_id()}, Name: {dobj.name}, Age: {dobj.age}, Salary: ${dobj.get_salary()}, And Programming Language: {dobj.language}.")

        print("\n--- Choose another operation ---")

    elif choice==4:

        print("\nChoose details to show:")
        print("1. Employee")
        print("2. Manager")
        print("3. Developer")

        ch = int(input("Enter your choice: "))

        if ch==1:
            if eobj:
                eobj.display()
            else:
                print("\nEmployee not created")
        
        elif ch==2:
            if mobj:
                mobj.display()
            else:
                print("\nManager not created")

        elif ch==3:
            if dobj:
                dobj.display()
            else:
                print("\nDeveloper not created")
        
        else:
            print("Invalid choice !")

        print("\n--- Choose another operation ---")

    elif choice==5:

        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!\n")
        break

    else:
        print("Invalid choice !")

    

