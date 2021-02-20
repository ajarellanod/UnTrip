# Generated by Django 3.1.6 on 2021-02-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210220_1413'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='asiento',
            constraint=models.UniqueConstraint(fields=('ruta', 'pasajero'), name='unique-pasajero'),
        ),
    ]
