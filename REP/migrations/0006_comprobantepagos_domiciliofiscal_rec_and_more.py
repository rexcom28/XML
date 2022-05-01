# Generated by Django 4.0.3 on 2022-04-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REP', '0005_alter_comprobantepagos_condicionesdepago_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantepagos',
            name='DomicilioFiscal_Rec',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='FacAtrAdquirente',
            field=models.CharField(blank=True, default='NA', editable=False, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='FacAtrAdquirente_Emi',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='Nombre_Emi',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='Nombre_Rec',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='NumRegIdTrib_Rec',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Emi',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Rec',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='ResidenciaFiscal_Rec',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='Rfc_Emi',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='Rfc_Rec',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobantepagos',
            name='UsoCFDI_Rec',
            field=models.CharField(blank=True, default='CP01', max_length=4, null=True),
        ),
    ]
