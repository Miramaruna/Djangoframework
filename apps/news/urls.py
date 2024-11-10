from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.news.views import BooksAPI

router = DefaultRouter()
router.register("api_books", BooksAPI, basename='api-book')

urlpatterns = [

]

urlpatterns += router.urls
