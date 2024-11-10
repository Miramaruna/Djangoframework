# from django.shortcuts import render
# from rest_framework.generics import ListAPIView, CreateAPIView, \
# RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from apps.news.models import Book
from apps.news.serializers import BookSerializer

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 20

class BooksAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination


# class NewsListAPIView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsCreateAPIView(CreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsUpdateAPIView(UpdateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsRetrievAPIView(RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsDeleteAPIView(DestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer