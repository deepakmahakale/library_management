from models.active_model import ActiveModel

class Book(ActiveModel):
    def __init__(self, name, author, available = None, record_id = None):
        self.id = record_id
        self.name = name
        self.author = author
        self.available = available

    # def all():
    #     file = open('books.txt', 'a+')
    #     file.seek(0)
    #     print(file.read())
    #     file.close()


    # def save(self):
    #     if self.id:
    #         # Update
    #         with open('books.txt', 'r+') as file:
    #             lines = file.readlines()
    #             file.seek(0)
    #             for line in lines:
    #                 if line.startswith(f"{self.id},"):
    #                     file.write(self.attributes())
    #                 else:
    #                     file.write(line)
    #             file.truncate()
    #     else:
    #         # Add new record
    #         file = open('books.txt', 'a+')
    #         file.seek(0)
    #         lastline = file.readlines()[-1]
    #         if lastline is None:
    #             pk = 1
    #         else:
    #             pk = int(lastline.split(',')[0]) + 1
    #         self.id = pk
    #         file.write(self.attributes())
    #         file.close()
    #     return self


    # def attributes(self):
    #     return f"{self.id},{self.name},{self.author}\n"


    # def delete(id):
    #     with open('books.txt', 'r+') as file:
    #         lines = file.readlines()
    #         file.seek(0)
    #         for line in lines:
    #             if not line.startswith(f"{id},"):
    #                 file.write(line)
    #         file.truncate()


    # def find(id):
    #     with open('books.txt', 'r+') as file:
    #         for line in file:
    #             if line.startswith(f"{id},"):
    #                 book = Book(*line.strip().split(',')[1:])
    #                 book.id = id
    #                 return book
