import requests
from django.db.models import Count, Avg
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SocialPost
from .serializers import SocialPostSerializer


class SocialPostViewSet(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by("-created_at")
    serializer_class = SocialPostSerializer


@api_view(["GET"])
def report_posts_summary(request):
    data = (
        SocialPost.objects
        .extra(select={"body_len": "length(body)"})
        .aggregate(
            count=Count("id"),
            avg_length=Avg("body_len"),
        )
    )
    return Response(data)


@api_view(["GET"])
def coin_prices(request):
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart",
            params={"vs_currency": "usd", "days": 1, "interval": "hourly"},
            timeout=10,
        )
        r.raise_for_status()
        payload = r.json()
        prices = payload.get("prices", [])[:200]
        return Response({"prices": prices})
    except Exception as e:
        return Response({"error": str(e)}, status=502)


