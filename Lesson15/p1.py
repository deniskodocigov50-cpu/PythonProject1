class LibraryBook:
    total_books = 0

    def __init__ (self, title, status="Доступна"):
        self.title = title
        self.status = status
        LibraryBook.total_books += 1

    @classmethod
    def get_total_books(cls):
        return f"Всего книг в библиотеке: {cls.total_books}"
    @staticmethod
    def is_available(status):
        return status == 'Доступна'

    def change_status(self, new_status):
        self.status = new_status



book1 = LibraryBook("Мастер и Маргарита")
book2 = LibraryBook("1984")
print(book1.title, "-", "Доступна" if LibraryBook.is_available(book1.status) else 'Нет')
book1.change_status("в аренде")
print(book1.title, "-", "Доступна" if LibraryBook.is_available(book1.status) else 'Нет')
print(LibraryBook.get_total_books())