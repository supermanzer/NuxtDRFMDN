from rest_framework import serializers
from .models import Author, Genre, BookInstance, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'last_name', 'first_name',
                  'date_of_birth', 'date_of_death']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['url', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.CharField(source='display_genre')
    author = serializers.CharField(source='author.display_name')

    class Meta:
        model = Book
        fields = [
            'url',
            'title',
            'author',
            'summary',
            'isbn',
            'genre'
        ]


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInstance
        fields = [
            'url',
            'book',
            'imprint',
            'status',
            'due_date'
        ]
