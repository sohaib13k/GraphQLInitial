from django.contrib import admin
from .models import ProductModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    pass