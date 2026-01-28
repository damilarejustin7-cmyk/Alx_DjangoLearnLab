# api/views.py
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# This handles only the GET (List) logic as requested in Task 1
class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This handles GET, POST, PUT, DELETE logic for Task 2
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer