from django.forms import ModelForm
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'tags': TagWidget(), # Helps format the tags input nicely
        }

# (Keep your existing CommentForm here as well)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']