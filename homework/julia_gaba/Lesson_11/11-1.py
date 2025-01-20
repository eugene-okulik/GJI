class Book:
    text = True
    material = 'бумага'

    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


book1 = Book('Идиот', 'Достоевский', 500, '978-5-699-12014-7', reserved=True)
book2 = Book("Преступление и наказание", "Достоевский",
             550, '978-5-679-12034-7', reserved=False)
book3 = Book("Война и мир", "Толстой", 1300,
             '978-5-679-62034-4', reserved=False)
book4 = Book("Анна Каренина", "Толстой", 864,
             '978-5-819-62034-4', reserved=False)
book5 = Book("Мастер и Маргарита", "Булгаков", 480,
             '918-5-679-62834-3', reserved=True)

book_list = [book1, book2, book3, book4, book5]

for i in book_list:
    if i.reserved:
        print(f"Название: {i.title}, Автор: {i.author}, страниц: {i.pages}, \n"
              f"материал: {i.material}, 'зарезервирована'")
    else:
        print(
            f"Название: {i.title}, Автор: {i.author}, страниц: {i.pages}, материал: {i.material}")


class SchoolBook(Book):

    def __init__(self, title, author, pages, subject, group, exercise=None, isbn=None, reserved=False):
        super().__init__(title, author, pages, isbn=isbn, reserved=reserved)
        self.subject = subject
        self.group = group
        self.exercise = exercise


school_book1 = SchoolBook('Алгебра', 'Иванов', 200,
                          'Математика', 9, reserved=True)
school_book2 = SchoolBook('Геометрия', 'Жуков', 180,
                          'Математика', 9, reserved=False)
school_book3 = SchoolBook('Русский язык', 'Горчаков', 210,
                          'Русский язык', 5, reserved=False)
school_book4 = SchoolBook('Квантовая физика', 'Петров', 230,
                          'Физика', 10, reserved=False)

school_books = [school_book1, school_book2, school_book3, school_book4]

for x in school_books:
    if x.reserved:
        print(f"Название: {x.title}, Автор: {x.author}, страниц: {x.pages}, \n"
              f"предмет: {x.subject}, класс: {x.group}, 'зарезервирована'")
    else:
        print(f"Название: {x.title}, Автор: {x.author}, страниц: {x.pages}, \n"
              f"предмет: {x.subject}, класс: {x.group}")
