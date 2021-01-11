from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


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


@admin.register(BookInstance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_date', 'id')
    list_filter = ('due_date', 'status',)
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_date')
        })
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)
