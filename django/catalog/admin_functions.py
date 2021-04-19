"""
    catalog/admin_functions.py

    Creating custom funcionality to be added to the Django admin site.
    https://docs.djangoproject.com/en/3.1/ref/contrib/admin/actions/

    Function(s):
    * return_to_circulation:  Sets `BookInstance` status based on `BorrowedCopy` subquery results
"""

from .annotations import status_staff


def return_to_circulation(modeladmin, request, queryset):
    """
    Assign correct `status` value to `BookInstance` based on `BorrowedCopy` subquery 

    Args:
        modeladmin (ModelAdmin): ModelAdmin objeect for `BookInstance`
        request (HttpRequest): HttpRequest object
        queryset (Queryset): Queryset object of `BookInstance` records to be modified.
    """
    queryset.update(status=status_staff)


# Adding a more helpful descrption to be rendered in the admin interface
return_to_circulation.short_description = 'Return copies to circulation'
