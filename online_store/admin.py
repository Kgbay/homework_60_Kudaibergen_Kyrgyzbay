from django.contrib import admin

from online_store.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'category_name', 'residue', 'is_deleted')
    list_filter = ('name', 'price', 'desc')
    search_fields = ('name', 'price')
    fields = ('name', 'category_name', 'price', 'img_link', 'residue', 'desc', 'is_deleted')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)