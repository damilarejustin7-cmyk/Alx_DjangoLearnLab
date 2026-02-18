"""
posts/views.py - Complete API views for Posts, Comments, and Feed
Handles CRUD, pagination, filtering, permissions, and social feed functionality.
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .filters import PostFilter


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom object-level permission:
    - SAFE_METHODS (GET, HEAD, OPTIONS): Allow everyone
    - Write methods (POST, PUT, PATCH, DELETE): Owner only
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    Complete CRUD API for Posts with:
    - Pagination (10/page via settings)
    - Filtering (?content=hello)
    - Search (?search=keyword)
    - Owner-only edit/delete permissions
    - Default ordering: newest first
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Comments
    - Owner-only edit/delete permissions
    - No pagination for compact threads
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = None


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    """
    Social feed endpoint: /api/posts/feed/
    Returns posts from users that request.user follows, newest first
    """

    following_users = request.user.following.all()

    feed_posts = (
        Post.objects
        .filter(author__in=following_users)
        .select_related('author')
        .order_by('-created_at')
    )

    serializer = PostSerializer(feed_posts, many=True)
    return Response(serializer.data)
