# Generated by Django 3.2.13 on 2023-02-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Burutma', 'verbose_name_plural': 'Burutmalar'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Maxsulot Buyurtmasi', 'verbose_name_plural': 'Maxsulot Buyurtmalari'},
        ),
        migrations.AlterModelOptions(
            name='shopcart',
            options={'verbose_name': "Do'kon savati", 'verbose_name_plural': "Do'konlar savati"},
        ),
    ]
