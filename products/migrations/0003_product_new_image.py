# Generated by Django 2.1.5 on 2020-09-29 01:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_image',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]