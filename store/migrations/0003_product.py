# Generated by Django 4.1.3 on 2022-11-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TimeField()),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing')], max_length=30)),
            ],
        ),
    ]
