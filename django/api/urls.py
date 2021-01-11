from django.urls import include, path
from rest_framework import routers
from catalog import api_views


router = routers.DefaultRouter()
# Registering API endpoints tied to our models
router.register(r'authors', api_views.AuthorViewset)
router.register(r'books', api_views.BookViewset)
router.register(r'book-instances', api_views.InstanceViewset)
router.register(r'genres', api_views.GenreViewset)

urlpatterns = [
    path('', include(router.urls))
]
