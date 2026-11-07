class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_info(self):
        return f"Материал: {self.title}"

class Book(LibraryItem):
    def get_info(self):
        return f"Книга: {self.title}"

class Journal(LibraryItem):
    def get_info(self):
        return f"Журнал: {self.title}"

class Audiobook(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration  # Длительность аудиокниги

    def get_info(self):
        return f"Аудиокнига: {self.title}, длительность: {self.duration} минут"

# Основная программа
library = [
    Book("Мастер и Маргарита"),
    Journal("National Geographic"),
    Audiobook("Война и мир", 1200)
]

for item in library:
    print(item.get_info())