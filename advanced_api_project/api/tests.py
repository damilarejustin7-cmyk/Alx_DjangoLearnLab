from django.test import TestCase
from api.models import Author, Book
# Create your tests here.
class AuthorBookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=self.author)

    def test_author_creation(self):
        self.assertEqual(self.author.name, "J.K. Rowling")

    def test_book_creation(self):
        self.assertEqual(self.book1.title, "Harry Potter and the Philosopher's Stone")
        self.assertEqual(self.book1.publication_year, 1997)
        self.assertEqual(self.book1.author, self.author)

    def test_author_books_relationship(self):
        books = self.author.books.all()
        self.assertEqual(books.count(), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)
     
    def test_string_representation(self):
        self.assertEqual(str(self.author), "J.K. Rowling")
        self.assertEqual(str(self.book1), "Harry Potter and the Philosopher's Stone")