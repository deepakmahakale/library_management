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
    1. Add member
    2. Update member details
    3. Delete member
    4. Add book
    5. Update book details
    6. Delete book
    7. View a member
    9. Assign a book
    10. List all members
    11. List all books"""

while True:

    print(message)
    option = input('Please enter your choice: ').lower()

    if option == '1':
        name = input('Member name: ')
        if confirm():
            member = Member(name)
            member.save()
            print('Member added successfully')

    elif option == '7':
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

    elif option == '9':
        member_id = input('Member id: ')
        member = Member.find_with_alert(member_id)
        book_id = input('Book id: ')
        print(member.assign_book(book_id))

    elif option == '10':
        print('=' * 80)
        print(f"Sr.No.  Name{' '*36}")
        print('=' * 80)
        for index, member in enumerate(Member.all(), start = 1):
            print(f'{str(index).ljust(8)}{member.name.ljust(40)}')


    elif option == '11':
        print('=' * 80)
        print(f"Sr.No. Book ID Name{' '*36}Author{' '*16}Available")
        print('=' * 80)
        for index, book in enumerate(Book.all(), start = 1):
            print(f'{str(index).ljust(8)}{str(book.record_id).ljust(7)}{book.name.ljust(40)}{book.author.ljust(20)}{book.available}')

    elif option == 'exit':
        print('Exiting....')
        break

    else:
        print("nothing")
