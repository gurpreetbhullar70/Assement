# Generated by Django 3.2 on 2022-06-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_dimension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dimension',
            field=models.CharField(max_length=254),
        ),
    ]