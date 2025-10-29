from django.contrib import admin
from .models import Product, Category, Supplier, Order, OrderItem, Customer, CurrencyRate


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email", "phone")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "sku", "name", "category", "supplier", "price", "stock", "created_at")
    search_fields = ("sku", "name", "description")
    list_filter = ("category", "supplier", "created_at")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email", "phone")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at")
    list_filter = ("status", "created_at")
    inlines = [OrderItemInline]


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ("date", "base", "symbol", "rate")
    list_filter = ("base", "symbol", "date")
