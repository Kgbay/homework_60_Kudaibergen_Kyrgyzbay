from django.views.generic import ListView, TemplateView
from online_store.models import Basket_product
from online_store.models import Product


class BasketView(ListView):
    template_name = 'basket.html'
    model = Basket_product
    context_object_name = 'basket_products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'products': Product.objects.all(),
        })
        return context

class BasketAddView(TemplateView):
    template_name = 'index'
    model = Basket_product



