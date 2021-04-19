"""
    catalog/managers.py

    Define custom model managers to encapsulate the use of annotations in returning querysets.
"""

from django.db.models import Manager, Subquery


class InstanceManager(Manager):
    """
    Define custom manager to handle dynamic values in DB layer.
    """

    def get_queryset(self):
        from .annotations import on_loan
        return super().get_queryset().annotate(due_date=Subquery(on_loan.values('due_date')[:1]))
