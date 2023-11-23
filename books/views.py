from rest_framework import generics
from .models import Book, CustomUser
from .serializers import BookSerializer, CustomUserSerializer
from rest_framework.response import Response
from .tasks import send_welcome_email

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.id)
        return Response(serializer.data)
