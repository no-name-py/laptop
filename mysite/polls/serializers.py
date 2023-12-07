from rest_framework import serializers
from .models import Laptop

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['brand', 'model', 'cpu', 'ram', 'price', 'image', 'id']





