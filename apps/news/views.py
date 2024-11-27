
# from rest_framework import mixins, viewsets
# from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.
from apps.news.models import User, ToDo
from apps.news.serializers import UserRegisterSerializer, UserSerializers, ToDoSerializer, CreateToDoSerializers

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class DeleteAllToDoApiView(ListAPIView):
    queryset = ToDo.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        otvet = ToDo.objects.all().delete()
        return otvet({"message": "Все записи удалены их вообще нету пон?"}, status=204)

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated,]

class TodoCreateApiView(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = CreateToDoSerializers
    permission_classes = [IsAuthenticated,]

class ToDoApiView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = Pagination
