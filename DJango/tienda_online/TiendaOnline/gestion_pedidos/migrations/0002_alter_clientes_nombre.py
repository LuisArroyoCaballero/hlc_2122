# Generated by Django 4.0.2 on 2022-02-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre completo del Cliente'),
        ),
    ]
