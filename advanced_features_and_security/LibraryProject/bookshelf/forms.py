from django import forms

class ExampleForm(forms.Form):
    book_title = forms.CharField(max_length=100)
    # Django forms automatically sanitize inputs to prevent XSS attacks