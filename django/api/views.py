"""
    api/views.py

    Define general purpose (non-app specific) views to return needed data
"""

from django.db.models import query
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from myauth.models import User

from .serializers import UserSerializer

# Create your views here.


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
