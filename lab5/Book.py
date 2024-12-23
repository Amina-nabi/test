class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return (f'Название книги: {self.title},'
                f'Автор: {self.author},'
                f'Год издания: {self.year}')
my_book = Book("Евгений Онегин",
            "Александр Сергеевич Пушкин",
               1823)
print(my_book.get_info())
