from django.urls import path
from .views import BookListCreateView, BookDetailView, UserRegistrationView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('users/register/', UserRegistrationView.as_view(), name='user-registration'),
]
