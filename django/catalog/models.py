import uuid
from django.urls import reverse
from django.db import models

# Create your models here.


class Genre(models.Model):
    """Model representing book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True, help_text='13 character ISBN number')
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        """Return URL to access a detail record for this book"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self) -> str:
        return ', '.join(genre.name for genre in self.genre.all())


class BookInstance(models.Model):
    """Model representing a specific copy of a book"""
    # CONSTANTS - I FIND THIS APPROACH USEFUL EVEN THOUGH IT SEEMS REDUNDANT
    MAINTENANCE = 'm'
    ON_LOAN = 'o'
    AVAILABLE = 'a'
    RESERVED = 'r'

    LOAN_STATUS = (
        (MAINTENANCE, 'Maintenance'),
        (ON_LOAN, 'On loan'),
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved')
    )
    # FIELDS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for particular book')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS,  # <- 1 advantage, no need to re-define values that shoud be constant
                              blank=True, default=MAINTENANCE, help_text='Book availability')

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing Author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self) -> str:
        return reverse('author-detail', kwargs={'pk': self.id})

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'
