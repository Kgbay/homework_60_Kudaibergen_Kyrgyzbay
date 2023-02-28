from django.urls import path

from online_store.views.base import products_view
from online_store.views.products import product_view, product_add_view, product_remove_view, product_confirm_remove, product_update_view

urlpatterns = [
    path("", products_view, name='products_view'),
    path("products/", products_view, name='products_view'),
    path("products/<int:pk>", product_view, name='product_view'),
    path("products/add/", product_add_view, name='product_add'),
    path("products/<int:pk>/remove/", product_remove_view, name='remove_product'),
    path("products/<int:pk>/confirm_remove/", product_confirm_remove, name='confirm_remove_product'),
    path('product/<int:pk>/update/', product_update_view, name='product_update'),
]