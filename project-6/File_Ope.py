#File Operator

print("\nWelcome to Personal Journal Manager!")

class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("\nEnter your journal entry with current Date and Time:\n")

        date_str = input("Enter Current Date: ")
        time_str = input("Enter Current Time: ")

        file = open(self.filename, "a")
        file.write("----------------------------\n")
        file.write("Date: " + date_str + "\n")
        file.write("Time: " + time_str + "\n")
        file.write(entry + "\n\n")
        file.close()

        print("\nEntry added successfully!")

    def view_entry(self):
        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if content.strip() == "":
                print("Output (If the file does not exist):")
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nOutput (If the file exists):")
                print("Your Journal Entries:")
                print(content)

        except FileNotFoundError:
            print("\nOutput:")
            print("Error: The journal file does not exist. Please add a new entry first.")

    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").lower()

        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if keyword in content.lower():
                print("\nOutput (If a match is found):")
                print("Matching Entries:")
                print("-----------------------------")
                
                for line in content.split("\n"):
                    if keyword in line.lower():
                        print(line)
                        
            else:
                print("\nOutput (If no match is found):")
                print("No entries were found for the keyword:", keyword)

        except FileNotFoundError:
            print("\nOutput (If the file does not exist):")
            print("No journal entries found. Start by adding a new entry!")

    def delete_entry(self):
        
        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").lower()

        if confirm == "yes":
            try:
                file = open(self.filename, "w")
                file.close()

                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")

            except FileNotFoundError:
                print("\nOutput (If the file does not exist):")
                print("No journal entries to delete.")
        else:
            print("Deletion Cancelled!")


jobj = JournalManager()

while True:

    print("\nPlease select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = int(input("\nUser Input:\n"))

    if choice==1:
        jobj.add_entry()

    elif choice==2:
        jobj.view_entry()

    elif choice==3:
        jobj.search_entry()

    elif choice==4:
        jobj.delete_entry()

    elif choice==5:
        print("\nOutput:")
        print("Thank you for using Personal Journal Manager. Goodbye!\n")
        break

    else:
        print("\nOutput:")
        print("Invalid option. Please select a valid option from the menu.")



