from django.db import models

# Models for Author and Book
class Author(models.Model):
# String field to store the author's name    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):    
   # String field for the book's title
    title = models.CharField(max_length=200)
  # Integer field for the year published
    publication_year = models.IntegerField()
   # Foreign key linking to Author (One-to-Many)
    # on_delete=models.CASCADE means if the author is deleted, their books are too
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title