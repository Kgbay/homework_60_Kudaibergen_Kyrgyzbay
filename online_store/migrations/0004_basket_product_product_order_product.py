# Generated by Django 4.1.7 on 2023-03-14 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_basket_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket_product',
            name='product',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='online_store.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='online_store.product'),
        ),
    ]
