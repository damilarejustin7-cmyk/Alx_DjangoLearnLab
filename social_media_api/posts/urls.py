 # posts/urls.py
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, user_feed
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),  # Single include for all routes
    path('feed/', user_feed, name='user-feed'),  # User feed endpoint
    # Nested comments 
    # path('posts/<int:post_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-comments'),
]