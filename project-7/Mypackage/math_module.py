#Mathematical Operation.....

import math 

def math_menu():

    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            
            num = int(input("\nEnter a number: "))
            print("Factorial: " , math.factorial(num))

        elif choice == "2":

            p = float(input("\nEnter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))

            amount = p * ((1 + r / 100) ** t)
            ci = amount - p 

            print("Compound Interest: ", ci)
            print("Total Amount: ", amount)

        elif choice == "3":

            degree = float(input("\nEnter Degree: "))
            print("Sin =", math.sin(math.radians(degree)))
            print("Cos =", math.cos(math.radians(degree)))
            print("Tan =", math.tan(math.radians(degree)))

        elif choice == "4":

            r = float(input("\nEnter Radius: "))
            print("Area =", math.pi * r * r)

        elif choice == "5":

            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    math_menu()