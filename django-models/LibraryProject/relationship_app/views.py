from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Book, Library

def list_books(request):
    books = Book.objects.select_related("author").all()
    # Uses the required template:
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_details.html"
    context_object_name = "library"
