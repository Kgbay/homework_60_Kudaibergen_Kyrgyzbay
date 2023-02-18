from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def add_view(request: WSGIRequest):
    return render(request, 'product_create.html')