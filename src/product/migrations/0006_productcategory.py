# Generated by Django 4.1.7 on 2023-04-25 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productimage_proiimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=30)),
                ('Des_Category', models.TextField()),
                ('Category_Image', models.ImageField(upload_to='category/')),
                ('ParentCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory')),
            ],
        ),
    ]
