# diary_app.py

import os

def display_menu():
    print("\nDiary Application")
    print("1. Add a new diary entry")
    print("2. View all diary entries")
    print("3. Search for an entry by date")
    print("4. Delete an entry by date")
    print("5. Exit")

def add_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    entry = input("Enter your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(f"{date}\n{entry}\n---\n")
    print(f"Entry for {date} added successfully.")

def view_entries():
    if not os.path.exists("diary.txt"):
        print("No diary entries found.")
        return

    print("\nAll Diary Entries:")
    with open("diary.txt", "r") as file:
        entries = file.read()
        if entries:
            print(entries)
        else:
            print("No diary entries found.")

def search_entry():
    search_date = input("Enter the date to search (YYYY-MM-DD): ")
    if not os.path.exists("diary.txt"):
        print("No diary entries found.")
        return

    with open("diary.txt", "r") as file:
        entries = file.read().split('---\n')
        found = False
        for entry in entries:
            if entry.startswith(search_date):
                print(f"\nEntry for {search_date}:\n{entry}")
                found = True
                break
        if not found:
            print(f"No entry found for the date {search_date}.")

def delete_entry():
    delete_date = input("Enter the date to delete (YYYY-MM-DD): ")
    if not os.path.exists("diary.txt"):
        print("No diary entries found.")
        return

    with open("diary.txt", "r") as file:
        entries = file.read().split('---\n')
    with open("diary.txt", "w") as file:
        found = False
        for entry in entries:
            if entry.startswith(delete_date):
                found = True
                continue
            file.write(entry + '---\n')
        if found:
            print(f"Entry for {delete_date} deleted successfully.")
        else:
            print(f"No entry found for the date {delete_date}.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting the Diary Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
