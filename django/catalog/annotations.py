"""
    catalog/annotations.py

    This file defines custom annotations applied to be applied to Django model classes defined in catalog.models.
"""
from django.db.models import Case, When, OuterRef, Exists
from django.db.models.expressions import Value
from django.db.models.fields import CharField
from .models import BookInstance, BorrowedCopy

# Define BorrowedCopy conditions for ON_LOAN and RESERVED statuses
on_loan = BorrowedCopy.objects.filter(
    copy=OuterRef('pk'),
    date_checked_out__isnull=False,
    date_returned__isnull=True,
)
reserved = BorrowedCopy.objects.filter(
    copy=OuterRef('pk'),
    date_checked_out__isnull=True
)

status_patrons = Case(
    When(Exists(on_loan), then=Value(BookInstance.ON_LOAN)),
    When(Exists(reserved), then=Value(BookInstance.RESERVED)),
    default=Value(BookInstance.MAINTENANCE),
    output_field=CharField()
)

status_staff = Case(
    When(Exists(reserved), then=Value(BookInstance.RESERVED)),
    default=Value(BookInstance.AVAILABLE),
    output_field=CharField()
)
