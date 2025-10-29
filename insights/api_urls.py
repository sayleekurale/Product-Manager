from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import SocialPostViewSet, report_posts_summary, coin_prices


router = DefaultRouter()
router.register(r"posts", SocialPostViewSet, basename="post")


urlpatterns = [
    path("", include(router.urls)),
    path("reports/posts_summary/", report_posts_summary, name="report_posts_summary"),
    path("external/coin_prices/", coin_prices, name="coin_prices"),
]


