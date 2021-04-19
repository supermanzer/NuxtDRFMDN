from logging import getLogger
from django.contrib import admin
from .models import Author, Book, BookInstance, BorrowedCopy, Genre
from .admin_functions import return_to_circulation

logger = getLogger(__name__)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = [
        'first_name', 'last_name',
        ('date_of_birth', 'date_of_death')
    ]


class InstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [InstanceInline, ]


class BorrowedInline(admin.TabularInline):
    model = BorrowedCopy
    extra = 0


@admin.register(BookInstance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'id')
    list_filter = ('status',)
    search_fields = ['id', 'book__title']
    inlines = [BorrowedInline, ]
    actions = [return_to_circulation, ]
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status',)
        })
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        logger.info(f'{qs.first().__dict__}')
        return qs


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class BorrowedInline(admin.TabularInline):
    model = BorrowedCopy
    extra = 0

    readonly_fields = '__all__'
