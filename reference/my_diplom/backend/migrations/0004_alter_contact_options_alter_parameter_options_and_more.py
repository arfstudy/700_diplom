# Generated by Django 5.0.6 on 2024-08-31 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_parameter_category_order_product_productinfo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт пользователя', 'verbose_name_plural': 'Список контактов'},
        ),
        migrations.AlterModelOptions(
            name='parameter',
            options={'ordering': ('name',), 'verbose_name': 'Название параметра', 'verbose_name_plural': 'Список параметров'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Список товаров'},
        ),
        migrations.AlterModelOptions(
            name='productinfo',
            options={'verbose_name': 'Информация о товаре', 'verbose_name_plural': 'Информация о товарах'},
        ),
        migrations.AlterModelOptions(
            name='productparameter',
            options={'verbose_name': 'Значение параметра', 'verbose_name_plural': 'Значения параметров'},
        ),
        migrations.RemoveConstraint(
            model_name='orderitem',
            name='unique_order_item',
        ),
        migrations.AlterField(
            model_name='category',
            name='catalog_number',
            field=models.IntegerField(unique=True, verbose_name='Номер по каталогу'),
        ),
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='backend.contact', verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_infos',
            field=models.ManyToManyField(related_name='orders', through='backend.OrderItem', to='backend.productinfo', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('BS', 'В корзине'), ('NE', 'Новый'), ('CF', 'Подтверждён'), ('AS', 'Собран'), ('SN', 'Отправлен'), ('CN', 'Отменён'), ('RC', 'Получен'), ('DL', 'Удалён')], default='BS', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='backend.productinfo', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='products',
            field=models.ManyToManyField(related_name='parameters', through='backend.ProductParameter', to='backend.productinfo', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='model',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Закупочная цена'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='price_rrc',
            field=models.PositiveIntegerField(default=0, verbose_name='Рекомендуемая розничная цена'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='backend.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_infos', to='backend.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='product_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_parameters', to='backend.productinfo', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Значение параметра'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='state',
            field=models.CharField(choices=[('OP', 'Открыт'), ('CL', 'Закрыт')], max_length=2, verbose_name='Приём заказов'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order', 'product_info'), name='unique_order_item'),
        ),
    ]