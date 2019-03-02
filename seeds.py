from models.book import Book
from models.member import Member

def filecheck():
    open('db/books.txt', 'a+').close()
    open('db/members.txt', 'a+').close()
    open('db/member_books.txt', 'a+').close()

filecheck()

Book('Game of thrones', 'George R. R. Martin', 2).save()
Book("Harry Potter", 'J. K. Rowling', 3).save()
Book('Moby Dick', 'Herman Melville', 4).save()

Member('Deepak').save()
Member('John').save()
Member('Jacob').save()
Member('Adam').save()
