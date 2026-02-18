from django.urls import path, include
from .views import PostViewSet, CommentViewSet, user_feed
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user-feed'),
     path('<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
]