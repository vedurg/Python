#Main file.....

from Mypackage.datetime_module import datetime_menu
from Mypackage.math_module import math_menu
from Mypackage.random_module import random_menu
from Mypackage.uuid_module import uuid_menu
from Mypackage.file_module import file_menu
from Mypackage.dir_module import dir_menu

while True:

    print("\n===============================")
    print("Welcome to Multi-Utility Toolkit")
    print("===============================")
    print("\nChoose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("================================")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        datetime_menu()
 
    elif choice == "2":
        math_menu()

    elif choice == "3":
        random_menu()

    elif choice == "4":
        uuid_menu()

    elif choice == "5":
        file_menu()

    elif choice == "6":
        dir_menu()

    elif choice == "7":
        print("\n================================")
        print("Thank you for using the Multi-Utility Toolkit!")
        print("================================\n")
        break

    else:
        print("Invalid choice!")