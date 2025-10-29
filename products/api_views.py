from django.db.models import Sum, Count, Avg
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
import requests


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer


@api_view(["GET"])
def report_inventory(request):
    data = Product.objects.values("category").annotate(
        total_stock=Sum("stock"),
        avg_price=Avg("price"),
        count=Count("id")
    ).order_by("category")
    return Response(list(data))


@api_view(["GET"])
def usd_to_inr_rate(request):
    # Simple external API: fetch USD->INR conversion rate
    try:
        r = requests.get("https://api.exchangerate.host/latest", params={"base": "USD", "symbols": "INR"}, timeout=10)
        r.raise_for_status()
        rate = r.json().get("rates", {}).get("INR")
        return Response({"USD_INR": rate})
    except Exception as e:
        return Response({"error": str(e)}, status=502)


