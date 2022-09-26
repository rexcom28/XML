
from xml.etree.ElementTree import(
    Element, QName, SubElement, Comment, tostring
)
from xml.dom import minidom
import xml.etree.ElementTree as ET
import decimal

def prettify(elem):
    
    rough_string = ET.tostring(elem, 'utf-8')
    
    reparsed = minidom.parseString(rough_string)
    
    return reparsed.toprettyxml(indent="  ",encoding="utf-8").decode("utf-8")

def Create_XML(data, TipoC):
    ns_map = {
        'cfdi': "http://www.sat.gob.mx/cfd/4",
        'xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'Pagos20':"http://www.sat.gob.mx/Pagos20"
    }

    SCHEMAS = "http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd"
    
    if TipoC=='pago':
        SCHEMAS += " http://www.sat.gob.mx/Pagos20 http://www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd"

    for prefix, uri in ns_map.items():
        ET.register_namespace(prefix,uri)
    
    
    Comprobante = ET.Element(ET.QName(ns_map['cfdi'],"Comprobante")) 
    Comprobante.set(QName(ns_map['xsi'],"schemaLocation"),SCHEMAS)
    Comprobante.set('Version',data['Version'])
    Comprobante.set('Serie',data['Serie'])
    Comprobante.set('Folio',data['Folio'])
    Comprobante.set('Fecha',data['Fecha'][:-1])
    Comprobante.set('Sello',data['Sello'])
    if TipoC not in ['pago']:
        Comprobante.set('FormaPago',"NA" if data['FormaPago'] ==None else (data['FormaPago']) )
        if data['Descuento']!=None:
            Comprobante.set('Descuento', data['Descuento'] )
        Comprobante.set('TipoCambio',data['TipoCambio'])
        Comprobante.set('MetodoPago',data['MetodoPago'])
        if data['CondicionesDePago'] !=None:
            Comprobante.set('CondicionesDePago',data['CondicionesDePago'])
            
    Comprobante.set('SubTotal', "NA" if data['SubTotal'] ==None else (data['SubTotal'] if TipoC not in ['pago'] else "0") )
    Comprobante.set('Moneda',   "NA" if data['Moneda'] ==None else (data['Moneda']  if TipoC not in ['pago'] else "XXX") )
    Comprobante.set('Total',    "NA" if data['Total'] ==None else (data['Total']   if TipoC not in ['pago'] else "0") )
    Comprobante.set('TipoDeComprobante','NA' if data['TipoDeComprobante'] ==None else (data['TipoDeComprobante']) )
    Comprobante.set('Exportacion',"NA" if data['Exportacion']==None else (data['Exportacion']) )
    Comprobante.set('LugarExpedicion',"NA" if data['LugarExpedicion']==None else ( data['LugarExpedicion']) )
    if data['Confirmacion'] != None:
        Comprobante.set('Confirmacion',data['Confirmacion'])
    Comprobante.set('NoCertificado',data['NoCertificado'])
    Comprobante.set('Certificado',data['Certificado'])
    #-----------Comprobante Attributes end------------------------------------->

    #CFDI Relacionados Comprobante Init---------------------------------------->
    if TipoC == 'ingreso':
        hay_DR = True if len(data['CFDI_REL_Comprobante']) > 0 else False
        if 'CFDI_REL_Comprobante' in data.keys() and hay_DR :
            CfdiRelacionados = SubElement(Comprobante,ET.QName(ns_map['cfdi'], 'CfdiRelacionados'))
            CfdiRelacionados.set("TipoRelacion", data['CFDI_REL_Comprobante'][0]['TipoRelacion'])        
            CfdiRelacionado =SubElement(CfdiRelacionados,ET.QName(ns_map['cfdi'], 'CfdiRelacionado'))
            CfdiRelacionado.set("UUID",data['CFDI_REL_Comprobante'][0]['UUID'])
    if TipoC == 'pago':
        hay_DR = True if len(data['CFDI_REL_REP']) > 0 else False
        if 'CFDI_REL_REP' in data.keys() and hay_DR :
            CfdiRelacionados = SubElement(Comprobante,ET.QName(ns_map['cfdi'], 'CfdiRelacionados'))
            CfdiRelacionados.set("TipoRelacion", data['CFDI_REL_REP'][0]['TipoRelacion'])        
            CfdiRelacionado =SubElement(CfdiRelacionados,ET.QName(ns_map['cfdi'], 'CfdiRelacionado'))
            CfdiRelacionado.set("UUID",data['CFDI_REL_REP'][0]['UUID'])    
    #CFDI Relacionados Comprobante End---------------------------------------->

    
    Emisor_Nodo(data, Comprobante, ns_map)
    Receptor_Nodo(data,Comprobante, ns_map)  


    #Conceptos Init-------------------------------------------------------->
    if TipoC == 'ingreso' :
        Conceptos_Ingreso_Nodo(data, Comprobante, ns_map)    
    if 'IVA' in data.keys() or 'IVA_Ret' in data.keys() or 'ISR' in data.keys():
        Impuestos = SubElement(Comprobante,ET.QName(ns_map['cfdi'],'Impuestos'))
        if data['IVA_Ret'] != None or data['ISR'] != None :
            suma = str(decimal.Decimal(data['IVA_Ret'])  + decimal.Decimal(data['ISR']) )                         
            Impuestos.set('TotalImpuestosRetenidos',suma)
            Retenciones = SubElement(Impuestos,ET.QName(ns_map['cfdi'],'Retenciones'))            
            if data['IVA_Ret'] != None :
                Retencion = SubElement(Retenciones, ET.QName(ns_map['cfdi'],'Retencion'))
                Retencion.set('Impuesto','002')
                Retencion.set('Importe',data['IVA_Ret'])

            if data['ISR'] != None:
                Retencion = SubElement(Retenciones, ET.QName(ns_map['cfdi'],'Retencion'))
                Retencion.set('Impuesto','001')
                Retencion.set('Importe',data['ISR'])
        if data['IVA']  != None:            
            Impuestos.set('TotalImpuestosTrasladados',data['IVA'])
            Traslados = SubElement(Impuestos,QName(ns_map['cfdi'],'Traslados'))
            Traslado = SubElement(Traslados,QName(ns_map['cfdi'], 'Traslado'))
            
            Traslado.set('Impuesto','002')
            Traslado.set('TipoFactor','Tasa')
            
        if len(data['partidasIngreso']) > 0:
            #print(data['partidasIngreso'][0]['Imp_Partida'][0]['Tipo_T_R'])
            if data['partidasIngreso'][0]['Imp_Partida'][0]['Tipo_T_R']=='TRASLADO':
                Traslado.set('TasaOCuota',data['partidasIngreso'][0]['Imp_Partida'][0]['TasaOCuota'])
            Traslado.set('Importe',data['IVA'])

    if TipoC == 'pago':
        Complemento = SubElement(Comprobante,ET.QName(ns_map['cfdi'],'Complemento'))
        Pagos_Nodo(data, Complemento, ns_map)


    Comprobante = prettify(Comprobante)
    print('----------------')
    print(Comprobante)  



def Emisor_Nodo (data, padre, ns):
    Emisor = SubElement(padre,ET.QName(ns['cfdi'], 'Emisor'))
    Emisor.set('Rfc',data['Rfc_Emi'])
    Emisor.set('Nombre',data['Nombre_Emi'])
    Emisor.set('RegimenFiscal',data['RegimenFiscal_Emi'])
    return Emisor

def Receptor_Nodo(data,padre, nameSpace):
    Receptor = SubElement(padre, ET.QName(nameSpace['cfdi'], 'Receptor'))
    Receptor.set('Rfc',data['Rfc_Rec'])
    Receptor.set('Nombre',data['Nombre_Rec'])    
    Receptor.set('DomicilioFiscalReceptor',data['DomicilioFiscal_Rec'])
    if data['ResidenciaFiscal_Rec'] != 'MEX':
        Receptor.set('ResidenciaFiscal',data['ResidenciaFiscal_Rec'])
        Receptor.set('NumRegIdTrib',data['NumRegIdTrib_Rec'])
    Receptor.set('RegimenFiscalReceptor',data['RegimenFiscal_Rec'])
    Receptor.set('UsoCFDI',data['UsoCFDI_Rec'])
    return Receptor

def Pagos_Nodo(data, padre, nameSapce):
    if 'Pagos_Rep' in data.keys():
        Pago20 = SubElement(padre,ET.QName(nameSapce['Pagos20'],"Pagos"))
        for Pag in data['Pagos_Rep']:
            PagoNodo = SubElement(Pago20,ET.QName(nameSapce['Pagos20'], 'Pago'))
            PagoNodo.set('FechaPago','')
            PagoNodo.set('FormaDePagoP','')
            PagoNodo.set('MonedaP','')
            PagoNodo.set('TipoCambioP','')
            PagoNodo.set('Monto','')
            if 'Pagos_DR' in Pag.keys():                
                for DRs in Pag['Pagos_DR']:
                    DoctoRelacionado = SubElement(PagoNodo,ET.QName(nameSapce['Pagos20'],'DoctoRelacionado'))
                    DoctoRelacionado.set('IdDocumento',DRs['IdDocumento'])
                    DoctoRelacionado.set('Serie',DRs['Serie'])
                    DoctoRelacionado.set('Folio',DRs['Folio'])
                    DoctoRelacionado.set('MonedaDR',DRs['MonedaDR'])
                    DoctoRelacionado.set('EquivalenciaDR',DRs['EquivalenciaDR'])
                    DoctoRelacionado.set('NumParcialidad',str(DRs['NumParcialidad']))
                    DoctoRelacionado.set('ImpSaldoAnt',DRs['ImpSaldoAnt'])
                    DoctoRelacionado.set('ImpPagado',DRs['ImpPagado'])
                    DoctoRelacionado.set('ImpSaldoInsoluto',DRs['ImpSaldoInsoluto'])
                    DoctoRelacionado.set('ObjetoImpDR',DRs['ObjetoImp'])
                    if 'DR_Pagos_Impuestos' in DRs.keys():
                        ImpuestosDR = SubElement(DoctoRelacionado,ET.QName(nameSapce['Pagos20'],'ImpuestosDR'))
                        TrasDR = 0
                        RetDR  = 0
                        
                        for dr in DRs['DR_Pagos_Impuestos']:
                            if dr['Tipo_T_R']=='RETENCION':
                                if RetDR ==0:
                                    RetencionesDR = SubElement(ImpuestosDR,ET.QName(nameSapce['Pagos20'], 'RetencionesDR'))
                                    RetDR +=1                                
                                RetencionDR = SubElement(RetencionesDR,ET.QName(nameSapce['Pagos20'], 'RetencionDR'))
                                RetencionDR.set('BaseDR','')
                                RetencionDR.set('ImpuestoDR','')
                                RetencionDR.set('TipoFactorDR','')
                                RetencionDR.set('TasaOCuotaDR','')
                                RetencionDR.set('ImporteDR','')
                            if dr['Tipo_T_R']=='TRASLADO':
                                if TrasDR==0:
                                    TrasladosDR = SubElement(ImpuestosDR,ET.QName(nameSapce['Pagos20'], 'TrasladosDR'))
                                    TrasDR+=1
                                TrasladoDR = SubElement(TrasladosDR,ET.QName(nameSapce['Pagos20'], 'TrasladoDR'))
                                TrasladoDR.set('BaseDR','')
                                TrasladoDR.set('ImpuestoDR','')
                                TrasladoDR.set('TipoFactorDR','')
                                TrasladoDR.set('TasaOCuotaDR','')
                                TrasladoDR.set('ImporteDR','')

                ImpuestoP = SubElement(PagoNodo,ET.QName(nameSapce['Pagos20'], 'ImpuestosP'))
                RetencionesP = SubElement(ImpuestoP,ET.QName(nameSapce['Pagos20'], 'RetencionesP'))
                TrasladosP = SubElement(ImpuestoP,ET.QName(nameSapce['Pagos20'], 'TrasladosP'))

    return Pago20

def Conceptos_Ingreso_Nodo(data, padre, nameSpace):
    if 'partidasIngreso' in data.keys():
        Conceptos = SubElement(padre,ET.QName(nameSpace['cfdi'],'Conceptos'))   
        for Con in data['partidasIngreso']:        
            Concepto = SubElement(Conceptos,ET.QName(nameSpace['cfdi'],'Concepto'))
            Concepto.set('ClaveProdServ',Con['ClaveProdServ'])        
            if 'NoIdentificacion' in Con.keys():
                Concepto.set('NoIdentificacion',Con['NoIdentificacion'])            
            Concepto.set('Cantidad',Con['Cantidad'])
            Concepto.set('ClaveUnidad',Con['ClaveUnidad'])
            Concepto.set('Unidad',Con['Unidad'])
            Concepto.set('Descripcion',Con['Descripcion'])
            Concepto.set('ValorUnitario',Con['ValorUnitario'])
            Concepto.set('Importe',Con['Importe'])
            Concepto.set('Descuento',Con['Descuento'])
            Concepto.set('ObjetoImp',Con['ObjetoImp'])

            #Si la partida tiene Impuestos
            if 'Imp_Partida' in Con.keys():
                Impuesto_Concepto = SubElement(Concepto,ET.QName(nameSpace['cfdi'],'Impuestos'))
                Tras = 0  
                Ret  = 0                
                for Imp_Partida in Con['Imp_Partida']:                    
                    if Imp_Partida['Tipo_T_R'] == 'TRASLADO':
                        if Tras == 0:
                            Traslados_ImpConcepto = SubElement(Impuesto_Concepto,ET.QName(nameSpace['cfdi'],'Traslados'))
                            Tras+=1
                        Traslado_ImpConcepto = SubElement(Traslados_ImpConcepto,ET.QName(nameSpace['cfdi'],'Traslado'))
                        Traslado_ImpConcepto.set('Base',Imp_Partida['Base'])
                        Traslado_ImpConcepto.set('Impuesto',Imp_Partida['Impuesto'])
                        Traslado_ImpConcepto.set('TipoFactor',Imp_Partida['TipoFactor'])
                        Traslado_ImpConcepto.set('TasaOCuota',Imp_Partida['TasaOCuota'])
                        Traslado_ImpConcepto.set('Importe',Imp_Partida['Importe'])
                    
                    if Imp_Partida['Tipo_T_R'] == 'RETENCION':                    
                        if Ret == 0:
                            Retenciones_ImpConcepto = SubElement(Impuesto_Concepto,ET.QName(nameSpace['cfdi'],'Retenciones'))
                            Ret +=1
                        Retencion_ImpConcepto = SubElement(Retenciones_ImpConcepto,ET.QName(nameSpace['cfdi'],'Retencion'))
                        Retencion_ImpConcepto.set('Base',Imp_Partida['Base'])
                        Retencion_ImpConcepto.set('Impuesto',Imp_Partida['Impuesto'])
                        Retencion_ImpConcepto.set('TipoFactor',Imp_Partida['TipoFactor'])
                        Retencion_ImpConcepto.set('TasaOCuota',Imp_Partida['TasaOCuota'])
                        Retencion_ImpConcepto.set('Importe',Imp_Partida['Importe'])
    return Conceptos

