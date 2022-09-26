from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

@dataclass
class InformacionGlobal:
	Periodicidad:str
	Meses:dict = {}
	Anio:int = None

@dataclass
class CfdiRelacionados:
    TipoRelacion:List[dict]


@dataclass
class Emisor:
	Rfc:str
	Nombre:str
	RegimenFisacl:str
	FacAtrAdquirente:str=None
	

@dataclass
class Receptor:
    pass

@dataclass
class Conceptos:
    pass

@dataclass
class Impuestos:
    pass

@dataclass
class Complemento:
    pass



@dataclass
class Comprobante:
    Version:str
    Serie:str = None
    Folio:str = None
    Fecha:str= None
    Sello:str= None
    FormaPago:str= None
    NoCertificado:str= None
    Certificado:str= None
    CondicionesDePago:str= None
    SubTotal:Decimal= None
    Descuento:Decimal= None
    Moneda:Decimal= None
    TipoCambio:Decimal= None
    Total:Decimal= None
    TipoDeComprobante:str= None
    Exportacion:str= None
    MetodoPago:str= None
    LugarExpedicion:str= None
    Confirmacion:str= None
    InfoGlobal:List[InformacionGlobal] = field(default_factory= list)

