from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, RetrieveTokenView, CustomUserViewSet, FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)  # /api/accounts/users/

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs for user listing/detail
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', RetrieveTokenView.as_view(), name='retrieve_token'),
     path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]