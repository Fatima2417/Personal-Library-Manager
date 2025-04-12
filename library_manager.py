import os
import json

# File to save and load library data here 
library_file = "library.txt"   

# load the library from file if it exists in the data
def load_library(): 
    if os.path.exists(library_file):
        with open(library_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# here i save the library to a file
def save_library(library):
    with open(library_file, "w") as file:
        json.dump(library, file, indent=4)

# for add a new book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year. Try again.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("Book added successfully!")

# for remove a book from the library by its title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# for search a book by title or author
def search_book(library):         
    print("Search by: \n1. Title \n2. Author")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_title = input("Enter the title: ").strip().lower()
        matches = [book for book in library if search_title in book['title'].lower()]
    elif choice == "2":
        search_author = input("Enter the author: ").strip().lower()
        matches = [book for book in library if search_author in book['author'].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):
            read_status = "Read" if book['read'] else "Unread"
            print(f"{idx}-> {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# for displaying all books in the library
def display_all_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            read_status = "Read" if book['read'] else "Unread"
            print(f"{idx}-> {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# display library statistics here
def display_statistics(library):
    total = len(library)
    read_count = sum(1 for book in library if book['read'])
    percentage_read = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage_read:.1f}%")
      
      
# Show the main menu to choose
def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")     
    print("2. Remove a book") 
    print("3. Search for a book") 
    print("4. Display all books")  
    print("5. Display statistics")
    print("6. Exit")

def main():
    library = load_library()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice!! Please try again.")

if __name__ == "__main__":
    main()
