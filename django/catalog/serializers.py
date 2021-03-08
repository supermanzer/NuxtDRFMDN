from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from rest_framework import serializers
from .models import Author, BorrowedCopy, Genre, BookInstance, Book


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'url', 'name']


class InstanceSerializer(serializers.ModelSerializer):
    inst_status = serializers.CharField(source='get_status_display')
    book = serializers.CharField(source='book.title')
    book_id = serializers.IntegerField(source='book.id')

    class Meta:
        model = BookInstance
        fields = [
            'id',
            'url',
            'book',
            'book_id',
            'imprint',
            'status',
            'inst_status',
            'due_date',
            'overdue',
        ]


class BookListSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='display_genre')
    author = serializers.CharField(source='author.display_name')

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'genre',
            'summary'
        ]


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'last_name',
            'first_name',
            'date_of_birth',
            'date_of_death'
        ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'url', 'last_name', 'first_name',
                  'date_of_birth', 'date_of_death', 'books']


class BookDetailSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='display_genre')
    author = AuthorSerializer(many=False, read_only=True)
    instances = InstanceSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'genre',
            'author',
            'summary',
            'isbn',
            'image',
            'instances'
        )


class BorrowedSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='copy.book', read_only=True)
    # status = serializers.CharField(source="copy.status", read_only=True),
    # copy = serializers.CharField(source='copy.id')

    class Meta:
        model = BorrowedCopy
        fields = (
            'id', 'patron', 'copy', 'book',
            'date_checked_out', 'due_date',
            'date_returned', 'late_fee',  # 'status'
        )
