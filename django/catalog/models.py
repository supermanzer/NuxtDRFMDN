import uuid
from django.urls import reverse
from django.db import models
from myauth.models import User
from datetime import date, timedelta
# Create your models here.

from logging import getLogger

logger = getLogger(__name__)


class Genre(models.Model):
    """Model representing book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name', ]


class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True, help_text='13 character ISBN number')
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book')
    image = models.URLField(
        help_text='A URL to an image for this book',
        null=True, blank=True
    )

    class Meta:
        ordering = ['title']

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
    book = models.ForeignKey(
        'Book', on_delete=models.RESTRICT, related_name='instances')
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS,  # <- 1 advantage, no need to re-define values that shoud be constant
                              blank=True, default=MAINTENANCE, help_text='Book availability')
    # Meta options

    class Meta:
        verbose_name = 'Copy'
        verbose_name_plural = 'Copies'
        ordering = ['due_date']

    # Model methods
    def __str__(self):
        return f'{self.id} ({self.book.title})'

    @property
    def overdue(self):
        if self.due_date and date.today() > self.due_date:
            return True
        return False


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

    def display_name(self) -> str:
        return str(self)


class BorrowedCopy(models.Model):
    """Defining a custom model to relate the borrowing of a book instance to a library patron"""
    # Constants
    # Length of time a book can be checked out for
    CHECKOUT_DURATION = timedelta(days=14)
    LATE_FEE = 0.5  # The per day fee assessed if a copy is late
    # Fields
    patron = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='borrowed_books')
    copy = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    date_checked_out = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    date_returned = models.DateField(null=True, blank=True)
    late_fee = models.FloatField(
        verbose_name='Late Fee', default=0.0, null=True, help_text='Late fee assessed (if any)')

    # Meta options
    class Meta:
        ordering = ('copy', )
        verbose_name = 'Checkout History'
        verbose_name_plural = 'Checkout History'

    # Model methods
    def save(self, *args, **kwargs):
        """Override default save method to set due date"""
        logger.info(f'Calling model save method for {self}')
        # We are going to use these records to hold reservations as well
        # so we need to accomodate situations where date_checked_out = None
        if self.date_checked_out and not self.due_date:
            self.due_date = self.date_checked_out + self.CHECKOUT_DURATION
            # This bit is redundant and I'll likely remove the due_date from
            # the Instance model but for now, let's keep our data in sync
            self.copy.due_date = self.due_date
            self.copy.save()
        if self.date_returned and self.date_returned > self.due_date:
            # Assigning late fee if returned after due date
            self.late_fee = (self.date_returned -
                             self.due_date).days * self.LATE_FEE
        super().save(*args, **kwargs)
