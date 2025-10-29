from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProductViewSet, report_inventory, usd_to_inr_rate, kpis, usd_inr_history


router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")


urlpatterns = [
    path("", include(router.urls)),
    path("reports/inventory/", report_inventory, name="report_inventory"),
    path("external/usd_inr/", usd_to_inr_rate, name="usd_to_inr_rate"),
    path("reports/kpis/", kpis, name="kpis"),
    path("external/usd_inr/history/", usd_inr_history, name="usd_inr_history"),
]


