from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserNotificationsView.as_view(), name='user-notifications'),
]
