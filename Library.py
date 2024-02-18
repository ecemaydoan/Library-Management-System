class Library:
    def __init__(self):
        try:
            with open("books.txt", "a+") as f:
                pass 
        except FileNotFoundError:
            print("books.txt not found. Creating a new one.")
            with open("books.txt", "w") as f:
                pass

    def list_books(self):
        
        with open("books.txt", "r") as f:
         books = f.read().splitlines()
        for book in books:
             title, author, release_year, num_pages = book.split(',')
             print(f"Title: {title}, Author: {author}, Release Year: {release_year}, Pages: {num_pages}")
          

    def add_book(self):
        
        book_name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        release_date = input("Enter the release date of the book (YYYY): ")
        num_of_pages = input("Enter the number of pages: ")

        book_info = f"{book_name},{author},{release_date},{num_of_pages}\n"

        with open("books.txt", "a") as f:
            f.write(book_info)

        print("Added the book successfully!")
        print("Here is the new list!")
        self.list_books()

    def remove_book(self):
        
        print("Here is the list of the books:")
        self.list_books()  

        book_title = input("Enter the title of the book to remove: ")

        try:
            with open("books.txt", "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                if not line.startswith(book_title):
                    new_lines.append(line)

            with open("books.txt", "w") as f:
                f.writelines(new_lines)

            print("Book removed successfully.")
            print("Here is the new list!")
            self.list_books()

        except FileNotFoundError:
            print("Error: books.txt not found.")

#Interaction Menu for console
lib = Library()
while True:
        print("*** MENU ***")
        print("\033[1m1) List Books\033[0m")
        print("\033[1m2) Add Book\033[0m")
        print("\033[1m3) Remove Book\033[0m")

        answer = input("Which option would you like to choose? ")

        if answer == "1":
            lib.list_books()
        elif answer == "2":
            lib.add_book()
        elif answer == "3":
            lib.remove_book()
        else:
            print("Invalid option!")

        cont = input(" Is there anything else you want to do? (Yes/No) ").lower()

        if cont not in ("yes","no","Yes","No"):
            print(" !!! INVALID EXPRESSION !!!")
        if cont ==("no"):
            print("Okey, bye!!!")
            break
