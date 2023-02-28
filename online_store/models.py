
from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    desc = models.TextField(max_length=3000, null=True, verbose_name='Описание', default='Описание товара')
    category_id = models.IntegerField(null=False, verbose_name='id категорий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена', )
    img_link = models.TextField(max_length=3000, verbose_name='Ссылка на изображения')
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} - {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    desc = models.TextField(max_length=3000, null=True, verbose_name='Описание', default='Описание товара')
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} - {self.desc}"
        
