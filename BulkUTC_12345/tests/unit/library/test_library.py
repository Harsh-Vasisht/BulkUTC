import unittest
from typing import List, Optional

# Mock implementations

class Author:
    def __init__(self, name: str):
        self.name = name

    def getName(self) -> str:
        return self.name

class Book:
    def __init__(self, isbn: str, title: str, author: Author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def getIsbn(self) -> str:
        return self.isbn

    def getTitle(self) -> str:
        return self.title

    def getAuthor(self) -> Author:
        return self.author

class AbstractLibrary:
    def addBook(self, book: Book) -> None:
        pass

    def removeBook(self, isbn: str) -> bool:
        pass

    def findBookByTitle(self, title: str) -> Optional[Book]:
        pass

    def listBooks(self) -> List[Book]:
        pass

    def findBooksByAuthor(self, author: Author) -> List[Book]:
        pass

# Implementation of Library class (ported from PHP to Python)

class Library(AbstractLibrary):
    def __init__(self):
        self.books = {}

    def addBook(self, book: Book) -> None:
        self.books[book.getIsbn()] = book

    def removeBook(self, isbn: str) -> bool:
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def findBookByTitle(self, title: str) -> Optional[Book]:
        for book in self.books.values():
            if book.getTitle().lower() == title.lower():
                return book
        return None

    def listBooks(self) -> List[Book]:
        return list(self.books.values())

    def findBooksByAuthor(self, author: Author) -> List[Book]:
        return [book for book in self.books.values() if book.getAuthor().getName() == author.getName()]

# Test cases

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.author1 = Author("John Doe")
        self.author2 = Author("Jane Smith")
        self.book1 = Book("1234567890", "Python Programming", self.author1)
        self.book2 = Book("0987654321", "Data Structures", self.author2)
        self.book3 = Book("1122334455", "Algorithms", self.author1)

    def test_add_book(self):
        self.library.addBook(self.book1)
        self.assertEqual(len(self.library.listBooks()), 1)
        self.assertEqual(self.library.listBooks()[0].getIsbn(), "1234567890")

    def test_remove_book(self):
        self.library.addBook(self.book1)
        self.assertTrue(self.library.removeBook("1234567890"))
        self.assertEqual(len(self.library.listBooks()), 0)
        self.assertFalse(self.library.removeBook("1234567890"))

    def test_find_book_by_title(self):
        self.library.addBook(self.book1)
        self.library.addBook(self.book2)
        found_book = self.library.findBookByTitle("Python Programming")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.getIsbn(), "1234567890")
        self.assertIsNone(self.library.findBookByTitle("Nonexistent Book"))

    def test_find_book_by_title_case_insensitive(self):
        self.library.addBook(self.book1)
        found_book = self.library.findBookByTitle("python programming")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.getIsbn(), "1234567890")

    def test_list_books(self):
        self.library.addBook(self.book1)
        self.library.addBook(self.book2)
        books = self.library.listBooks()
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

    def test_find_books_by_author(self):
        self.library.addBook(self.book1)
        self.library.addBook(self.book2)
        self.library.addBook(self.book3)
        books_by_author1 = self.library.findBooksByAuthor(self.author1)
        self.assertEqual(len(books_by_author1), 2)
        self.assertIn(self.book1, books_by_author1)
        self.assertIn(self.book3, books_by_author1)
        books_by_author2 = self.library.findBooksByAuthor(self.author2)
        self.assertEqual(len(books_by_author2), 1)
        self.assertIn(self.book2, books_by_author2)

    def test_find_books_by_nonexistent_author(self):
        self.library.addBook(self.book1)
        self.library.addBook(self.book2)
        nonexistent_author = Author("Nonexistent Author")
        books = self.library.findBooksByAuthor(nonexistent_author)
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()