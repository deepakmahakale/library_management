from models.active_model import ActiveModel
from models.book import Book

class Member(ActiveModel):
    def __init__(self, name, record_id = None):
        self.id = record_id
        self.name = name

    def books(self):
        collection = []
        with open('db/member_books.txt') as file:
            for line in file:
                if line.startswith(f"{self.id},"):
                    book = Book.find(line.strip().split(',')[-1])
                    if book:
                        collection.append(book)
        return collection

    def assign_book(self, book_id):
        book = Book.find(book_id)
        if not book:
            return "Record not found"
        with open('db/member_books.txt', 'r+') as file:
            for line in file:
                if line.startswith(f"{self.id},{book_id}"):
                    print('Already assigned')
                    return
            file.write(f"{self.id},{book_id}\n")
        book.available -= 1
        book.save

