# Generated by Django 4.0.3 on 2022-05-05 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0011_alter_cliente_recidencia_alter_cliente_regimen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Recidencia',
            field=models.CharField(choices=[('AFG', 'AFG - Afganistán'), ('ALA', 'ALA - Islas Åland'), ('ALB', 'ALB - Albania'), ('DEU', 'DEU - Alemania'), ('AND', 'AND - Andorra'), ('AGO', 'AGO - Angola'), ('AIA', 'AIA - Anguila'), ('ATA', 'ATA - Antártida'), ('ATG', 'ATG - Antigua y Barbuda'), ('SAU', 'SAU - Arabia Saudita'), ('DZA', 'DZA - Argelia'), ('ARG', 'ARG - Argentina'), ('ARM', 'ARM - Armenia'), ('ABW', 'ABW - Aruba'), ('AUS', 'AUS - Australia'), ('AUT', 'AUT - Austria'), ('AZE', 'AZE - Azerbaiyán'), ('BHS', 'BHS - Bahamas (las)'), ('BGD', 'BGD - Bangladés'), ('BRB', 'BRB - Barbados'), ('BHR', 'BHR - Baréin'), ('BEL', 'BEL - Bélgica'), ('BLZ', 'BLZ - Belice'), ('BEN', 'BEN - Benín'), ('BMU', 'BMU - Bermudas'), ('BLR', 'BLR - Bielorrusia'), ('MMR', 'MMR - Myanmar'), ('BOL', 'BOL - Bolivia, Estado Plurinacional de'), ('BIH', 'BIH - Bosnia y Herzegovina'), ('BWA', 'BWA - Botsuana'), ('BRA', 'BRA - Brasil'), ('BRN', 'BRN - Brunéi Darussalam'), ('BGR', 'BGR - Bulgaria'), ('BFA', 'BFA - Burkina Faso'), ('BDI', 'BDI - Burundi'), ('BTN', 'BTN - Bután'), ('CPV', 'CPV - Cabo Verde'), ('KHM', 'KHM - Camboya'), ('CMR', 'CMR - Camerún'), ('CAN', 'CAN - Canadá'), ('QAT', 'QAT - Catar'), ('BES', 'BES - Bonaire, San Eustaquio y Saba'), ('TCD', 'TCD - Chad'), ('CHL', 'CHL - Chile'), ('CHN', 'CHN - China'), ('CYP', 'CYP - Chipre'), ('COL', 'COL - Colombia'), ('COM', 'COM - Comoras'), ('PRK', 'PRK - Corea (la República Democrática Popular de)'), ('KOR', 'KOR - Corea (la República de)'), ('CIV', "CIV - Côte d'Ivoire"), ('CRI', 'CRI - Costa Rica'), ('HRV', 'HRV - Croacia'), ('CUB', 'CUB - Cuba'), ('CUW', 'CUW - Curaçao'), ('DNK', 'DNK - Dinamarca'), ('DMA', 'DMA - Dominica'), ('ECU', 'ECU - Ecuador'), ('EGY', 'EGY - Egipto'), ('SLV', 'SLV - El Salvador'), ('ARE', 'ARE - Emiratos Árabes Unidos (Los)'), ('ERI', 'ERI - Eritrea'), ('SVK', 'SVK - Eslovaquia'), ('SVN', 'SVN - Eslovenia'), ('ESP', 'ESP - España'), ('USA', 'USA - Estados Unidos (los)'), ('EST', 'EST - Estonia'), ('ETH', 'ETH - Etiopía'), ('PHL', 'PHL - Filipinas (las)'), ('FIN', 'FIN - Finlandia'), ('FJI', 'FJI - Fiyi'), ('FRA', 'FRA - Francia'), ('GAB', 'GAB - Gabón'), ('GMB', 'GMB - Gambia (La)'), ('GEO', 'GEO - Georgia'), ('GHA', 'GHA - Ghana'), ('GIB', 'GIB - Gibraltar'), ('GRD', 'GRD - Granada'), ('GRC', 'GRC - Grecia'), ('GRL', 'GRL - Groenlandia'), ('GLP', 'GLP - Guadalupe'), ('GUM', 'GUM - Guam'), ('GTM', 'GTM - Guatemala'), ('GUF', 'GUF - Guayana Francesa'), ('GGY', 'GGY - Guernsey'), ('GIN', 'GIN - Guinea'), ('GNB', 'GNB - Guinea-Bisáu'), ('GNQ', 'GNQ - Guinea Ecuatorial'), ('GUY', 'GUY - Guyana'), ('HTI', 'HTI - Haití'), ('HND', 'HND - Honduras'), ('HKG', 'HKG - Hong Kong'), ('HUN', 'HUN - Hungría'), ('IND', 'IND - India'), ('IDN', 'IDN - Indonesia'), ('IRQ', 'IRQ - Irak'), ('IRN', 'IRN - Irán (la República Islámica de)'), ('IRL', 'IRL - Irlanda'), ('BVT', 'BVT - Isla Bouvet'), ('IMN', 'IMN - Isla de Man'), ('CXR', 'CXR - Isla de Navidad'), ('NFK', 'NFK - Isla Norfolk'), ('ISL', 'ISL - Islandia'), ('CYM', 'CYM - Islas Caimán (las)'), ('CCK', 'CCK - Islas Cocos (Keeling)'), ('COK', 'COK - Islas Cook (las)'), ('FRO', 'FRO - Islas Feroe (las)'), ('SGS', 'SGS - Georgia del sur y las islas sandwich del sur'), ('HMD', 'HMD - Isla Heard e Islas McDonald'), ('FLK', 'FLK - Islas Malvinas [Falkland] (las)'), ('MNP', 'MNP - Islas Marianas del Norte (las)'), ('MHL', 'MHL - Islas Marshall (las)'), ('PCN', 'PCN - Pitcairn'), ('SLB', 'SLB - Islas Salomón (las)'), ('TCA', 'TCA - Islas Turcas y Caicos (las)'), ('UMI', 'UMI - Islas de Ultramar Menores de Estados Unidos (las)'), ('VGB', 'VGB - Islas Vírgenes (Británicas)'), ('VIR', 'VIR - Islas Vírgenes (EE.UU.)'), ('ISR', 'ISR - Israel'), ('ITA', 'ITA - Italia'), ('JAM', 'JAM - Jamaica'), ('JPN', 'JPN - Japón'), ('JEY', 'JEY - Jersey'), ('JOR', 'JOR - Jordania'), ('KAZ', 'KAZ - Kazajistán'), ('KEN', 'KEN - Kenia'), ('KGZ', 'KGZ - Kirguistán'), ('KIR', 'KIR - Kiribati'), ('KWT', 'KWT - Kuwait'), ('LAO', 'LAO - Lao, (la) República Democrática Popular'), ('LSO', 'LSO - Lesoto'), ('LVA', 'LVA - Letonia'), ('LBN', 'LBN - Líbano'), ('LBR', 'LBR - Liberia'), ('LBY', 'LBY - Libia'), ('LIE', 'LIE - Liechtenstein'), ('LTU', 'LTU - Lituania'), ('LUX', 'LUX - Luxemburgo'), ('MAC', 'MAC - Macao'), ('MDG', 'MDG - Madagascar'), ('MYS', 'MYS - Malasia'), ('MWI', 'MWI - Malaui'), ('MDV', 'MDV - Maldivas'), ('MLI', 'MLI - Malí'), ('MLT', 'MLT - Malta'), ('MAR', 'MAR - Marruecos'), ('MTQ', 'MTQ - Martinica'), ('MUS', 'MUS - Mauricio'), ('MRT', 'MRT - Mauritania'), ('MYT', 'MYT - Mayotte'), ('MEX', 'MEX - México'), ('FSM', 'FSM - Micronesia (los Estados Federados de)'), ('MDA', 'MDA - Moldavia (la República de)'), ('MCO', 'MCO - Mónaco'), ('MNG', 'MNG - Mongolia'), ('MNE', 'MNE - Montenegro'), ('MSR', 'MSR - Montserrat'), ('MOZ', 'MOZ - Mozambique'), ('NAM', 'NAM - Namibia'), ('NRU', 'NRU - Nauru'), ('NPL', 'NPL - Nepal'), ('NIC', 'NIC - Nicaragua'), ('NER', 'NER - Níger (el)'), ('NGA', 'NGA - Nigeria'), ('NIU', 'NIU - Niue'), ('NOR', 'NOR - Noruega'), ('NCL', 'NCL - Nueva Caledonia'), ('NZL', 'NZL - Nueva Zelanda'), ('OMN', 'OMN - Omán'), ('NLD', 'NLD - Países Bajos (los)'), ('PAK', 'PAK - Pakistán'), ('PLW', 'PLW - Palaos'), ('PSE', 'PSE - Palestina, Estado de'), ('PAN', 'PAN - Panamá'), ('PNG', 'PNG - Papúa Nueva Guinea'), ('PRY', 'PRY - Paraguay'), ('PER', 'PER - Perú'), ('PYF', 'PYF - Polinesia Francesa'), ('POL', 'POL - Polonia'), ('PRT', 'PRT - Portugal'), ('PRI', 'PRI - Puerto Rico'), ('GBR', 'GBR - Reino Unido (el)'), ('CAF', 'CAF - República Centroafricana (la)'), ('CZE', 'CZE - República Checa (la)'), ('MKD', 'MKD - Macedonia (la antigua República Yugoslava de)'), ('COG', 'COG - Congo'), ('COD', 'COD - Congo (la República Democrática del)'), ('DOM', 'DOM - República Dominicana (la)'), ('REU', 'REU - Reunión'), ('RWA', 'RWA - Ruanda'), ('ROU', 'ROU - Rumania'), ('RUS', 'RUS - Rusia, (la) Federación de'), ('ESH', 'ESH - Sahara Occidental'), ('WSM', 'WSM - Samoa'), ('ASM', 'ASM - Samoa Americana'), ('BLM', 'BLM - San Bartolomé'), ('KNA', 'KNA - San Cristóbal y Nieves'), ('SMR', 'SMR - San Marino'), ('MAF', 'MAF - San Martín (parte francesa)'), ('SPM', 'SPM - San Pedro y Miquelón'), ('VCT', 'VCT - San Vicente y las Granadinas'), ('SHN', 'SHN - Santa Helena, Ascensión y Tristán de Acuña'), ('LCA', 'LCA - Santa Lucía'), ('STP', 'STP - Santo Tomé y Príncipe'), ('SEN', 'SEN - Senegal'), ('SRB', 'SRB - Serbia'), ('SYC', 'SYC - Seychelles'), ('SLE', 'SLE - Sierra leona'), ('SGP', 'SGP - Singapur'), ('SXM', 'SXM - Sint Maarten (parte holandesa)'), ('SYR', 'SYR - Siria, (la) República Árabe'), ('SOM', 'SOM - Somalia'), ('LKA', 'LKA - Sri Lanka'), ('SWZ', 'SWZ - Suazilandia'), ('ZAF', 'ZAF - Sudáfrica'), ('SDN', 'SDN - Sudán (el)'), ('SSD', 'SSD - Sudán del Sur'), ('SWE', 'SWE - Suecia'), ('CHE', 'CHE - Suiza'), ('SUR', 'SUR - Surinam'), ('SJM', 'SJM - Svalbard y Jan Mayen'), ('THA', 'THA - Tailandia'), ('TWN', 'TWN - Taiwán (Provincia de China)'), ('TZA', 'TZA - Tanzania, República Unida de'), ('TJK', 'TJK - Tayikistán'), ('IOT', 'IOT - Territorio Británico del Océano Índico (el)'), ('ATF', 'ATF - Territorios Australes Franceses (los)'), ('TLS', 'TLS - Timor-Leste'), ('TGO', 'TGO - Togo'), ('TKL', 'TKL - Tokelau'), ('TON', 'TON - Tonga'), ('TTO', 'TTO - Trinidad y Tobago'), ('TUN', 'TUN - Túnez'), ('TKM', 'TKM - Turkmenistán'), ('TUR', 'TUR - Turquía'), ('TUV', 'TUV - Tuvalu'), ('UKR', 'UKR - Ucrania'), ('UGA', 'UGA - Uganda'), ('URY', 'URY - Uruguay'), ('UZB', 'UZB - Uzbekistán'), ('VUT', 'VUT - Vanuatu'), ('VAT', 'VAT - Santa Sede[Estado de la Ciudad del Vaticano] (la)'), ('VEN', 'VEN - Venezuela, República Bolivariana de'), ('VNM', 'VNM - Viet Nam'), ('WLF', 'WLF - Wallis y Futuna'), ('YEM', 'YEM - Yemen'), ('DJI', 'DJI - Yibuti'), ('ZMB', 'ZMB - Zambia'), ('ZWE', 'ZWE - Zimbabue'), ('ZZZ', 'ZZZ - Países no declarados')], default='MEX', max_length=3),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Regimen',
            field=models.CharField(choices=[('601', '601 - General de Ley Personas Morales'), ('603', '603 - Personas Morales con Fines no Lucrativos'), ('605', '605 - Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606 - Arrendamiento'), ('607', '607 - Régimen de Enajenación o Adquisición de Bienes'), ('608', '608 - Demás ingresos'), ('610', '610 - Residentes en el Extranjero sin Establecimiento Permanente en México'), ('611', '611 - Ingresos por Dividendos (socios y accionistas)'), ('612', '612 - Personas Físicas con Actividades Empresariales y Profesionales'), ('614', '614 - Ingresos por intereses'), ('615', '615 - Régimen de los ingresos por obtención de premios'), ('616', '616 - Sin obligaciones fiscales'), ('620', '620 - Sociedades Cooperativas de Producción que optan por diferir sus ingresos'), ('621', '621 - Incorporación Fiscal'), ('622', '622 - Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'), ('623', '623 - Opcional para Grupos de Sociedades'), ('624', '624 - Coordinados'), ('625', '625 - Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas'), ('626', '626 - Régimen Simplificado de Confianza')], max_length=3),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='Recidencia',
            field=models.CharField(choices=[('AFG', 'AFG - Afganistán'), ('ALA', 'ALA - Islas Åland'), ('ALB', 'ALB - Albania'), ('DEU', 'DEU - Alemania'), ('AND', 'AND - Andorra'), ('AGO', 'AGO - Angola'), ('AIA', 'AIA - Anguila'), ('ATA', 'ATA - Antártida'), ('ATG', 'ATG - Antigua y Barbuda'), ('SAU', 'SAU - Arabia Saudita'), ('DZA', 'DZA - Argelia'), ('ARG', 'ARG - Argentina'), ('ARM', 'ARM - Armenia'), ('ABW', 'ABW - Aruba'), ('AUS', 'AUS - Australia'), ('AUT', 'AUT - Austria'), ('AZE', 'AZE - Azerbaiyán'), ('BHS', 'BHS - Bahamas (las)'), ('BGD', 'BGD - Bangladés'), ('BRB', 'BRB - Barbados'), ('BHR', 'BHR - Baréin'), ('BEL', 'BEL - Bélgica'), ('BLZ', 'BLZ - Belice'), ('BEN', 'BEN - Benín'), ('BMU', 'BMU - Bermudas'), ('BLR', 'BLR - Bielorrusia'), ('MMR', 'MMR - Myanmar'), ('BOL', 'BOL - Bolivia, Estado Plurinacional de'), ('BIH', 'BIH - Bosnia y Herzegovina'), ('BWA', 'BWA - Botsuana'), ('BRA', 'BRA - Brasil'), ('BRN', 'BRN - Brunéi Darussalam'), ('BGR', 'BGR - Bulgaria'), ('BFA', 'BFA - Burkina Faso'), ('BDI', 'BDI - Burundi'), ('BTN', 'BTN - Bután'), ('CPV', 'CPV - Cabo Verde'), ('KHM', 'KHM - Camboya'), ('CMR', 'CMR - Camerún'), ('CAN', 'CAN - Canadá'), ('QAT', 'QAT - Catar'), ('BES', 'BES - Bonaire, San Eustaquio y Saba'), ('TCD', 'TCD - Chad'), ('CHL', 'CHL - Chile'), ('CHN', 'CHN - China'), ('CYP', 'CYP - Chipre'), ('COL', 'COL - Colombia'), ('COM', 'COM - Comoras'), ('PRK', 'PRK - Corea (la República Democrática Popular de)'), ('KOR', 'KOR - Corea (la República de)'), ('CIV', "CIV - Côte d'Ivoire"), ('CRI', 'CRI - Costa Rica'), ('HRV', 'HRV - Croacia'), ('CUB', 'CUB - Cuba'), ('CUW', 'CUW - Curaçao'), ('DNK', 'DNK - Dinamarca'), ('DMA', 'DMA - Dominica'), ('ECU', 'ECU - Ecuador'), ('EGY', 'EGY - Egipto'), ('SLV', 'SLV - El Salvador'), ('ARE', 'ARE - Emiratos Árabes Unidos (Los)'), ('ERI', 'ERI - Eritrea'), ('SVK', 'SVK - Eslovaquia'), ('SVN', 'SVN - Eslovenia'), ('ESP', 'ESP - España'), ('USA', 'USA - Estados Unidos (los)'), ('EST', 'EST - Estonia'), ('ETH', 'ETH - Etiopía'), ('PHL', 'PHL - Filipinas (las)'), ('FIN', 'FIN - Finlandia'), ('FJI', 'FJI - Fiyi'), ('FRA', 'FRA - Francia'), ('GAB', 'GAB - Gabón'), ('GMB', 'GMB - Gambia (La)'), ('GEO', 'GEO - Georgia'), ('GHA', 'GHA - Ghana'), ('GIB', 'GIB - Gibraltar'), ('GRD', 'GRD - Granada'), ('GRC', 'GRC - Grecia'), ('GRL', 'GRL - Groenlandia'), ('GLP', 'GLP - Guadalupe'), ('GUM', 'GUM - Guam'), ('GTM', 'GTM - Guatemala'), ('GUF', 'GUF - Guayana Francesa'), ('GGY', 'GGY - Guernsey'), ('GIN', 'GIN - Guinea'), ('GNB', 'GNB - Guinea-Bisáu'), ('GNQ', 'GNQ - Guinea Ecuatorial'), ('GUY', 'GUY - Guyana'), ('HTI', 'HTI - Haití'), ('HND', 'HND - Honduras'), ('HKG', 'HKG - Hong Kong'), ('HUN', 'HUN - Hungría'), ('IND', 'IND - India'), ('IDN', 'IDN - Indonesia'), ('IRQ', 'IRQ - Irak'), ('IRN', 'IRN - Irán (la República Islámica de)'), ('IRL', 'IRL - Irlanda'), ('BVT', 'BVT - Isla Bouvet'), ('IMN', 'IMN - Isla de Man'), ('CXR', 'CXR - Isla de Navidad'), ('NFK', 'NFK - Isla Norfolk'), ('ISL', 'ISL - Islandia'), ('CYM', 'CYM - Islas Caimán (las)'), ('CCK', 'CCK - Islas Cocos (Keeling)'), ('COK', 'COK - Islas Cook (las)'), ('FRO', 'FRO - Islas Feroe (las)'), ('SGS', 'SGS - Georgia del sur y las islas sandwich del sur'), ('HMD', 'HMD - Isla Heard e Islas McDonald'), ('FLK', 'FLK - Islas Malvinas [Falkland] (las)'), ('MNP', 'MNP - Islas Marianas del Norte (las)'), ('MHL', 'MHL - Islas Marshall (las)'), ('PCN', 'PCN - Pitcairn'), ('SLB', 'SLB - Islas Salomón (las)'), ('TCA', 'TCA - Islas Turcas y Caicos (las)'), ('UMI', 'UMI - Islas de Ultramar Menores de Estados Unidos (las)'), ('VGB', 'VGB - Islas Vírgenes (Británicas)'), ('VIR', 'VIR - Islas Vírgenes (EE.UU.)'), ('ISR', 'ISR - Israel'), ('ITA', 'ITA - Italia'), ('JAM', 'JAM - Jamaica'), ('JPN', 'JPN - Japón'), ('JEY', 'JEY - Jersey'), ('JOR', 'JOR - Jordania'), ('KAZ', 'KAZ - Kazajistán'), ('KEN', 'KEN - Kenia'), ('KGZ', 'KGZ - Kirguistán'), ('KIR', 'KIR - Kiribati'), ('KWT', 'KWT - Kuwait'), ('LAO', 'LAO - Lao, (la) República Democrática Popular'), ('LSO', 'LSO - Lesoto'), ('LVA', 'LVA - Letonia'), ('LBN', 'LBN - Líbano'), ('LBR', 'LBR - Liberia'), ('LBY', 'LBY - Libia'), ('LIE', 'LIE - Liechtenstein'), ('LTU', 'LTU - Lituania'), ('LUX', 'LUX - Luxemburgo'), ('MAC', 'MAC - Macao'), ('MDG', 'MDG - Madagascar'), ('MYS', 'MYS - Malasia'), ('MWI', 'MWI - Malaui'), ('MDV', 'MDV - Maldivas'), ('MLI', 'MLI - Malí'), ('MLT', 'MLT - Malta'), ('MAR', 'MAR - Marruecos'), ('MTQ', 'MTQ - Martinica'), ('MUS', 'MUS - Mauricio'), ('MRT', 'MRT - Mauritania'), ('MYT', 'MYT - Mayotte'), ('MEX', 'MEX - México'), ('FSM', 'FSM - Micronesia (los Estados Federados de)'), ('MDA', 'MDA - Moldavia (la República de)'), ('MCO', 'MCO - Mónaco'), ('MNG', 'MNG - Mongolia'), ('MNE', 'MNE - Montenegro'), ('MSR', 'MSR - Montserrat'), ('MOZ', 'MOZ - Mozambique'), ('NAM', 'NAM - Namibia'), ('NRU', 'NRU - Nauru'), ('NPL', 'NPL - Nepal'), ('NIC', 'NIC - Nicaragua'), ('NER', 'NER - Níger (el)'), ('NGA', 'NGA - Nigeria'), ('NIU', 'NIU - Niue'), ('NOR', 'NOR - Noruega'), ('NCL', 'NCL - Nueva Caledonia'), ('NZL', 'NZL - Nueva Zelanda'), ('OMN', 'OMN - Omán'), ('NLD', 'NLD - Países Bajos (los)'), ('PAK', 'PAK - Pakistán'), ('PLW', 'PLW - Palaos'), ('PSE', 'PSE - Palestina, Estado de'), ('PAN', 'PAN - Panamá'), ('PNG', 'PNG - Papúa Nueva Guinea'), ('PRY', 'PRY - Paraguay'), ('PER', 'PER - Perú'), ('PYF', 'PYF - Polinesia Francesa'), ('POL', 'POL - Polonia'), ('PRT', 'PRT - Portugal'), ('PRI', 'PRI - Puerto Rico'), ('GBR', 'GBR - Reino Unido (el)'), ('CAF', 'CAF - República Centroafricana (la)'), ('CZE', 'CZE - República Checa (la)'), ('MKD', 'MKD - Macedonia (la antigua República Yugoslava de)'), ('COG', 'COG - Congo'), ('COD', 'COD - Congo (la República Democrática del)'), ('DOM', 'DOM - República Dominicana (la)'), ('REU', 'REU - Reunión'), ('RWA', 'RWA - Ruanda'), ('ROU', 'ROU - Rumania'), ('RUS', 'RUS - Rusia, (la) Federación de'), ('ESH', 'ESH - Sahara Occidental'), ('WSM', 'WSM - Samoa'), ('ASM', 'ASM - Samoa Americana'), ('BLM', 'BLM - San Bartolomé'), ('KNA', 'KNA - San Cristóbal y Nieves'), ('SMR', 'SMR - San Marino'), ('MAF', 'MAF - San Martín (parte francesa)'), ('SPM', 'SPM - San Pedro y Miquelón'), ('VCT', 'VCT - San Vicente y las Granadinas'), ('SHN', 'SHN - Santa Helena, Ascensión y Tristán de Acuña'), ('LCA', 'LCA - Santa Lucía'), ('STP', 'STP - Santo Tomé y Príncipe'), ('SEN', 'SEN - Senegal'), ('SRB', 'SRB - Serbia'), ('SYC', 'SYC - Seychelles'), ('SLE', 'SLE - Sierra leona'), ('SGP', 'SGP - Singapur'), ('SXM', 'SXM - Sint Maarten (parte holandesa)'), ('SYR', 'SYR - Siria, (la) República Árabe'), ('SOM', 'SOM - Somalia'), ('LKA', 'LKA - Sri Lanka'), ('SWZ', 'SWZ - Suazilandia'), ('ZAF', 'ZAF - Sudáfrica'), ('SDN', 'SDN - Sudán (el)'), ('SSD', 'SSD - Sudán del Sur'), ('SWE', 'SWE - Suecia'), ('CHE', 'CHE - Suiza'), ('SUR', 'SUR - Surinam'), ('SJM', 'SJM - Svalbard y Jan Mayen'), ('THA', 'THA - Tailandia'), ('TWN', 'TWN - Taiwán (Provincia de China)'), ('TZA', 'TZA - Tanzania, República Unida de'), ('TJK', 'TJK - Tayikistán'), ('IOT', 'IOT - Territorio Británico del Océano Índico (el)'), ('ATF', 'ATF - Territorios Australes Franceses (los)'), ('TLS', 'TLS - Timor-Leste'), ('TGO', 'TGO - Togo'), ('TKL', 'TKL - Tokelau'), ('TON', 'TON - Tonga'), ('TTO', 'TTO - Trinidad y Tobago'), ('TUN', 'TUN - Túnez'), ('TKM', 'TKM - Turkmenistán'), ('TUR', 'TUR - Turquía'), ('TUV', 'TUV - Tuvalu'), ('UKR', 'UKR - Ucrania'), ('UGA', 'UGA - Uganda'), ('URY', 'URY - Uruguay'), ('UZB', 'UZB - Uzbekistán'), ('VUT', 'VUT - Vanuatu'), ('VAT', 'VAT - Santa Sede[Estado de la Ciudad del Vaticano] (la)'), ('VEN', 'VEN - Venezuela, República Bolivariana de'), ('VNM', 'VNM - Viet Nam'), ('WLF', 'WLF - Wallis y Futuna'), ('YEM', 'YEM - Yemen'), ('DJI', 'DJI - Yibuti'), ('ZMB', 'ZMB - Zambia'), ('ZWE', 'ZWE - Zimbabue'), ('ZZZ', 'ZZZ - Países no declarados')], default='MEX', max_length=3),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='Regimen',
            field=models.CharField(choices=[('601', '601 - General de Ley Personas Morales'), ('603', '603 - Personas Morales con Fines no Lucrativos'), ('605', '605 - Sueldos y Salarios e Ingresos Asimilados a Salarios'), ('606', '606 - Arrendamiento'), ('607', '607 - Régimen de Enajenación o Adquisición de Bienes'), ('608', '608 - Demás ingresos'), ('610', '610 - Residentes en el Extranjero sin Establecimiento Permanente en México'), ('611', '611 - Ingresos por Dividendos (socios y accionistas)'), ('612', '612 - Personas Físicas con Actividades Empresariales y Profesionales'), ('614', '614 - Ingresos por intereses'), ('615', '615 - Régimen de los ingresos por obtención de premios'), ('616', '616 - Sin obligaciones fiscales'), ('620', '620 - Sociedades Cooperativas de Producción que optan por diferir sus ingresos'), ('621', '621 - Incorporación Fiscal'), ('622', '622 - Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'), ('623', '623 - Opcional para Grupos de Sociedades'), ('624', '624 - Coordinados'), ('625', '625 - Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas'), ('626', '626 - Régimen Simplificado de Confianza')], max_length=3),
        ),
    ]
