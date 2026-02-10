1. Modify bookshelf/admin.py
Open your admin.py file and use the following code. This registers the model and applies the customizations for the list view, filters, and search functionality.

Python
from django.contrib import admin
from .models import Book

# Customizing the Admin Interface
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a filter sidebar for the publication year
    list_filter = ('publication_year', 'author')
    
    # Add a search bar to search by title and author
    search_fields = ('title', 'author')

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)
2. Breakdown of Customizations
By adding these attributes to the BookAdmin class, you change how the Django dashboard behaves:

list_display: Instead of just seeing the title (from your __str__ method), you will now see three distinct columns for title, author, and year.

list_filter: A sidebar will appear on the right. This is incredibly helpful once you have dozens of books and want to see only those from a specific year.

search_fields: A search box appears at the top. This allows you to perform partial matches on titles or author names.