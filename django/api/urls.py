from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from catalog import api_views

from .views import UserView


router = routers.DefaultRouter()
# Registering API endpoints tied to our models
router.register(r'authors', api_views.AuthorViewset)
router.register(r'books', api_views.BookViewset)
router.register(r'book-instances', api_views.InstanceViewset)
router.register(r'genres', api_views.GenreViewset)

urlpatterns = [
    path('', include(router.urls))
]

# URL Patterns based on Simple JWT authentication and NuxtJS Auth module

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('token/refresh', TokenRefreshView.as_view, name='refresh-token'),
    path('user/', UserView.as_view(), name='user-detail')
]
