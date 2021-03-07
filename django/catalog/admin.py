from django.contrib import admin
from .models import Author, Book, BookInstance, BorrowedCopy, Genre


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
    inlines = [BorrowedInline, ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(BorrowedCopy)
class BorrowedAdmin(admin.ModelAdmin):
    list_display = ('copy', 'patron', 'date_checked_out',
                    'due_date', 'date_returned', 'late_fee')
    fieldsets = (
        (None, {
            'fields': ('copy', 'patron')
        }),
        ('Dates', {
            'fields': ('date_checked_out', 'due_date', 'date_returned')
        }),
        (None, {
            'fields': ('late_fee', )
        })
    )


class BorrowedInline(admin.TabularInline):
    model = BorrowedCopy
    extra = 0

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)
