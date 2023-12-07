from django.db import models


class Laptop(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='laptop_image/')

    def __str__(self):
        return self.brand





































