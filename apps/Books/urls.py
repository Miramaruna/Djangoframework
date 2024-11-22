from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
# router.register("s_viewsets", RecipeViewsSets, basename='api-recipe')

urlpatterns = [
    path('authors/', AuthorsListApiView.as_view(), name='users'),
    path('authors/add', AuthorsCreateApiView.as_view(), name='adduser'),
    path('books/', BookListApiView.as_view(), name='books'),
    path('books/add', BookCreateApiView.as_view(), name='booksadd'),
    path('genre/', GenreListApiView.as_view(), name='genres'),
    path('genre/add', GenreCreateApiView.as_view(), name='genreadd'),
    path('authors/<int:pk>', AuthorsListApiView.as_view(), name='usersfromnum'),
    path('books/<int:pk>', BookListApiView.as_view(), name='booksfromnum'),
    path('genre/<int:pk>', GenreListApiView.as_view(), name='genresfromnum'),
]

# urlpatterns += router.urls