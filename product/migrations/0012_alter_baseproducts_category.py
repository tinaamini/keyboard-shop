# Generated by Django 5.0.6 on 2024-11-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_category_is_sub_category_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproducts',
            name='category',
            field=models.ManyToManyField(related_name='products', to='product.category'),
        ),
    ]
