from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class LaptopListPagination(PageNumberPagination):
    page_size = 10

class LaptopListView(ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LaptopListPagination

class LaptopCreateView(CreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]

class LaptopUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]
    


























