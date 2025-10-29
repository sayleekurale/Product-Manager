from django.db.models import Sum, Count, Avg, F
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, timedelta
from .models import Product, CurrencyRate
from .serializers import ProductSerializer, CurrencyRateSerializer
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
        # upsert today's rate into CurrencyRate
        if rate is not None:
            CurrencyRate.objects.update_or_create(
                base="USD", symbol="INR", date=date.today(),
                defaults={"rate": rate}
            )
        return Response({"USD_INR": rate})
    except Exception as e:
        return Response({"error": str(e)}, status=502)

@api_view(["GET"])
def kpis(request):
    total_products = Product.objects.count()
    total_stock_units = Product.objects.aggregate(total=Sum("stock"))['total'] or 0
    inventory_value = Product.objects.aggregate(
        value=Sum(F("stock") * F("cost_price"))
    )["value"] or 0
    return Response({
        "total_products": total_products,
        "total_stock_units": total_stock_units,
        "inventory_value": float(inventory_value),
    })


@api_view(["GET"])
def usd_inr_history(request):
    days = int(request.GET.get("days", 30))
    start = date.today() - timedelta(days=days)
    qs = CurrencyRate.objects.filter(base="USD", symbol="INR", date__gte=start).order_by("date")
    return Response(CurrencyRateSerializer(qs, many=True).data)


