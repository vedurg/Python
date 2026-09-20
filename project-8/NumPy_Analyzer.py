# Project 8........................

# Array Creation

import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def array_menu(self):

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            elements = input("\nEnter elements for the array separated by space: ")

            values = list(map(int,elements.split()))
            self.array = np.array(values)

        elif choice == "2":

            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            elements = input(f"Enter {rows * columns} elements for the array separated by space: ")

            values = list(map(int,elements.split()))
            self.array = np.array(values).reshape(rows,columns)
            
        elif choice == "3":

            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            elements = input(
                f"Enter {layers*rows*columns} elements for the array separated by space: ")

            values = list(map(int,elements.split()))
            self.array = np.array(values).reshape(layers,rows,columns)

        else :

            print("Invalid choice")
            return

        print("\nArray created successfully:")
        print(self.array)

# Indexing and Slicing.....................

        while True:

            print("\nChoose an operation: ")
            print("1.Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("\nEnter your choice: ")

    # Indexing......

            if choice == "1":

                if self.array.ndim == 1:

                    index = int(input("\nEnter the index: "))

                    if index < -len(self.array) or index >= len(self.array):
                        print("\nInvalid index")

                    else:
                        print("\nElement: ")
                        print(self.array[index])

                elif self.array.ndim == 2:

                    row = int(input("\nEnter the row index: "))
                    column = int(input("Enter the column index: "))

                    if row < -self.array.shape[0] or row >= self.array.shape[0]:
                        print("\nInvalid row index.")

                    elif column < -self.array.shape[1] or column >= self.array.shape[1]:
                        print("\nInvalid column index.")

                    else:
                        print("\nElement: ")
                        print(self.array[row,column])

                else:

                    layer = int(input("\nEnter the layer index: "))
                    row = int(input("Enter the row index: "))
                    column = int(input("Enter the column index: "))

                    if layer < -self.array.shape[0] or layer >= self.array.shape[0]:
                        print("\nInvalid layer index.")

                    elif row < -self.array.shape[1] or row >= self.array.shape[1]:
                        print("\nInvalid row index.")

                    elif column < -self.array.shape[2] or column >= self.array.shape[2]:
                        print("\nInvalid column index.")

                    else:
                        print("\nElement: ")
                        print(self.array[layer,row,column])

     # Slicing

            elif choice == "2":

                if self.array.ndim == 1:

                    range_value = input("\nEnter the range (start:end): ")

                    start,end = map(int,range_value.split(":"))
                    result = self.array[start:end]

                elif self.array.ndim == 2:

                    row_range = input("\nEnter the row range (start:end): ")
                    column_range = input("Enter the column range (start:end): ")

                    row_start,row_end = map(int,row_range.split(":"))
                    column_start,column_end = map(int,column_range.split(":"))

                    result = self.array[row_start:row_end,column_start:column_end]

                else:

                    layer_range = input("\nEnter the layer range (start:end): ")
                    row_range = input("Enter the row range (start:end): ")
                    column_range = input("Enter the column range (start:end): ")

                    layer_start,layer_end = map(int,layer_range.split(":"))
                    row_start,row_end = map(int,row_range.split(":"))
                    column_start,column_end = map(int,column_range.split(":"))

                    result = self.array[layer_start:layer_end,
                                            row_start:row_end,
                                            column_start:column_end]

                print("\nSliced Array:")
                print(result)

            elif choice == "3":

                break

            else:

                print("Invalid choice")

 # Mathematical Operation.................

    def mathematical_operations(self):

        if self.array is None:

            print("\nPlease create an array first")
            return 

        print("\nChoose a mathematical operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")

        choice = input("\nEnter your choice: ")

        if choice in["1","2","3","4"]:

            print(f"\nEnter{self.array.size}elements"
                  "for second array separated by space:")

            elements = input()

            values = list(map(int,elements.split()))

            if len(values) != self.array.size:
                print(
                    f"\nPlease enter exactly {self.array.size} elements.")
            
                return

            second_array = np.array(values).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            if choice == "1":

                result = self.array + second_array

                print("\nResult of Addition:")
                print(result)

            elif choice == "2":

                result = self.array - second_array

                print("\nResult of Subtraction:")
                print(result)

            elif choice == "3":

                result = self.array * second_array

                print("\nResult of Multiplication:")
                print(result)

            elif choice == "4":

                result = self.array / second_array

                print("\nResult of Division:")
                print(result)

        elif choice == "5":

            if self.array.ndim !=2:

                print("\nDot product requires a 2D array ")

                return
                
            columns = self.array.shape[1]

            elements = input(f"Enter{columns} elements for second array: ")

            values = list(map(int,elements.split()))


            if len(values) != columns:
                print(
                    f"\nPlease enter exactly {columns} elements.")
            
                return

            second_array = np.array(values).reshape(columns,1)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            result = np.dot(self.array,second_array)

            print("\nResult of Dot Product:")
            print(result)

        else:

            print("Invalid choice")

# Combine or split array

    def combine_split_arrays(self):

        if self.array is None:

            print("\nPlease create an array first")
            return

        print("\nChoose an Combine or Split Arrays: ")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            elements = input(f"\nEnter the elements of another array to combine"
                              "separated by space:")

            values = list(map(int,elements.split()))
            
            if len(values) != self.array.size:
                print(f"\nPlease enter exactly {self.array.size} elements.")
                return
                             
            second_array = np.array(values).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            result = np.concatenate((self.array,second_array))

            print("\nCombined Array:")
            print(result)

        elif choice == "2":

            splits = int(input("\nEnter number of splits: "))
            result = np.array_split(self.array,splits)

            print("\nSplit Array:")

            for i ,array in enumerate(result,1):

                print(f"\nArray {i}:")
                print(array)

        else:

            print("Invalid choice")

# Search,Sort and Filter

    def search_sort_filter(self):

        if self.array is None:

            print("\nPlease create an array first")
            return

        print("\nSearch, Sort, or Filter Arrays: ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            value = int(input("\nEnter the value to search: "))
            result = np.where(self.array == value)

            print("\nValue found at index:")
            print(result[0])


        elif choice == "2":

            print("\nOriginal Array:")
            print(self.array)

            result = np.sort(self.array)

            print("\nSorted Array:")
            print(result)

        elif choice == "3":

            value = int(input("\nEnter the minimum value: "))

            result = self.array[self.array > value]

            print("\nFiltered Values:")
            print(result)

        else:

            print("Invalid choice")

# Aggregates And Statistics

    def aggregates_statistics(self):

        if self.array is None: 

            print("\nPlease create an array first.")
            return
        
        while True:  

            print("\nChoose an Aggregate/Statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentile")
            print("9. Correlation")
            print("10. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                print("\nSum of Array:", np.sum(self.array))

            elif choice == "2":

                print("\nMean of Array:",np.mean(self.array))

            elif choice == "3":

                print("\nMedian of Array:",np.median(self.array))

            elif choice == "4":

                print("\nStandard Deviation:",np.std(self.array))

            elif choice == "5":

                print("\nVariance:",np.var(self.array))

            elif choice == "6":

                print("\nMinimum:",np.min(self.array))

            elif choice == "7":

                print("\nMaximum:",np.max(self.array))

            elif choice == "8":

                percentile = float(input("Enter percentile (0-100):"))
                result = np.percentile(self.array,percentile)
                print(f"\n{percentile}th Percentile:", result)

            elif choice == "9":

                if self.array.ndim !=1:

                    print("\nCorrelation requires a 1D array")
                    continue
            
                elements = input(f"\nEnter {self.array.size} elements"
                             "for second array separated by space:")

                values = list(map(int,elements.split()))

                second_array = np.array(values)

                result = np.corrcoef(self.array,second_array)

                print("\nCorrelation Matrix:")
                print(result)

            elif choice == "10":
                break

            else:

                print("Invalid choice")

# Main Program................................ 
            
analyzer = DataAnalytics()

print("\nWelcome to the NumPy Analyzer!")
print("=============================================")

while True:

    print("\nChoose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    choice = input("\nEnter Your choice: ")

    if choice == "1":

        analyzer.array_menu()

    elif choice == "2":

        analyzer.mathematical_operations()

    elif choice == "3":

        analyzer.combine_split_arrays()

    elif choice == "4":

        analyzer.search_sort_filter()

    elif choice =="5":

        analyzer.aggregates_statistics()

    elif choice == "6":

        print("\nThank you for using the Numpy Analyzer! Goodbye!\n")
        break

    else:

        print("\nInvalid choice. Please try again")