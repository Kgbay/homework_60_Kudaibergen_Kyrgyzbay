from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from online_store.models import Product


# Create your views here.
def products_view(request: WSGIRequest):
    products = Product.objects.exclude(is_deleted=True)
    context = {
        'products': products,
    }
    return render(request, 'index.html', context=context)






