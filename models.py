class Book:
    """Представляет книгу в трекере чтения."""

    def __init__(self, title, author, pages, current_page=0):
        """Инициализирует книгу с базовыми атрибутами."""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page

    def progress(self):
        """Возвращает процент прогресса чтения книги."""
        if self.pages > 0:
            return (self.current_page / self.pages) * 100
        return 0
