from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from online_store.models import Product, Category

def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'product_create.html', context=context)
    product_data = {
        'name': request.POST.get('name'),
        'desc': request.POST.get('desc'),
        'category_id': request.POST.get('category_id'),
        'price': request.POST.get('price'),
        'img_link': request.POST.get('img_link')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_view', pk=product.pk)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    return render(request, 'product.html', context={
        'product': product,
        'categories': categories
    })

def product_remove_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    product.delete()
    return render(request, 'remove_product.html', context=context)
