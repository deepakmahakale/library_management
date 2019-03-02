from models.book import Book
from models.member import Member

def filecheck():
    open('db/books.txt', 'a+').close()
    open('db/members.txt', 'a+').close()
    open('db/member_books.txt', 'a+').close()

def confirm():
    options = input('Are you sure you want to proceed? (Y/N) ')
    if options.lower() == 'y':
        print('Proceeding...')
        return True
    else:
        print('Last operation is cancelled.')
        return False

filecheck()

message = """
    1. List members                6. List books
    2. View member deails          7. Add book
    3. Add Member                  8. Update book details
    4. Update member details       9. Delete book
    5. Delete member              10. Assign book

    11. Return book

    Type `exit` to exit the program
"""

while True:

    print(message)
    option = input('Please enter your choice: ').lower()

    if option == '1':
        print('=' * 80)
        print(f"Sr.No. Member ID Name{' '*36}")
        print('=' * 80)
        for index, member in enumerate(Member.all(), start = 1):
            print(f'{str(index).ljust(7)}{str(member.record_id).ljust(10)}{member.name.ljust(30)}')

    elif option == '2':
        member_id = input('Member id: ')
        member = Member.find(member_id)
        if not member:
            print("Record not found")
        else:
            print('=' * 80)
            print(f'Name:\t{member.name}')
            print('=' * 80)
            books = member.books()
            if not books:
                continue
            for index, book in enumerate(books, start = 1):
                print(f"{index}.\t{book.name}")

    elif option == '3':
        name = input('Member name: ')
        if confirm():
            member = Member(name)
            member.save()
            print('Member added successfully')

    elif option == '4':
        member_id = input('Member ID: ')
        member = Member.find_with_alert(member_id)
        if not member:
            continue
        print("Enter the updated details. If you don't provide value it will remain unchanged")
        name = input(f'Member name: ({member.name}): ').strip()
        if name:
            member.name = name
            member.save()
            print('Details updated successfully')


    elif option == '5':
        member_id = input('Member ID: ')
        if confirm():
            member = Member.find_with_alert(member_id)
            Member.delete(member_id)
            print('Member deleted successfully')

    elif option == '6':
        print('=' * 80)
        print(f"Sr.No. Book ID Name{' '*26}Author{' '*14}Available")
        print('=' * 80)
        for index, book in enumerate(Book.all(), start = 1):
            print(f'{str(index).ljust(8)}{str(book.record_id).ljust(7)}{book.name.ljust(30)}{book.author.ljust(20)}{book.available}')

    elif option == '7':
        name = input('Book name: ')
        author_name = input('Author name: ')
        available = input('Available book count: ')
        if confirm():
            book = Book(name, author_name, available)
            book.save()
            print('Book added successfully')

    elif option == '8':
        book_id = input('Book ID: ')
        book = Book.find_with_alert(book_id)
        if not book:
            continue
        print("Enter the updated details. If you don't provide value it will remain unchanged")
        name = input(f'Book name: ({book.name}): ').strip()
        author = input(f'Book author: ({book.author}): ').strip()
        available = input(f'Books available: ({book.available}): ').strip()
        if name:
            book.name = name
        if author:
            book.author = author
        if available:
            book.available = available
        if name or author or available:
            book.save()
            print('Details updated successfully')

    elif option == '9':
        book_id = input('Book ID: ')
        if confirm():
            member = Book.find_with_alert(book_id)
            Book.delete(book_id)
            print('Book deleted successfully')

    elif option == '10':
        member_id = input('Member id: ')
        member = Member.find_with_alert(member_id)
        book_id = input('Book id: ')
        print(member.assign_book(book_id))

    elif option == '11':
        member_id = input('Member id: ')
        member = Member.find_with_alert(member_id)
        book_id = input('Book id: ')
        print(member.return_book(book_id))

    elif option == 'exit':
        print('Exiting....')
        break

    else:
        print("nothing")
