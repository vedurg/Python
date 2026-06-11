"""Data Analyzer and Transformer program """

arr = []

print("\nWelcome to the Data Analyzer and Transformer Program")

def statistics(*args, **kwargs):
    """
    Calculate statistical information from a dataset.

    Parameters:
        *args : int
            Dataset values passed as arguments.

        **kwargs : dict
            Optional keyword arguments such as title.

    Example:
        statistics(10, 20, 30, title="Dataset Statistics")
    """
    
    if len(args) == 0:
        return None

    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    if "title" in kwargs:
        print(f"{kwargs['title']}")

    return minimum, maximum, total, average

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

        arr = [int(i)for i in input("\nEnter data for 1D array(separated by spaces):\n").split()]
        print("\nData has been stored successfully!")

    elif choice==2:

        if len(arr) == 0:
            print("Please input data first!")

        else:
            print("\nData Summary:")
            print("- Total elements: ", len(arr))
            print("- Minimum value: ", min(arr))
            print("- Maximum value: ", max(arr))
            print("- Sum of all value: ", sum(arr))
            print(f"- Average value: {sum(arr) / len(arr):.2f}")

    elif choice==3:
        
        def fact(n):
            """
            Calculate factorial of a number using recursion.

                Parameters:
                    n (int): Positive integer.
                 Returns:
                    int: Factorial of n.
            """
            if n <= 1:
                return 1
            return n * fact(n-1)
        num = int(input("\nEnter a number to calculate its factorial: "))
        print(f"\nFactorial of {num} is: {fact(num)}")

    elif choice==4:

        if len(arr) == 0:
            print("Please input data first!")

        else:
            val = int(input("\nEnter a threshold value to filter out data above this value:\n"))

            filter_list = list(filter(lambda x : x >= val, arr))
            print(f"\nFiltered Data (values >= {val}):")
            print(filter_list)

    elif choice==5:
        
        if len(arr) == 0:
            print("Please input data first!")

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

    elif choice==6:
        
        if len(arr) == 0:
            print("Please input data first!")

        else:
            minimum, maximum, total, average = statistics(*arr, title = "\nDataset Statistics:")

            print("- Minimum value: ", minimum)
            print("- Maximum value: ", maximum)
            print("- Sum of all value: ", total)
            print(f"- Average value: {average:.2f}")
        
    elif choice==7:

        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!\n")
        break

    else:
        print("Invalid choice!")




