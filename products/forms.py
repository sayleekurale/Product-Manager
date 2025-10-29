from django import forms
from .models import Product, Category, Supplier


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)

    class Meta:
        model = Product
        fields = ["sku", "name", "description", "category", "supplier", "cost_price", "price", "stock"]


