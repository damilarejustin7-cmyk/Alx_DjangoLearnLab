# api/views.py
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# This handles only the GET (List) logic as requested in Task 1
class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

# This handles GET, POST, PUT, DELETE logic for Task 2
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated | IsAdminUser] 
    