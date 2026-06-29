#Datetime and Time Operation

from datetime import datetime

import time

def datetime_menu():

    while True:
        
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nCurrent Date and Time: ", datetime.now())

        elif choice == "2":

            date1 = input("\nEnter the first date(DD-MM-YYYY): ")
            date2 = input("Enter the second date(DD-MM-YYYY): ")
            
            d1 = datetime.strptime(date1, "%d-%m-%Y")
            d2 = datetime.strptime(date2, "%d-%m-%Y")

            print("\nDifference: ", abs((d2-d1).days), "days")

        elif choice == "3":

            print("\nFormatted Data and Time:")
            print(datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))

        elif choice == "4":
            
            sec = int(input("Enter Seconds: "))
            print("Stopwatch Started")
            for i in range(sec):
                print(i+1)
                time.sleep(1)

        elif choice == "5":

            sec = int(input("Enter Seconds: "))
            
            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1
            print("Time's Up!")

        elif choice == "6":

            break

        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    datetime_menu()