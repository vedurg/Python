#Explore Module Attributes(dir())

import datetime
import math
import random
import uuid
from Mypackage import file_module

def dir_menu():

    print("\nExplore Module Attributes:")

    module = input("Enter module name to explore: ").lower()

    if module == "datetime":
        print("\nAvailable Attributes in datetime module:")
        print(dir(datetime))

    elif module == "math":
        print("\nAvailable Attributes in math module:")
        print(dir(math))

    elif module == "random":
        print("\nAvailable Attributes in random module:")
        print(dir(random))

    elif module == "uuid":
        print("\nAvailable Attributes in uuid module:")
        print(dir(uuid))

    elif module == "file":
        print("\nAvailable Attributes in file module:")
        print(dir(file_module))

    else:
        print("Module not found!")

if __name__ == "__main__":
    dir_menu()
