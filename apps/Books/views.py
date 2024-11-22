
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
# Create your views here.
from apps.Books.models import Books, Genre, Authors
from apps.Books.serializers import BooksSerializer, GenreSerializer, AuthorsSerializer

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class AuthorsCreateApiView(CreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    pagination_class = Pagination

class AuthorsListApiView(ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    pagination_class = Pagination

class BookCreateApiView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = Pagination

class BookListApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = Pagination

class GenreCreateApiView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = Pagination

class GenreListApiView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = Pagination