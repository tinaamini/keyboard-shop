# Generated by Django 5.0.6 on 2024-11-27 11:11

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_value_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='colors',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=None, verbose_name='مقدار'),
        ),
    ]