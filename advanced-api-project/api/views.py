from django.shortcuts import render
rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# This View handles the ListView for retrieving all books
class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow anyone to read, but only authenticated users to create

# This ViewSet handles all CRUD operations for Book 
# DetailView: Retrieve a single book
# UpdateView: Modify an existing book
# DeleteView: Remove a book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Allow anyone to read, but only authenticated users to update/delete