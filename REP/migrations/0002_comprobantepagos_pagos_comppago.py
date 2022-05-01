# Generated by Django 4.0.3 on 2022-04-21 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('REP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobantePagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Version', models.CharField(default='4.0', max_length=5)),
                ('Serie', models.CharField(blank=True, max_length=25)),
                ('Folio', models.CharField(blank=True, max_length=40)),
                ('Fecha', models.DateTimeField(blank=True)),
                ('TipoCambio', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('Moneda', models.CharField(default='MXN', max_length=3)),
                ('FormaPago', models.CharField(blank=True, choices=[('1', '1-Efectivo'), ('2', '2-Cheque nominativo'), ('3', '3-Transferencia electrónica de fondos'), ('4', '4-Tarjeta de crédito'), ('5', '5-Monedero electrónico'), ('6', '6-Dinero electrónico'), ('8', '8-Vales de despensa'), ('12', '12-Dación en pago'), ('13', '13-Pago por subrogación'), ('14', '14-Pago por consignación'), ('15', '15-Condonación'), ('17', '17-Compensación'), ('23', '23-Novación'), ('24', '24-Confusión'), ('25', '25-Remisión de deuda'), ('26', '26-Prescripción o caducidad'), ('27', '27-A satisfacción del acreedor'), ('28', '28-Tarjeta de débito'), ('29', '29-Tarjeta de servicios'), ('30', '30-Aplicación de anticipos'), ('31', '31-Intermediario pagos'), ('99', '99-Por definir')], max_length=2, null=True)),
                ('Exportacion', models.CharField(choices=[('01', '01-No aplica'), ('02', '02-Definitiva'), ('03', '03-Temporal')], default='01', max_length=2)),
                ('MetodoPago', models.CharField(blank=True, choices=[('PUE', 'PUE-Pago en una sola exhibición'), ('PPD', 'PPD-Pago en parcialidades o diferido')], default='PPD', max_length=4, null=True)),
                ('LugarExpedicion', models.CharField(max_length=5)),
                ('TipoDeComprobante', models.CharField(default='I', max_length=3)),
                ('NoCertificado', models.CharField(blank=True, max_length=20)),
                ('Certificado', models.TextField(blank=True)),
                ('Sello', models.TextField(blank=True)),
                ('SubTotal', models.DecimalField(blank=True, decimal_places=6, max_digits=21, null=True)),
                ('Descuento', models.DecimalField(blank=True, decimal_places=6, max_digits=11, null=True)),
                ('CondicionesDePago', models.CharField(blank=True, max_length=1000, null=True)),
                ('Total', models.DecimalField(decimal_places=6, max_digits=21, null=True)),
                ('Confirmacion', models.CharField(blank=True, max_length=5, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('Estado_CFDI', models.CharField(blank=True, default='NUEVO', max_length=20)),
                ('IVA', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True)),
                ('IVA_Ret', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True)),
                ('ISR', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pagos',
            name='CompPago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REP.comprobantepagos'),
        ),
    ]
