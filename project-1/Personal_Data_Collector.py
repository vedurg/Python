#Personal Data Collector

print("Welcome to the interctive personal data collector!\n")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
number = int(input("Enter your favourite number: "))


print("\nThank you! Here is the information we collected:\n")

print("Name:" , name , "(Type:", type(name), ", Memory Address:", id(name),")")
print("Age:" , age , "(Type:", type(age), ", Memory Address:", id(age),")")
print("Height:" , height , "(Type:", type(height), ", Memory Address:", id(height),")")
print("Favourite Number:" , number , "(Type:", type(number), ", Memory Address:", id(number),")")

current_year = 2026
birth_year = current_year - age

print("\nYour birth year is approximately:", birth_year, "(based on your age of", age,")")

print("\nThank you for using the Personal Data Collector. Goodbye!")



