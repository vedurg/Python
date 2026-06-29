#Random Data Generation......

import random
import string

def random_menu():

    while True:

        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            
            num = random.randint(1,100)
            print("\nRandom Number: ",num)

        elif choice == "2":

            random_list = [random.randint(1,1000) for i in range(5)]
            print("\nRandom List: ",random_list)

        elif choice == "3":
            
            length = int(input("\nEnter password length: "))
            password = ""

            for i in range(length):
                password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12534849607@!*&#")

            print("Generated Password: ", password)
        
        elif choice == "4":

            otp = random.randint(100000,999999)
            print("Generated OTP: ",otp)

        elif choice == "5":

            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    random_menu()




