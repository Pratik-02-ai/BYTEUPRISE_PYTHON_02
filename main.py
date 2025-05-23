# LIBRARY MANAGEMENT SYSTEM task_02

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "available": True
            }
            print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nLibrary Books:")
        for book_id, info in self.books.items():
            status = "Available" if info["available"] else "Borrowed"
            print(f"ID: {book_id} | Title: {info['title']} | Author: {info['author']} | Status: {status}")

    def borrow_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["available"]:
                self.books[book_id]["available"] = False
                print(f"You have borrowed '{self.books[book_id]['title']}'.")
            else:
                print("Book is currently not available.")
        else:
            print("Book ID not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]["available"]:
                self.books[book_id]["available"] = True
                print(f"Thank you for returning '{self.books[book_id]['title']}'.")
            else:
                print("This book was not borrowed.")
        else:
            print("Book ID not found.")

# Main program
def main():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            lib.add_book(book_id, title, author)

        elif choice == '2':
            lib.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to borrow: ")
            lib.borrow_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            lib.return_book(book_id)

        elif choice == '5':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
