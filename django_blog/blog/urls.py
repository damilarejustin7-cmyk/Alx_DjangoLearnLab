from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Blog Home
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    
    # Detail
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Update
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/',views.profile,name='profile'), 
]
