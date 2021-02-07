from .models import Genre, BookInstance, Book, Author
from rest_framework import viewsets, filters
from django_filters import rest_framework as df_filters
from .serializers import (
    AuthorListSerializer, BookDetailSerializer, GenreSerializer, BookListSerializer, InstanceSerializer, AuthorSerializer
)
from api.viewset_mixins import ListDetailMixin


class AuthorViewset(ListDetailMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    detail_serializer = AuthorSerializer
    list_serializer = AuthorListSerializer
    search_fields = ['last_name', 'first_name']


class BookViewset(ListDetailMixin, viewsets.ModelViewSet):
    queryset = Book.objects.all()
    list_serializer = BookListSerializer
    detail_serializer = BookDetailSerializer
    search_fields = ['title']
    ordering_fields = ['title', 'author', 'genre']


class InstanceViewset(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = InstanceSerializer
    search_fields = ['book__title', 'status']
    filterset_fields = ('status', )


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
