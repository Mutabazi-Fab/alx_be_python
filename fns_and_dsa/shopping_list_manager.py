# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("\nThe shopping list is currently empty.")

def main():
    shopping_list = []  # Implementation of an array shopping_list
    while True:
        display_menu()  # Calling display_menu function
        try:
            choice = int(input("Choose an option (1-4): "))  # Choice input as a number
            if choice == 1:
                add_item(shopping_list)
            elif choice == 2:
                remove_item(shopping_list)
            elif choice == 3:
                view_list(shopping_list)
            elif choice == 4:
                print("Exiting the shopping list manager.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
