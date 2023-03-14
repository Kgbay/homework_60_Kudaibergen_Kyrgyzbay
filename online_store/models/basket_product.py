from django.db import models
from django.utils import timezone

from online_store.models import Product


class Basket_product(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        default=5
    )
    amount = models.PositiveIntegerField(
        null=False,
        default=0,
        verbose_name='Количество'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления')
    in_basket = models.BooleanField(
        verbose_name='В корзине',
        null=False,
        default=False
    )
    added_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None)

    def add(self, using=None, keep_parents=False):
        self.in_basket = True
        self.added_at = timezone.now()
        self.save()
