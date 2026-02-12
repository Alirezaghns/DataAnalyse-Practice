# class Book:
#     def __init__(self, book_name, writer_name):
#         self.book_name = book_name
#         self.writer_name = writer_name


# class ShowPage(Book):
#     def __init__(self, book_name, writer_name, pages):
#         super().__init__(book_name, writer_name)
#         self.pages = pages

#     def __str__(self):
#         return f"{self.book_name} {self.writer_name} {self.pages} pages"


# class ShowSize(Book):
#     def __init__(self, book_name, writer_name, size_mb):
#         super().__init__(book_name, writer_name)
#         self.size_mb = size_mb

#     def __str__(self):
#         return f"{self.book_name} {self.writer_name} {self.size_mb} MB"

    
# b1 = ShowPage("Savushun", "Simin Daneshvar", 307)
# b2 = ShowSize("Savushun", "Simin Daneshvar", 8)

# b3 = ShowPage("Masnavi Manavi", "Molana", 1050)
# b4 = ShowSize("Masnavi Manavi", "Molana", 18)

# b5 = ShowPage("The Gambler", "Fyodor Dostoevsky", 1200)
# b6 = ShowSize("The Gambler", "Fyodor Dostoevsky", 22)

# print(b1)
# print(b2)
# print(b3)
# print(b4)
# print(b5)
# print(b6)



#2th and best solution



class Book:
    def __init__(self, book_name, writer_name, **kwargs):
        if not isinstance(book_name, str) or not book_name.strip():
            raise ValueError("Book name must be a non-empty string")

        if not isinstance(writer_name, str) or not writer_name.strip():
            raise ValueError("Writer name must be a non-empty string")

        super().__init__(**kwargs)

        self.book_name = book_name
        self.writer_name = writer_name


class ShowPage(Book):
    def __init__(self, pages, **kwargs):
        if not isinstance(pages, int):
            raise TypeError("Pages must be an integer")

        if pages <= 0:
            raise ValueError("Pages must be greater than zero")

        super().__init__(**kwargs)
        self.pages = pages

    def page(self):
        return f"{self.pages} pages"


class ShowSize(Book):
    def __init__(self, size_mb, **kwargs):
        if not isinstance(size_mb, (int, float)):
            raise TypeError("Size must be numeric")

        if size_mb <= 0:
            raise ValueError("Size must be greater than zero")

        super().__init__(**kwargs)
        self.size_mb = size_mb

    def size(self):
        return f"{self.size_mb}MB"


class Information(ShowPage, ShowSize):
    def __init__(self, book_name, writer_name, pages, size_mb):
        super().__init__(
            book_name=book_name,
            writer_name=writer_name,
            pages=pages,
            size_mb=size_mb
        )

    def showinfo(self):
        print(
            f"{self.book_name:<20} "
            f"{self.writer_name:<20} "
            f"{self.page():<15} "
            f"{self.size()}"
        )

try:
    b1 = Information("Savushun", "Simin Daneshvar", 307, 8)
    b2 = Information("Masnavi Manavi", "Molana", 1050, 18)
    b3 = Information("The Gamber", "Fydor Dostoevsky", 1200, 22)

    b1.showinfo()
    b2.showinfo()
    b3.showinfo()

except (ValueError, TypeError) as e:
    print(f" Error: {e}")








