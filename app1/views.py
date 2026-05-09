from django.shortcuts import render, redirect, get_object_or_404
from . models import Products
from . forms import products_form

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products_list(request):
    product = Products.objects.all()
    return render (request, 'products.html', {'product': product})
    

def add_products(request):
    if request.method == 'POST':
        form = products_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('products_list')
    else:
        form = products_form()
    return render (request, 'add_products.html', {'form': form})

def update_products(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = products_form(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = products_form(instance=product)
    return render(request, 'update_products.html', {'form': form, 'product':product})


def delete_products(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    return render(request, 'delete_products.html', {'product': product})

