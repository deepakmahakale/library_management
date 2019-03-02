from models.active_model import ActiveModel
from models.book import Book

class Member(ActiveModel):
    def __init__(self, name, record_id = None):
        self.record_id = record_id
        self.name = name

    def books(self):
        collection = []
        with open('db/member_books.txt') as file:
            for line in file:
                if line.startswith(f"{self.record_id},"):
                    book = Book.find(line.strip().split(',')[-1])
                    if book:
                        collection.append(book)
        return collection

    def assign_book(self, book_id):
        book = Book.find_with_alert(book_id)
        if not book:
            return
        with open('db/member_books.txt', 'r+') as file:
            for line in file:
                if line.startswith(f"{self.record_id},{book_id}"):
                    print('Already assigned')
                    return
            file.write(f"{self.record_id},{book_id}\n")
        book.available -= 1
        book.save()
        return 'Operation successful'

    def return_book(self, book_id):
        success = False
        book = Book.find_with_alert(book_id)
        if not book:
            return
        with open('db/member_books.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.startswith(f"{self.record_id},{book_id}"):
                    book.available += 1
                    book.save()
                    success = True
                else:
                    file.write(line)
            file.truncate()
        if success:
            return 'Operation successful'
        else:
            return 'Record not found'
