# Generated by Django 4.1.3 on 2022-11-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='ShopX', max_length=50),
        ),
    ]