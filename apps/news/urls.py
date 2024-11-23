from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.news.views import StudentListApi, StudentTransaktionListApiView, StudentTransaktionCreateApiView, StudentRegisterApiView, StudentBalanceApiView
# from .serializers import StudentTransaktionCreateApiView

router = DefaultRouter()
# router.register("s_viewsets", RecipeViewsSets, basename='api-recipe')

urlpatterns = [
    path('users/', StudentListApi.as_view(), name='users'),
    path('register/', StudentRegisterApiView.as_view(), name='register'),
    path('transaction/', StudentTransaktionListApiView.as_view(), name='transaction'),
    path('transaction/add', StudentTransaktionCreateApiView.as_view(), name='transactionadd'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('balance/', StudentBalanceApiView.as_view(), name='balance')
]

# urlpatterns += router.urls