
from gc import collect
from rest_framework import serializers
from collections import OrderedDict
from Comp.models import * 
from REP.models import * 

class Impuesto_PartidasIngreso_Serializer(serializers.ModelSerializer):
    Partidas_id = serializers.PrimaryKeyRelatedField(queryset=Ingreso_Conceptos.objects.all(), source='Imp_Partida.id')
    class Meta:
        model = Impuesto_PartidasIngreso
        fields = '__all__'

class IngresoPartidas_Serializer(serializers.ModelSerializer):
    Ingreso_id  = serializers.PrimaryKeyRelatedField(queryset=Ingreso.objects.all(), source='Comprobante.id')
    Imp_Partida   = Impuesto_PartidasIngreso_Serializer(many=True, read_only=True)
    class Meta:
        model  = Ingreso_Conceptos        
        fields =['id','Ingreso_id','ClaveProdServ'
        , 'Descuento', 'ObjetoImp', 'Cantidad', 'ClaveUnidad'
        , 'Unidad', 'Descripcion', 'ValorUnitario', 'Importe'
        , 'IVA', 'IVA_Ret', 'ISR'

        ,'Imp_Partida',]
    

class IngresoDocumentoRelacionados_Serializer(serializers.ModelSerializer):
    CFDI_Rel = serializers.PrimaryKeyRelatedField(queryset=Ingreso.objects.all(), source='CFDI_Rel.id')
    class Meta:
        model = CfdiRelacionados_Ingreso
        fields = '__all__'

class Ingreso_Serializer(serializers.ModelSerializer):
    
    partidasIngreso = IngresoPartidas_Serializer(many=True, read_only=False, required=False)

    CFDI_REL_Comprobante = IngresoDocumentoRelacionados_Serializer(many=True, read_only=True)
    class Meta:
        model   = Ingreso
        fields  = ('id','Ingreso','Version', 'Serie', 'Folio'
        , 'Fecha', 'TipoCambio', 'Moneda', 'FormaPago'
        , 'Exportacion', 'MetodoPago', 'LugarExpedicion'
        , 'TipoDeComprobante', 'NoCertificado', 'Certificado'
        , 'Sello', 'SubTotal', 'Descuento', 'CondicionesDePago'
        , 'Total', 'Confirmacion', 'created_at', 'Estado_CFDI'
        , 'IVA', 'IVA_Ret', 'ISR', 'UUID'

        , 'Rfc_Emi', 'Nombre_Emi', 'RegimenFiscal_Emi'
        , 'Rfc_Rec', 'Nombre_Rec', 'RegimenFiscal_Rec', 'DomicilioFiscal_Rec', 'ResidenciaFiscal_Rec', 'NumRegIdTrib_Rec', 'UsoCFDI_Rec'

        , 'CFDI_REL_Comprobante'
        , 'partidasIngreso')
        depth =2
        
    def create(self, validated_data):
        
        partidas_data = validated_data.pop('partidasIngreso')
        ingreso = Ingreso.objects.create(**validated_data)
        for partida_data in partidas_data:
            
            # print('---------------', partida_data)
            # print(ingreso)
            # need to get removed from partidas_data, because is in the json
            # so when the instance of ingreso are passed to Ingreso_Conceptos create, are addes to the partidas instance to 
            # gives they its own instance of ingreso to partidas
            partida_data.pop('Comprobante', None) 

            Ingreso_Conceptos.objects.create(Comprobante=ingreso, **partida_data)
        return ingreso
    
    def update(self, instance, validated_data):
        partidas= self.data['partidasIngreso']
        
        
        print(type(partidas))
        for coll in partidas:
            collect = [ (key, val) for key, val in coll.items()]
            
            del collect[-1]
            print(collect)
            #('id', 1), ('Ingreso_id', 61), ('ClaveProdServ', '10101500'), 
            #('Descuento', '0.000000'), ('ObjetoImp', '02'), ('Cantidad', '12.000000'), 
            #('ClaveUnidad', 'E48'), ('Unidad', 'E48'), 
            #('Descripcion', 'Animales vivos de granja'), ('ValorUnitario', '2.000000'),
            #('Importe', '24.000000'), ('IVA', True), ('IVA_Ret', True), ('ISR', True)

            obj, created = Ingreso_Conceptos.objects.update_or_create(
                id=collect[0][1], 
                #Ingreso_id=collect[1][1],
                ClaveProdServ=collect[2][1],
                Descuento = collect[3][1],
                ObjetoImp = collect[4][1],
                Cantidad = collect[5][1],
                ClaveUnidad = collect[6][1],
                Unidad  = collect[7][1]

            )   
            print(obj, created)

        return instance

#Serializers REP Init------------------------------->
class Pagos_Impuestos_DRs_Serializer(serializers.ModelSerializer):
    docto_rel= serializers.PrimaryKeyRelatedField(queryset=DoctoRelacionado_Pagos.objects.all(), source='docto_rel.id')
    class Meta:
        model = ImpuestoDR_Pagos
        fields= '__all__'

class Pagos_DocumentosRelacionados_serializer(serializers.ModelSerializer):
    Pago_rel = serializers.PrimaryKeyRelatedField(queryset=Pagos.objects.all(), source='Pago_rel.id')
    DR_Pagos_Impuestos = Pagos_Impuestos_DRs_Serializer(many=True,read_only=True)
    class Meta:
        model = DoctoRelacionado_Pagos
        fields = ('id','Pago_rel', 'IdDocumento', 'Serie', 'Folio'
        ,'MonedaDR', 'EquivalenciaDR', 'NumParcialidad'
        ,'ImpSaldoAnt', 'ImpPagado', 'ImpSaldoInsoluto', 'ObjetoImp'
        
        ,'DR_Pagos_Impuestos'
        )
class PagoDocumentoRelacionado_Serializer(serializers.ModelSerializer):
    CFDI_Rel = serializers.PrimaryKeyRelatedField(queryset=ComprobantePagos.objects.all(), source='CFDI_Rel.id')
    class Meta:
        model = CfdiRelacionados_REP
        fields = '__all__'
class Pagos_Serializer(serializers.ModelSerializer):
    Pagos_DR = Pagos_DocumentosRelacionados_serializer(many=True, read_only=True)        
    class Meta:
        model = Pagos
        fields=('CompPago', 'FechaPago', 'FormaDePagoP'
        , 'MonedaP', 'TipoCambioP', 'Monto', 'RfcEmisorCtaOrd'
        , 'NomBancoOrdExt', 'CtaOrdenante', 'RfcEmisorCtaBen'
        , 'CtaBeneficiario'
        , 'Pagos_DR'
        )

class Pago_Serializer(serializers.ModelSerializer):
    CFDI_REL_REP = PagoDocumentoRelacionado_Serializer(many=True, read_only=True)
    Pagos_Rep    = Pagos_Serializer(many=True, read_only=True)
    class Meta:
        model = ComprobantePagos
        fields = ('id','Version', 'Serie', 'Folio', 'NumPago'
        , 'Fecha', 'TipoCambio', 'Moneda', 'FormaPago'
        , 'Exportacion', 'MetodoPago', 'LugarExpedicion'
        , 'TipoDeComprobante', 'NoCertificado', 'Certificado'
        , 'Sello', 'SubTotal', 'Descuento', 'CondicionesDePago'
        , 'Total', 'Confirmacion', 'created_at', 'Estado_CFDI'
        , 'IVA', 'IVA_Ret', 'ISR', 'UUID'

        , 'Rfc_Emi', 'Nombre_Emi', 'RegimenFiscal_Emi'
        , 'Rfc_Rec', 'Nombre_Rec', 'RegimenFiscal_Rec', 'DomicilioFiscal_Rec', 'ResidenciaFiscal_Rec', 'NumRegIdTrib_Rec', 'UsoCFDI_Rec'

        ,'CFDI_REL_REP'
        ,'Pagos_Rep'
        )


