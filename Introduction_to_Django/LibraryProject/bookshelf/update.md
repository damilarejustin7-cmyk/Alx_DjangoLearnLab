# Command:
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output: <Book: Nineteen Eighty-Four> (Title updated and saved)