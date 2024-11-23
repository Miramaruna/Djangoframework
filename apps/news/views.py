
# from rest_framework import mixins, viewsets
# from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.
from apps.news.models import Students, Transaction
from apps.news.serializers import StudentSerializer, TransactionSerializers, StudentsRegisterSerializer, StudentBalanceSerializers

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class StudentRegisterApiView(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsRegisterSerializer
    pagination_class = Pagination

class StudentTransaktionListApiView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

class StudentListApi(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

class StudentTransaktionCreateApiView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

class StudentBalanceApiView(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentBalanceSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

# class UserCreateAPIView(CreateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentsRegisterSerializer
#     pagination_class = Pagination
#     permission_classes = [IsAuthenticated]