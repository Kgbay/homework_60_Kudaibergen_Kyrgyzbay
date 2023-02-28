from django.urls import path

from online_store.views.base import products_view, categories_view
from online_store.views.products import product_view, product_add_view, product_remove_view, product_confirm_remove, product_update_view
from online_store.views.categories import category_add_view, category_view, category_remove_view, category_confirm_remove, category_update_view

urlpatterns = [
    path("", products_view, name='products_view'),
    path("products/", products_view, name='products_view'),
    path("products/<int:pk>", product_view, name='product_view'),
    path("products/add/", product_add_view, name='product_add'),
    path("categories/add/", category_add_view, name='category_add'),
    path("categories/<int:pk>", category_view, name='category_view'),
    path("categories/", categories_view, name='categories_view'),

    path("categories/<int:pk>/remove/", category_remove_view, name='remove_category'),
    path("categories/<int:pk>/confirm_remove/", category_confirm_remove, name='confirm_remove_category'),

    path("products/<int:pk>/remove/", product_remove_view, name='remove_product'),
    path("products/<int:pk>/confirm_remove/", product_confirm_remove, name='confirm_remove_product'),

    path('product/<int:pk>/update/', product_update_view, name='product_update'),
    path('categories/<int:pk>/update/', category_update_view, name='category_update'),
]