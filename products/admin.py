from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "stock", "created_at")
    search_fields = ("name", "category", "description")
    list_filter = ("category", "created_at")
