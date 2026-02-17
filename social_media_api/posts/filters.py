import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
     content = django_filters.CharFilter(lookup_expr='icontains')  # Search content
    # title = django_filters.CharFilter(field_name='title')  # If posts had title
     
     class Meta:
        model = Post
        fields = ['content']  # Filter by content

