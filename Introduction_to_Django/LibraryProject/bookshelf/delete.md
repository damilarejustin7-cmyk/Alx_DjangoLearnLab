# Command:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirmation:
all_books = Book.objects.all()
print(all_books)

# Expected Output: <QuerySet []> (The list is empty, confirming deletion)