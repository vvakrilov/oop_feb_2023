from typing import List
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List = []
        self.books_available: dict = {}  # authors (key: str) & the books available for each of the authors ([*] of str)
        self.rented_books: dict = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if [book_name in b for b in self.rented_books]:
            return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

        if author in self.books_available:
            if book_name in self.books_available[author]:
                book_index = self.books_available[author].index(book_name)
                self.books_available[author].pop(book_index)
                self.rented_books[user.username] = {book_name: days_to_return}
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        if author in self.rented_books:
            del self.rented_books[author]

        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)

        user.books.remove(book_name)
