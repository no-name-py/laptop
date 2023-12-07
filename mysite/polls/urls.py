from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('laptop_list/', LaptopListView.as_view(), name='laptop_list'),
    path('sell_laptop/', LaptopCreateView.as_view(), name='sell_laptop'),
    path('manage_laptop/<int:pk>/', LaptopUpdateDeleteView.as_view(), name='manage_laptop')
]































