# Generated by Django 4.2 on 2023-05-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_proiimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='proslug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]