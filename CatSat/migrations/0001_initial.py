# Generated by Django 4.0.3 on 2022-07-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='c_Aduana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aduana', models.CharField(max_length=3)),
                ('Patente', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='c_ClaveProdServ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductoServ', models.CharField(max_length=8)),
                ('Descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='c_ClaveUnidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClaveUnidad', models.CharField(max_length=5)),
                ('Nombre', models.CharField(max_length=150)),
                ('Descripcion', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='c_CodigoPostal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoPostal', models.CharField(max_length=5)),
                ('Estado_c', models.CharField(max_length=3)),
                ('Municipio_c', models.CharField(blank=True, max_length=3, null=True)),
                ('Localidad_c', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colonia', models.CharField(max_length=5)),
                ('Codigo_c', models.CharField(blank=True, max_length=5, null=True)),
                ('NombreAsentamiento', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=4)),
                ('Pais_c', models.CharField(blank=True, max_length=3, null=True)),
                ('Nombre_estado', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FormaPago', models.CharField(max_length=2)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='c_Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Localidad', models.CharField(max_length=5)),
                ('Estado_c', models.CharField(blank=True, max_length=3, null=True)),
                ('Descripcion', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moneda', models.CharField(max_length=3)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='c_Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Municipio', models.CharField(max_length=4)),
                ('Estado_c', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pais', models.CharField(max_length=3)),
                ('Descripcion', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='c_PatenteAduanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patente', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='c_RegimenFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regimen', models.CharField(max_length=3)),
                ('Descripcion', models.CharField(max_length=101)),
                ('Fisica', models.BooleanField(blank=True, null=True)),
                ('Moral', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_TipoRelacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Relacion', models.CharField(max_length=2)),
                ('Descripcion', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_UsoCFDI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uso', models.CharField(max_length=4)),
                ('Descripcion', models.CharField(max_length=150)),
            ],
        ),
    ]
