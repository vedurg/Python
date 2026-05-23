print("Welcome to the Pattern Generator and Number Analyzer!")

while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            print("\nPattern Menu")
            print("1.Right-angled Triangle")
            print("2.Left-angled Triangle")
            print("3.Full Triangle")

            subchoice = int(input("\nEnter your pattern choice:"))

            match subchoice:
                case 1:
                    print("\nRight-angled Triangle")
                    rows = int(input("Enter the number of rows for the pattern:"))
            
                    for i in range(1 , rows + 1):
                        print("*" *i)

                case 2:  
                    print("\nLeft-angled Triangle")
                    rows = int(input("Enter the number of rows for the pattern:"))
            
                    for i in range(1 , rows + 1):
                        print(" " * (rows - i) + "*" * i)   

                case 3:  
                    print("\nFull Triangle")
                    rows = int(input("Enter the number of rows for the pattern:"))
            
                    for i in range(1 , rows + 1):
                        print(" " * (rows - i) + "*" * (2 * i -1))      
   
        case 2:
            start = int(input("\nEnter the start of range:"))
            end = int(input("Enter the end of range:"))

            total = 0
            count = 0
            for i in range(start , end+1):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                total += i
                count += 1  
            print(f"\nSum of all numbers from {start} to {end} is: {total}")
            print(f"Average of all number from {start} to {end} is: {total / count}")

        case 3:
            print(f"\nExiting the program. Goodbye!")
            break