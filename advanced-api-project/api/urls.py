from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

url patterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]