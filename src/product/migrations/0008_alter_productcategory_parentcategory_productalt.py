# Generated by Django 4.2 on 2023-04-28 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productcategory_parentcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='ParentCategory',
            field=models.ForeignKey(blank=True, limit_choices_to={'ParentCategory__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
        ),
        migrations.CreateModel(
            name='ProductAlt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alternative', models.ManyToManyField(related_name='alternative_products', to='product.product', verbose_name='product alternative')),
                ('PLAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product', verbose_name='product plan')),
            ],
            options={
                'verbose_name': 'Alternative',
                'verbose_name_plural': 'Alternatives',
            },
        ),
    ]
