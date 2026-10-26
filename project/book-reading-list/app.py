books = []

while True:
    print("\n--- Book Reading List ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Mark as Read")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()

        if title:
            books.append({"title": title, "read": False})
            print("Book added!")
        else:
            print("Book title cannot be empty.")

    elif choice == "2":
        if not books:
            print("No books added yet.")
        for i, book in enumerate(books, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} - {status}")

    elif choice == "3":
        try:
            number = int(input("Book number: "))
            if 1 <= number <= len(books):
                books[number - 1]["read"] = True
                print("Book marked as read!")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            number = int(input("Book number to remove: "))
            if 1 <= number <= len(books):
                removed = books.pop(number - 1)
                print(f"Removed: {removed['title']}")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")