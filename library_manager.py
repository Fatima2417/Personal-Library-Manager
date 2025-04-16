import json
import os

library = []
file_path = "library.txt"

# Load existing books if file exists
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        library = json.load(file)

def save_library():
    with open(file_path, "w") as file:
        json.dump(library, file, indent=4)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }
    library.append(book)
    print("Book added successfully!\n")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found!\n")

def search_book():
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    keyword = input("Enter the keyword: ").lower()
    found = False
    for book in library:
        if (choice == "1" and keyword in book["Title"].lower()) or \
           (choice == "2" and keyword in book["Author"].lower()):
            print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            found = True
    if not found:
        print("No matching books found.\n")

def display_books():
    if not library:
        print("No books in your library.\n")
        return
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["Read"] else "Unread"
        print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
    print()

def display_stats():
    total = len(library)
    if total == 0:
        print("Library is empty.\n")
        return
    read_count = sum(1 for book in library if book["Read"])
    percent = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Books read: {read_count}")
    print(f"Percentage read: {percent:.2f}%\n")

def main():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
