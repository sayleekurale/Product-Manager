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
from insights import views as insights_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', insights_views.home, name='home'),
    path('dashboard/', insights_views.dashboard, name='dashboard'),
    path('posts/', insights_views.post_list, name='post_list'),
    path('posts/new/', insights_views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', insights_views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', insights_views.post_delete, name='post_delete'),
    path('api/', include('insights.api_urls')),
]
