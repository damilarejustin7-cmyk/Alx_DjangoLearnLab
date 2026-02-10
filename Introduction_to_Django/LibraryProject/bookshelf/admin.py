from django.contrib import admin
from .models import Book
# Register your models here.
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