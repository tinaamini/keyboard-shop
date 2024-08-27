# Generated by Django 5.0.6 on 2024-08-27 10:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_baseproducts_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseproducts',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت محصول'),
            preserve_default=False,
        ),
    ]
