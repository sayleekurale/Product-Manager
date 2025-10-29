from rest_framework import serializers
from .models import Product, Category, Supplier, Order, OrderItem, CurrencyRate


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "phone", "address"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source="category", queryset=Category.objects.all(), write_only=True, required=False, allow_null=True)
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(source="supplier", queryset=Supplier.objects.all(), write_only=True, required=False, allow_null=True)

    class Meta:
        model = Product
        fields = [
            "id", "sku", "name", "description",
            "category", "category_id", "supplier", "supplier_id",
            "cost_price", "price", "stock", "created_at"
        ]
        read_only_fields = ["id", "created_at", "category", "supplier"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(source="product", queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_id", "quantity", "unit_price", "subtotal"]
        read_only_fields = ["id", "subtotal", "product"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "status", "created_at", "items", "total_amount"]
        read_only_fields = ["id", "created_at", "total_amount"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if items_data is not None:
            instance.items.all().delete()
            for item in items_data:
                OrderItem.objects.create(order=instance, **item)
        return instance


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ["id", "base", "symbol", "date", "rate"]


