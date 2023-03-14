from django.db import models

from online_store.models import Product


class Order(models.Model):
    product = models.ManyToManyField(
        Product
    )
    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Имя пользователя')
    phone = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Телефон')
    address = models.CharField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Адрес')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления')
