from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("fulfilled", "Fulfilled"),
        ("cancelled", "Cancelled"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self) -> str:
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def __str__(self) -> str:
        return f"{self.product} x {self.quantity}"


class CurrencyRate(models.Model):
    base = models.CharField(max_length=10, default="USD")
    symbol = models.CharField(max_length=10, default="INR")
    date = models.DateField()
    rate = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        unique_together = ("base", "symbol", "date")
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.base}->{self.symbol} {self.date}: {self.rate}"
