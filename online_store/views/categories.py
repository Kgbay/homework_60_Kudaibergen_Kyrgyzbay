from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from online_store.models import Category


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_create.html')
    category_data = {
        'name': request.POST.get('name'),
        'desc': request.POST.get('desc')
    }
    category = Category.objects.create(**category_data)
    return redirect('category_view', pk=category.pk)


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category.html', context={
        'category': category
    })


def category_remove_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_confirm_delete.html', context={'category': category})


def category_confirm_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories_view')


def category_update_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.desc = request.POST.get('desc')
        category.save()
        return redirect('category_view', pk=category.pk)
    return render(request, 'category_update.html', context={
        'category': category
    })
