# Generated by Django 5.0.6 on 2024-08-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseproducts',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
