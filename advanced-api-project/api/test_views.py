from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create an author and a book for testing
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=self.author)

    def test_book_list(self):   
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_book_detail(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter and the Philosopher's Stone")

    def test_book_create(self):
        data = {
            'title': "Harry Potter and the Chamber of Secrets",
            'publication_year': 1998,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "Harry Potter and the Chamber of Secrets")

    def test_book_update(self):
        data = {
            'title': "Harry Potter and the Sorcerer's Stone",
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/update/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Sorcerer's Stone")

    def test_book_delete(self):
        response = self.client.delete(f'/api/books/delete/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

        