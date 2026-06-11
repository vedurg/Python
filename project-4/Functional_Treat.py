"""Data Analyzer and Transformer program """

arr = []

print("\nWelcome to the Data Analyzer and Transformer Program")

def input_data():
    """Input Dataset"""

    global arr
    arr = [int(i)for i in input("\nEnter data for 1D array(separated by spaces):\n").split()]
    print("\nData has been stored successfully!")


def data_summary():
    """Display Data Summary"""

    if len(arr) == 0:
        print("\nPlease input data first!")

    else:
        print("\nData Summary:")
        print("- Total elements: ", len(arr))
        print("- Minimum value: ", min(arr))
        print("- Maximum value: ", max(arr))
        print("- Sum of all value: ", sum(arr))
        print(f"- Average value: {sum(arr) / len(arr):.2f}")


def fact(n):
    """Calculate Factorial Using Recursion"""

    if n <= 1:
        return 1

    return n * fact(n-1)


def filter_data():
    """Filter Data Using Lambda Function"""

    if len(arr) == 0:
        print("\nPlease input data first!")

    else:
        val = int(input("\nEnter a threshold value to filter out data above this value:\n"))

        filter_list = list(filter(lambda x : x >= val, arr))
        print(f"\nFiltered Data (values >= {val}):")
        print(filter_list)


def sort_data():
    """Sort Dataset"""

    if len(arr) == 0:
        print("\nPlease input data first!")

    else:
        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        subchoice = int(input("\nEnter your choice: "))

        if subchoice==1:
            arr.sort()
            print("\nSorted Data in Ascending Order:")
            print(arr)

        elif subchoice==2:
            arr.sort(reverse=True)
            print("\nSorted Data in Descending Order:")
            print(arr)

        else:
            print("Invalid choice!")

def statistics():
    """Dataset Statistics"""

    if len(arr) == 0:
            print("\nPlease input data first!")

    else:
        minimum = min(arr)
        maximum = max(arr)
        total = sum(arr)
        average = total / len(arr)

        print("\nDataset Statistics:")
        print("- Minimum value: ", minimum)
        print("- Maximum value: ", maximum)
        print("- Sum of all value: ", total)
        print(f"- Average value: {average:.2f}")


while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice:"))

    if choice==1:

        input_data()

    elif choice==2:

        data_summary()

    elif choice==3:
        
        num = int(input("\nEnter a number to calculate its factorial: "))
        print(f"\nFactorial of {num} is: {fact(num)}")

    elif choice==4:

        filter_data()

    elif choice==5:
        
        sort_data()

    elif choice==6:
        
        statistics()
        
    elif choice==7:

        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!\n")
        break

    else:
        print("Invalid choice!")




