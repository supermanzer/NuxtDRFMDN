from .models import Genre, BookInstance, Book, Author
from rest_framework import viewsets, filters
from django_filters import rest_framework as df_filters
from .serializers import GenreSerializer, BookSerializer, InstanceSerializer, AuthorSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['last_name', 'first_name']


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title']
    ordering_fields = ['title', 'author', 'genre']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class InstanceViewset(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = InstanceSerializer
    search_fields = ['book__title', 'status']
    filterset_fields = ('status', )
    filter_backends = [df_filters.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
