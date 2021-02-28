
from .models import BorrowedCopy, Genre, BookInstance, Book, Author
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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


class BorrowViewset(viewsets.ModelViewSet):
    queryset = BorrowedCopy.objects.all()
    serializer_class = BorrowedSerializer

    @action(detail=False, methods=['get'])
    def user_books(self, request):
        """Provide view of checked out books specific to user."""
        data = {}
        if request.user.is_authenticated:
            qs = self.queryset.filter(
                patron=request.user.id, date_returned__isnull=True)
            data['current'] = self.get_serializer(qs, many=True).data
            qs = self.queryset.filter(
                patron=request.user.id, date_returned__isnull=False)
            data['historic'] = self.get_serializer(qs, many=True).data
        else:
            data = {'message': 'Unauthenticated request.'}
        return Response(data)

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data.update({'patron': user.id})
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        logger.info(f'Calling partial update in Viewset: {args}, {kwargs}')
        return super().partial_update(request, *args, **kwargs)
