from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.news.views import RecipeViewsSets

router = DefaultRouter()
router.register("recipe_viewsets", RecipeViewsSets, basename='api-recipe')

urlpatterns = [
    path('recipe/', include(router.urls))
]

# urlpatterns += router.urls