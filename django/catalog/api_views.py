

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import BorrowedCopy, Genre, BookInstance, Book, Author
from .serializers import (
    AuthorListSerializer, BookDetailSerializer, BorrowedSerializer,
    GenreSerializer, BookListSerializer, InstanceSerializer, AuthorSerializer
)
from api.viewset_mixins import ListDetailMixin

from logging import getLogger

logger = getLogger(__name__)


class AuthorViewset(ListDetailMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    detail_serializer = AuthorSerializer
    list_serializer = AuthorListSerializer
    search_fields = ['last_name', 'first_name']

    @method_decorator(cache_page(60*60*12))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*60*12))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # The books by each other do not change very much so we'll cache these results for 4 hours
    @method_decorator(cache_page(60*60*4))
    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        obj = self.get_object()
        books = [
            BookDetailSerializer(b).data
            for b in obj.books.all()
        ]
        return Response(books)


class BookViewset(ListDetailMixin, viewsets.ModelViewSet):
    queryset = Book.objects.all()
    list_serializer = BookListSerializer
    detail_serializer = BookDetailSerializer
    search_fields = ['title']
    ordering_fields = ['title', 'author', 'genre']
    filterset_fields = ['author', 'genre', 'instances__status']

    def get_queryset(self):
        return Book.objects.all().prefetch_related('genre').distinct()
        

    @action(detail=True, methods=['get'])
    def instances(self, request, pk=None):
        obj = self.get_object()
        instances = [
            InstanceSerializer(i).data
            for i in obj.instances.all()
        ]
        return Response(instances)

    


class InstanceViewset(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = InstanceSerializer
    search_fields = ['book__title', 'status']
    filterset_fields = ('status', )


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BorrowViewset(viewsets.ModelViewSet):
    queryset = BorrowedCopy.objects.all()
    serializer_class = BorrowedSerializer

    @action(detail=False, methods=['get'])
    def user_books(self, request):
        """Provide view of checked out books specific to user."""
        data = {}
        if request.user.is_authenticated:
            qs = self.queryset.filter(
                patron=request.user.id, date_returned__isnull=True, 
                date_checked_out__isnull=False)
            data['current'] = self.get_serializer(qs, many=True).data
            qs = self.queryset.filter(
                patron=request.user.id, date_returned__isnull=False)
            data['historic'] = self.get_serializer(qs, many=True).data
            qs = self.queryset.filter(
                patron=request.user.id,
                date_checked_out__isnull=True
            )
            data['reservations'] = self.get_serializer(qs, many=True).data
        else:
            data = {'message': 'Unauthenticated request.'}
        return Response(data)

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data.update({'patron': user.id})
        logger.info(request.data)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        logger.info(f'Calling partial update in Viewset: {args}, {kwargs}')
        return super().partial_update(request, *args, **kwargs)
