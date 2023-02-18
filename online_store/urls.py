from django.urls import path

from source.online_store.views.base import index_view
from source.online_store.views.products import add_view

urlpatterns = [
    path("", index_view),
    path("product/add", add_view)
]