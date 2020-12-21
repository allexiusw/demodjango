from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Product
from .forms import ProductForm

def list_products(request):
    if request.method == "GET":
        form = ProductForm()
    else:
        form =  ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    rows = Product.objects.all()
    return render(request, "list_products.html", {"rows": rows, 'form': form})
