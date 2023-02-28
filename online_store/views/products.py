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
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})

def product_confirm_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products_view')

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.desc = request.POST.get('desc')
        product.category_id = request.POST.get('category_id')
        product.price = request.POST.get('price')
        product.img_link = request.POST.get('img_link')
        product.save()
        return redirect('product_view', pk=product.pk)
    return render(request, 'product_update.html', context={
        'product': product,
        'categories': categories
    })

