from django.db import models
from django.utils import timezone


class ProductModel(models.Model):
    segment = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    units = models.IntegerField()
    sales = models.IntegerField()
    date_sold = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.product