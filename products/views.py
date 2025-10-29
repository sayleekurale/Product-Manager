from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def home(request):
    return redirect("products_dashboard")


def dashboard(request):
    return render(request, "products/dashboard.html")


def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "products/list.html", {"products": products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created.")
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/form.html", {"form": form, "mode": "Create"})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated.")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/form.html", {"form": form, "mode": "Edit"})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect("product_list")
    return render(request, "products/confirm_delete.html", {"product": product})

