from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    all_added_products = Product.objects.filter(product_added=True)
    context = {'all_added_products': all_added_products}
    return render(request, 'shopping/index.html', context)
