# Generated by Django 4.2.5 on 2023-11-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0010_rename_cantidadtotal_venta_cantidadproductos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='caracteristicas',
            field=models.TextField(max_length=500),
        ),
    ]
