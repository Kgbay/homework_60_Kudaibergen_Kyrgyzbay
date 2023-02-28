from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from online_store.models import Product, Category


# Create your views here.
def products_view(request: WSGIRequest):
    products = Product.objects.exclude(is_deleted=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def categories_view(request):
    categories = Category.objects.exclude(is_deleted=True)
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)




