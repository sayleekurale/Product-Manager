from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Seed sample Product data"

    def handle(self, *args, **options):
        samples = [
            {"name": "Laptop", "category": "Electronics", "price": 999.99, "stock": 10},
            {"name": "Headphones", "category": "Electronics", "price": 199.99, "stock": 50},
            {"name": "Coffee Mug", "category": "Home", "price": 12.5, "stock": 100},
            {"name": "Notebook", "category": "Stationery", "price": 5.99, "stock": 200},
            {"name": "Office Chair", "category": "Furniture", "price": 149.99, "stock": 15},
        ]
        for s in samples:
            Product.objects.get_or_create(
                name=s["name"],
                defaults={
                    "description": f"Sample {s['name']}",
                    "category": s["category"],
                    "price": s["price"],
                    "stock": s["stock"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Seeded products"))


