from django.contrib import admin

from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price', 'desc')
    search_fields = ('name', 'price')
    fields = ('name', 'desc', 'category_id', 'price')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)