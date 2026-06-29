#File Operation....

def file_menu():

    while True:

        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            name = input("\nEnter file name: ")

            file = open(name , "w")
            file.close()

            print("File created successfully!")

        elif choice == "2":

           name = input("\nEnter file name: ")
           data = input("Enter data to write: ")

           file = open(name , "w")
           file.write(data)
           file.close()

           print("Data written successfully!")

        elif choice == "3":

            name = input("\nEnter file name: ")

            file = open(name , "r")
            print("\nFile Content:")
            print(file.read())
            file.close()

        elif choice == "4":

            name = input("\nEnter file name: ")
            data = input("Enter data to append: ")

            file = open(name , "a")
            file.write("\n" + data)
            file.close()

            print("Data appended successfully!")

        elif choice == "5":

            break

        else:
            
            print("Invalid choice!")

if __name__ == "__main__":
    file_menu()

        