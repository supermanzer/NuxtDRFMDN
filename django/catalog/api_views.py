from .models import Genre, BookInstance, Book, Author
from rest_framework import viewsets
from .serializers import GenreSerializer, BookSerializer, InstanceSerializer, AuthorSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['last_name', 'first_name']


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title']


class InstanceViewset(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = InstanceSerializer
    filterset_fields = ['status']


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
