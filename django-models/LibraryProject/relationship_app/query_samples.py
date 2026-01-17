from relationship_app.models import Author, Book, Library, Librarian

# Sample Queries 
author_books = book.objects.filter(author__id=1)
print("Books by specific author:")
for book in author_books:
    print(f"-{book.title}") by {book.author.name}")

library_books = Library.objects.get(id=1).books.all()    
print("\nBooks in library:")
for book in library_books:
    print(f"- {book.title}")

try:
    librarian = Librarian.objects.get(library_id=1)
    print(f"\nLibrarian: {librarian.name} for {librarian.library.name}")
except Librarian.DoesNotExist:
    print("\nNo librarian found.")