# Generated by Django 4.0.3 on 2022-07-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Emi',
            field=models.CharField(choices=[('601', '601-General de Ley Personas Morales'), ('603', '603-Personas Morales con Fines no Lucrativos'), ('605', '605-Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606-Arrendamiento'), ('607', '607-RÃ©gimen de EnajenaciÃ³n o AdquisiciÃ³n de Bienes'), ('608', '608-DemÃ¡s ingresos'), ('610', '610-Residentes en el Extranjero sin Establecimiento Permanente en MÃ©xico'), ('611', '611-Ingresos por Dividendos (socios y accionistas)'), ('612', '612-Personas FÃ\xadsicas con Actividades Empresariales y Profesionales'), ('614', '614-Ingresos por intereses'), ('615', '615-RÃ©gimen de los ingresos por obtenciÃ³n de premios'), ('616', '616-Sin obligaciones fiscales'), ('620', '620-Sociedades Cooperativas de ProducciÃ³n que optan por diferir sus ingresos'), ('621', '621-IncorporaciÃ³n Fiscal'), ('622', '622-Actividades AgrÃ\xadcolas, Ganaderas, SilvÃ\xadcolas y Pesqueras'), ('623', '623-Opcional para Grupos de Sociedades'), ('624', '624-Coordinados'), ('625', '625-RÃ©gimen de las Actividades Empresariales con ingresos a travÃ©s de Plataformas TecnolÃ³gicas'), ('626', '626-RÃ©gimen Simplificado de Confianza')], max_length=4),
        ),
        migrations.AlterField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Rec',
            field=models.CharField(choices=[('601', '601-General de Ley Personas Morales'), ('603', '603-Personas Morales con Fines no Lucrativos'), ('605', '605-Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606-Arrendamiento'), ('607', '607-RÃ©gimen de EnajenaciÃ³n o AdquisiciÃ³n de Bienes'), ('608', '608-DemÃ¡s ingresos'), ('610', '610-Residentes en el Extranjero sin Establecimiento Permanente en MÃ©xico'), ('611', '611-Ingresos por Dividendos (socios y accionistas)'), ('612', '612-Personas FÃ\xadsicas con Actividades Empresariales y Profesionales'), ('614', '614-Ingresos por intereses'), ('615', '615-RÃ©gimen de los ingresos por obtenciÃ³n de premios'), ('616', '616-Sin obligaciones fiscales'), ('620', '620-Sociedades Cooperativas de ProducciÃ³n que optan por diferir sus ingresos'), ('621', '621-IncorporaciÃ³n Fiscal'), ('622', '622-Actividades AgrÃ\xadcolas, Ganaderas, SilvÃ\xadcolas y Pesqueras'), ('623', '623-Opcional para Grupos de Sociedades'), ('624', '624-Coordinados'), ('625', '625-RÃ©gimen de las Actividades Empresariales con ingresos a travÃ©s de Plataformas TecnolÃ³gicas'), ('626', '626-RÃ©gimen Simplificado de Confianza')], max_length=4),
        ),
    ]
