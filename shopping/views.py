from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product, ProductCategory

def index(request):
    all_added_products = Product.objects.all()
    context = {'all_added_products': all_added_products}
    return render(request, 'shopping/index.html', context)

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shopping/product_details.html', {'product': product})

def change_category_form(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shopping/change_category.html', {'product': product})

def change_category(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        new_category = ProductCategory.objects.filter(pk=request.POST['category'])
    except (KeyError, Product.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'shopping/change_category.html', {
            'product': product,
            'error_message': "You didn't select a category.",
        })
    else:
        product.product_category_code = new_category
        product.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('shopping:product_details', args=(product.id)))

