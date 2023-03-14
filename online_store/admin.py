from django.contrib import admin

from online_store.models import Product, Order, Basket_product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'category_name', 'residue', 'is_deleted')
    list_filter = ('name', 'price', 'desc')
    search_fields = ('name', 'price')
    fields = ('name', 'category_name', 'price', 'img_link', 'residue', 'desc', 'is_deleted')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'address', 'created_at')
    list_filter = ('username', 'created_at')
    search_fields = ('username', 'phone')
    fields = ('username', 'phone', 'address')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Order, OrderAdmin)


class BasketProduct(admin.ModelAdmin):
    list_display = ('amount', 'product', 'in_basket', 'created_at')
    list_filter = ('amount',  'in_basket', 'created_at')
    search_fields = ('amount', 'in_basket')
    fields = ('amount', 'in_basket', 'product')


admin.site.register(Basket_product, BasketProduct)
