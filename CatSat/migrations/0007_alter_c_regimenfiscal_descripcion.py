# Generated by Django 4.0.3 on 2022-05-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatSat', '0006_alter_c_moneda_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_regimenfiscal',
            name='Descripcion',
            field=models.CharField(max_length=101),
        ),
    ]
