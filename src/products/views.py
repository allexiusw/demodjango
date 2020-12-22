from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def list_products(request):
    action = "new"
    if request.method == "GET":
        form = ProductForm()
    else:
        form =  ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    rows = Product.objects.all()
    return render(request, "list_products.html", {"rows": rows, 'form': form, "action": action})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk).delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect("list_products")

def edit_product(request, pk):
    action = "update"
    if request.method == "GET":
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    rows = Product.objects.all()
    return render(request, "edit_product.html", {"rows": rows, 'form': form, "action": action})