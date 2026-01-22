from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    
    pass