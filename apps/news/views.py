
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from apps.news.models import Recipe
from apps.news.serializers import RecipeSerializer

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class RecipeViewsSets(ModelViewSet):
    queryset = Recipe.objects.all()
    serializers_class = RecipeSerializer
    pagination_class = Pagination