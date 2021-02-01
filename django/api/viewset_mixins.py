"""
    api/viewset_mixins.py

    Defining custom mixins to abstract commonly used functionality
"""


class ListDetailMixin:
    """
    Encapsulate the selection of separate serializers based on the detail boolean
    """
    # For details regarding viewset attrbiutes please refer to the DRF documentation
    # https://www.django-rest-framework.org/api-guide/viewsets/

    def get_serializer_class(self):
        if not all([hasattr(self, 'detail_serializer'), hasattr(self, 'list_serializer')]):
            raise AttributeError(
                'detail_serializer and list_serializer attributes must be set when using ListDetailMixin'
            )
        if self.detail:
            return self.detail_serializer
        else:
            return self.list_serializer
