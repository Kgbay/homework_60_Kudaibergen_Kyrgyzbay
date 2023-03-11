from django.urls import path

from online_store.views.base import ProductView
from online_store.views.products import ProductDetail, ProductCreateView, ProductUpdateView, TaskDeleteView

urlpatterns = [
    path("", ProductView.as_view(), name='products_view'),
    path("products/", ProductView.as_view(), name='products_view'),
    path("products/<int:pk>", ProductDetail.as_view(), name='product_view'),
    path("products/add/", ProductCreateView.as_view(), name='product_add'),
    path("products/<int:pk>/remove/", TaskDeleteView.as_view(), name='remove_product'),
    path("products/<int:pk>/confirm_remove/", TaskDeleteView.as_view(), name='confirm_remove_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]