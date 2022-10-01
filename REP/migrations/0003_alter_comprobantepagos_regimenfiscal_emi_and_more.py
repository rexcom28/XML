# Generated by Django 4.0.3 on 2022-09-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REP', '0002_alter_comprobantepagos_regimenfiscal_emi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Emi',
            field=models.CharField(choices=[('603', '603-Personas Morales con Fines no Lucrativos'), ('605', '605-Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606-Arrendamiento'), ('607', '607-Régimen de Enajenación o Adquisición de Bienes'), ('608', '608-Demás ingresos'), ('610', '610-Residentes en el Extranjero sin Establecimiento Permanente en México'), ('611', '611-Ingresos por Dividendos (socios y accionistas)'), ('612', '612-Personas Físicas con Actividades Empresariales y Profesionales'), ('614', '614-Ingresos por intereses'), ('615', '615-Régimen de los ingresos por obtención de premios'), ('616', '616-Sin obligaciones fiscales'), ('620', '620-Sociedades Cooperativas de Producción que optan por diferir sus ingresos'), ('621', '621-Incorporación Fiscal'), ('622', '622-Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'), ('623', '623-Opcional para Grupos de Sociedades'), ('624', '624-Coordinados'), ('625', '625-Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas'), ('626', '626-Régimen Simplificado de Confianza')], max_length=4),
        ),
        migrations.AlterField(
            model_name='comprobantepagos',
            name='RegimenFiscal_Rec',
            field=models.CharField(choices=[('603', '603-Personas Morales con Fines no Lucrativos'), ('605', '605-Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606-Arrendamiento'), ('607', '607-Régimen de Enajenación o Adquisición de Bienes'), ('608', '608-Demás ingresos'), ('610', '610-Residentes en el Extranjero sin Establecimiento Permanente en México'), ('611', '611-Ingresos por Dividendos (socios y accionistas)'), ('612', '612-Personas Físicas con Actividades Empresariales y Profesionales'), ('614', '614-Ingresos por intereses'), ('615', '615-Régimen de los ingresos por obtención de premios'), ('616', '616-Sin obligaciones fiscales'), ('620', '620-Sociedades Cooperativas de Producción que optan por diferir sus ingresos'), ('621', '621-Incorporación Fiscal'), ('622', '622-Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'), ('623', '623-Opcional para Grupos de Sociedades'), ('624', '624-Coordinados'), ('625', '625-Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas'), ('626', '626-Régimen Simplificado de Confianza')], max_length=4),
        ),
        migrations.AlterField(
            model_name='comprobantepagos',
            name='ResidenciaFiscal_Rec',
            field=models.CharField(blank=True, choices=[('ALA', 'ALA-Islas Aland'), ('ALB', 'ALB-Albania'), ('DEU', 'DEU-Alemania'), ('AND', 'AND-Andorra'), ('AGO', 'AGO-Angola'), ('AIA', 'AIA-Anguila'), ('ATA', 'ATA-Antartida'), ('ATG', 'ATG-Antigua y Barbuda'), ('SAU', 'SAU-Arabia Saudita'), ('DZA', 'DZA-Argelia'), ('ARG', 'ARG-Argentina'), ('ARM', 'ARM-Armenia'), ('ABW', 'ABW-Aruba'), ('AUS', 'AUS-Australia'), ('AUT', 'AUT-Austria'), ('AZE', 'AZE-Azerbaiyan'), ('BHS', 'BHS-Bahamas (las)'), ('BGD', 'BGD-Banglades'), ('BRB', 'BRB-Barbados'), ('BHR', 'BHR-Barein'), ('BEL', 'BEL-Belgica'), ('BLZ', 'BLZ-Belice'), ('BEN', 'BEN-Benin'), ('BMU', 'BMU-Bermudas'), ('BLR', 'BLR-Bielorrusia'), ('MMR', 'MMR-Myanmar'), ('BOL', 'BOL-Bolivia, Estado Plurinacional de'), ('BIH', 'BIH-Bosnia y Herzegovina'), ('BWA', 'BWA-Botsuana'), ('BRA', 'BRA-Brasil'), ('BRN', 'BRN-Brunei Darussalam'), ('BGR', 'BGR-Bulgaria'), ('BFA', 'BFA-Burkina Faso'), ('BDI', 'BDI-Burundi'), ('BTN', 'BTN-Butan'), ('CPV', 'CPV-Cabo Verde'), ('KHM', 'KHM-Camboya'), ('CMR', 'CMR-Camerun'), ('CAN', 'CAN-Canada'), ('QAT', 'QAT-Catar'), ('BES', 'BES-Bonaire, San Eustaquio y Saba'), ('TCD', 'TCD-Chad'), ('CHL', 'CHL-Chile'), ('CHN', 'CHN-China'), ('CYP', 'CYP-Chipre'), ('COL', 'COL-Colombia'), ('COM', 'COM-Comoras'), ('PRK', 'PRK-Corea (la Republica Democratica Popular de)'), ('KOR', 'KOR-Corea (la Republica de)'), ('CIV', "CIV-Cote d'Ivoire"), ('CRI', 'CRI-Costa Rica'), ('HRV', 'HRV-Croacia'), ('CUB', 'CUB-Cuba'), ('CUW', 'CUW-Curacao'), ('DNK', 'DNK-Dinamarca'), ('DMA', 'DMA-Dominica'), ('ECU', 'ECU-Ecuador'), ('EGY', 'EGY-Egipto'), ('SLV', 'SLV-El Salvador'), ('ARE', 'ARE-Emiratos Arabes Unidos (Los)'), ('ERI', 'ERI-Eritrea'), ('SVK', 'SVK-Eslovaquia'), ('SVN', 'SVN-Eslovenia'), ('ESP', 'ESP-Espana'), ('USA', 'USA-Estados Unidos (los)'), ('EST', 'EST-Estonia'), ('ETH', 'ETH-Etiopia'), ('PHL', 'PHL-Filipinas (las)'), ('FIN', 'FIN-Finlandia'), ('FJI', 'FJI-Fiyi'), ('FRA', 'FRA-Francia'), ('GAB', 'GAB-Gabon'), ('GMB', 'GMB-Gambia (La)'), ('GEO', 'GEO-Georgia'), ('GHA', 'GHA-Ghana'), ('GIB', 'GIB-Gibraltar'), ('GRD', 'GRD-Granada'), ('GRC', 'GRC-Grecia'), ('GRL', 'GRL-Groenlandia'), ('GLP', 'GLP-Guadalupe'), ('GUM', 'GUM-Guam'), ('GTM', 'GTM-Guatemala'), ('GUF', 'GUF-Guayana Francesa'), ('GGY', 'GGY-Guernsey'), ('GIN', 'GIN-Guinea'), ('GNB', 'GNB-Guinea-Bisau'), ('GNQ', 'GNQ-Guinea Ecuatorial'), ('GUY', 'GUY-Guyana'), ('HTI', 'HTI-Haiti'), ('HND', 'HND-Honduras'), ('HKG', 'HKG-Hong Kong'), ('HUN', 'HUN-Hungria'), ('IND', 'IND-India'), ('IDN', 'IDN-Indonesia'), ('IRQ', 'IRQ-Irak'), ('IRN', 'IRN-Iran (la Republica Islamica de)'), ('IRL', 'IRL-Irlanda'), ('BVT', 'BVT-Isla Bouvet'), ('IMN', 'IMN-Isla de Man'), ('CXR', 'CXR-Isla de Navidad'), ('NFK', 'NFK-Isla Norfolk'), ('ISL', 'ISL-Islandia'), ('CYM', 'CYM-Islas Caiman (las)'), ('CCK', 'CCK-Islas Cocos (Keeling)'), ('COK', 'COK-Islas Cook (las)'), ('FRO', 'FRO-Islas Feroe (las)'), ('SGS', 'SGS-Georgia del sur y las islas sandwich del sur'), ('HMD', 'HMD-Isla Heard e Islas McDonald'), ('FLK', 'FLK-Islas Malvinas [Falkland] (las)'), ('MNP', 'MNP-Islas Marianas del Norte (las)'), ('MHL', 'MHL-Islas Marshall (las)'), ('PCN', 'PCN-Pitcairn'), ('SLB', 'SLB-Islas Salomon (las)'), ('TCA', 'TCA-Islas Turcas y Caicos (las)'), ('UMI', 'UMI-Islas de Ultramar Menores de Estados Unidos (las)'), ('VGB', 'VGB-Islas Virgenes (Britanicas)'), ('VIR', 'VIR-Islas Virgenes (EE.UU.)'), ('ISR', 'ISR-Israel'), ('ITA', 'ITA-Italia'), ('JAM', 'JAM-Jamaica'), ('JPN', 'JPN-Japon'), ('JEY', 'JEY-Jersey'), ('JOR', 'JOR-Jordania'), ('KAZ', 'KAZ-Kazajistan'), ('KEN', 'KEN-Kenia'), ('KGZ', 'KGZ-Kirguistan'), ('KIR', 'KIR-Kiribati'), ('KWT', 'KWT-Kuwait'), ('LAO', 'LAO-Lao, (la) Republica Democratica Popular'), ('LSO', 'LSO-Lesoto'), ('LVA', 'LVA-Letonia'), ('LBN', 'LBN-Libano'), ('LBR', 'LBR-Liberia'), ('LBY', 'LBY-Libia'), ('LIE', 'LIE-Liechtenstein'), ('LTU', 'LTU-Lituania'), ('LUX', 'LUX-Luxemburgo'), ('MAC', 'MAC-Macao'), ('MDG', 'MDG-Madagascar'), ('MYS', 'MYS-Malasia'), ('MWI', 'MWI-Malaui'), ('MDV', 'MDV-Maldivas'), ('MLI', 'MLI-Mali'), ('MLT', 'MLT-Malta'), ('MAR', 'MAR-Marruecos'), ('MTQ', 'MTQ-Martinica'), ('MUS', 'MUS-Mauricio'), ('MRT', 'MRT-Mauritania'), ('MYT', 'MYT-Mayotte'), ('MEX', 'MEX-Mexico'), ('FSM', 'FSM-Micronesia (los Estados Federados de)'), ('MDA', 'MDA-Moldavia (la Republica de)'), ('MCO', 'MCO-Monaco'), ('MNG', 'MNG-Mongolia'), ('MNE', 'MNE-Montenegro'), ('MSR', 'MSR-Montserrat'), ('MOZ', 'MOZ-Mozambique'), ('NAM', 'NAM-Namibia'), ('NRU', 'NRU-Nauru'), ('NPL', 'NPL-Nepal'), ('NIC', 'NIC-Nicaragua'), ('NER', 'NER-Niger (el)'), ('NGA', 'NGA-Nigeria'), ('NIU', 'NIU-Niue'), ('NOR', 'NOR-Noruega'), ('NCL', 'NCL-Nueva Caledonia'), ('NZL', 'NZL-Nueva Zelanda'), ('OMN', 'OMN-Oman'), ('NLD', 'NLD-Paises Bajos (los)'), ('PAK', 'PAK-Pakistan'), ('PLW', 'PLW-Palaos'), ('PSE', 'PSE-Palestina, Estado de'), ('PAN', 'PAN-Panama'), ('PNG', 'PNG-Papua Nueva Guinea'), ('PRY', 'PRY-Paraguay'), ('PER', 'PER-Peru'), ('PYF', 'PYF-Polinesia Francesa'), ('POL', 'POL-Polonia'), ('PRT', 'PRT-Portugal'), ('PRI', 'PRI-Puerto Rico'), ('GBR', 'GBR-Reino Unido (el)'), ('CAF', 'CAF-Republica Centroafricana (la)'), ('CZE', 'CZE-Republica Checa (la)'), ('MKD', 'MKD-Macedonia (la antigua Republica Yugoslava de)'), ('COG', 'COG-Congo'), ('COD', 'COD-Congo (la Republica Democratica del)'), ('DOM', 'DOM-Republica Dominicana (la)'), ('REU', 'REU-Reunion'), ('RWA', 'RWA-Ruanda'), ('ROU', 'ROU-Rumania'), ('RUS', 'RUS-Rusia, (la) Federacion de'), ('ESH', 'ESH-Sahara Occidental'), ('WSM', 'WSM-Samoa'), ('ASM', 'ASM-Samoa Americana'), ('BLM', 'BLM-San Bartolome'), ('KNA', 'KNA-San Cristobal y Nieves'), ('SMR', 'SMR-San Marino'), ('MAF', 'MAF-San Martin (parte francesa)'), ('SPM', 'SPM-San Pedro y Miquelon'), ('VCT', 'VCT-San Vicente y las Granadinas'), ('SHN', 'SHN-Santa Helena, Ascension y Tristan de Acuna'), ('LCA', 'LCA-Santa Lucia'), ('STP', 'STP-Santo Tome y Principe'), ('SEN', 'SEN-Senegal'), ('SRB', 'SRB-Serbia'), ('SYC', 'SYC-Seychelles'), ('SLE', 'SLE-Sierra leona'), ('SGP', 'SGP-Singapur'), ('SXM', 'SXM-Sint Maarten (parte holandesa)'), ('SYR', 'SYR-Siria, (la) Republica Arabe'), ('SOM', 'SOM-Somalia'), ('LKA', 'LKA-Sri Lanka'), ('SWZ', 'SWZ-Suazilandia'), ('ZAF', 'ZAF-Sudafrica'), ('SDN', 'SDN-Sudan (el)'), ('SSD', 'SSD-Sudan del Sur'), ('SWE', 'SWE-Suecia'), ('CHE', 'CHE-Suiza'), ('SUR', 'SUR-Surinam'), ('SJM', 'SJM-Svalbard y Jan Mayen'), ('THA', 'THA-Tailandia'), ('TWN', 'TWN-Taiwan (Provincia de China)'), ('TZA', 'TZA-Tanzania, Republica Unida de'), ('TJK', 'TJK-Tayikistan'), ('IOT', 'IOT-Territorio Britanico del Oceano Indico (el)'), ('ATF', 'ATF-Territorios Australes Franceses (los)'), ('TLS', 'TLS-Timor-Leste'), ('TGO', 'TGO-Togo'), ('TKL', 'TKL-Tokelau'), ('TON', 'TON-Tonga'), ('TTO', 'TTO-Trinidad y Tobago'), ('TUN', 'TUN-Tunez'), ('TKM', 'TKM-Turkmenistan'), ('TUR', 'TUR-Turquia'), ('TUV', 'TUV-Tuvalu'), ('UKR', 'UKR-Ucrania'), ('UGA', 'UGA-Uganda'), ('URY', 'URY-Uruguay'), ('UZB', 'UZB-Uzbekistan'), ('VUT', 'VUT-Vanuatu'), ('VAT', 'VAT-Santa Sede[Estado de la Ciudad del Vaticano] (la)'), ('VEN', 'VEN-Venezuela, Republica Bolivariana de'), ('VNM', 'VNM-Viet Nam'), ('WLF', 'WLF-Wallis y Futuna'), ('YEM', 'YEM-Yemen'), ('DJI', 'DJI-Yibuti'), ('ZMB', 'ZMB-Zambia'), ('ZWE', 'ZWE-Zimbabue'), ('ZZZ', 'ZZZ-Paises no declarados')], default='MEX', max_length=3),
        ),
        migrations.AlterField(
            model_name='comprobantepagos',
            name='UsoCFDI_Rec',
            field=models.CharField(blank=True, choices=[('G02', 'G02-Devoluciones, descuentos o bonificaciones.'), ('G03', 'G03-Gastos en general.'), ('I01', 'I01-Construcciones.'), ('I02', 'I02-Mobiliario y equipo de oficina por inversiones.'), ('I03', 'I03-Equipo de transporte.'), ('I04', 'I04-Equipo de computo y accesorios.'), ('I05', 'I05-Dados, troqueles, moldes, matrices y herramental.'), ('I06', 'I06-Comunicaciones telefónicas.'), ('I07', 'I07-Comunicaciones satelitales.'), ('I08', 'I08-Otra maquinaria y equipo.'), ('D01', 'D01-Honorarios médicos, dentales y gastos hospitalarios.'), ('D02', 'D02-Gastos médicos por incapacidad o discapacidad.'), ('D03', 'D03-Gastos funerales.'), ('D04', 'D04-Donativos.'), ('D05', 'D05-Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación).'), ('D06', 'D06-Aportaciones voluntarias al SAR.'), ('D07', 'D07-Primas por seguros de gastos médicos.'), ('D08', 'D08-Gastos de transportación escolar obligatoria.'), ('D09', 'D09-Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.'), ('D10', 'D10-Pagos por servicios educativos (colegiaturas).'), ('S01', 'S01-Sin efectos fiscales.  '), ('CP01', 'CP01-Pagos'), ('CN01', 'CN01-Nómina')], default='CP01', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='FormaDePagoP',
            field=models.CharField(choices=[('01', '01-Efectivo'), ('02', '02-Cheque nominativo'), ('03', '03-Transferencia electronica de fondos'), ('04', '04-Tarjeta de credito'), ('05', '05-Monedero electronico'), ('06', '06-Dinero electronico'), ('08', '08-Vales de despensa'), ('12', '12-Dacion en pago'), ('13', '13-Pago por subrogacion'), ('14', '14-Pago por consignacion'), ('15', '15-Condonacion'), ('17', '17-Compensacion'), ('23', '23-Novacion'), ('24', '24-Confusion'), ('25', '25-Remision de deuda'), ('26', '26-Prescripcion o caducidad'), ('27', '27-A satisfaccion del acreedor'), ('28', '28-Tarjeta de debito'), ('29', '29-Tarjeta de servicios'), ('30', '30-Aplicacion de anticipos'), ('31', '31-Intermediario pagos'), ('99', '99-Por definir')], max_length=2),
        ),
    ]
