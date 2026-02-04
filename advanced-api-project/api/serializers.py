from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Create serializers for Book and Author models
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
# This nests the BookSerializer we just made
    # 'many=True' because one author has many books
    # 'read_only=True' is usually best for nested data
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# This is an example of a custom validation to ensure publication year is not in the future
#The 'data' argument is a dictionary of all field values being validated.
    def validate(self, data):
        if data['publication_year'] > 2026:
            raise serializers.ValidationError({
                "Publication year cannot be in the future."
                })
        return data