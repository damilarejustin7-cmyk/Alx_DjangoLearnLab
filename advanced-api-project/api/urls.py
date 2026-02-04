from django.urls import path
from .views import BookList, BookDetailView

urlpatterns = [
    # This maps 'books/' to your BookList view (ListAPIView)
    path('books/', views.BookList.as_view(), name='book-list'),
        # This maps 'books/<int:pk>/' to your BookDetailView (RetrieveUpdateDestroyAPIView)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]