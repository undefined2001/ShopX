# Generated by Django 4.1.3 on 2022-11-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='none', upload_to=''),
            preserve_default=False,
        ),
    ]