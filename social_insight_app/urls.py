"""
URL configuration for social_insight_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views as products_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_views.home, name='home'),
    path('dashboard/', products_views.dashboard, name='products_dashboard'),
    path('products/', products_views.product_list, name='product_list'),
    path('products/new/', products_views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', products_views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', products_views.product_delete, name='product_delete'),
    path('api/products/', include('products.api_urls')),
]
