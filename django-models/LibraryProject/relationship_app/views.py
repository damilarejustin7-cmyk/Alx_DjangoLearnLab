from django.shortcuts import render
from django.views.generic.details import DetailView
from .models import Book
from .models import Library

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_objects_name = 'Library'
    