class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_lis):
        books = []
        for title, author in book_lis:
            books.append(Book(title, author))
        return cls(books)


bc = Bookcase.create_bookcase([('Moby-Dick', 'Herman Melville'), ('Jungle Book', 'Rudyard Kipling')])
print(bc)
print(bc.books)
print(bc.books[0])
print(bc.books[1])


class DreamVacation:
    def __init__(self, *args):
        self.location = args
        self.activities = args

    @classmethod
    def rome(cls):
        return cls('Rome', ['visit the Colosseum', 'Eat gelato'])


vacacion = DreamVacation()
print(str(vacacion.rome()))


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)