# -*- coding: utf-8 -*-
from django.db import models
from django import forms

from django.utils.encoding import force_unicode

# Create your models here.

#def prueba():
#	return

TEST = (
	("Uno","1"), 
	("Dos","2"), 
	("Tres","3"),
)
#----------------------------------------------------------------------------------------------------
class Barras(models.Model):
     idbarra = models.IntegerField("Codigo de barras",primary_key=True, db_column='idBarra')
     codigo = models.CharField("Descripcion",max_length=200)
     class Meta:
        db_table = u'barras'
        verbose_name_plural = "Codigo de Barra"
#	help_text = u"Holaaaaaaa"
        
     def __unicode__(self):
        return force_unicode(self.codigo)

#----------------------------------------------------------------------------------------------------
class Cuentaspatrimoniales(models.Model):
     codigocuenta = models.SmallIntegerField("Codigo C. Patrimonial",primary_key=True, db_column='codigoCuenta') 
     descripcioncuenta = models.CharField("Desc C. Patrimonial",max_length=200, db_column='descripcionCuenta') 
     class Meta:
        db_table = u'cuentasPatrimoniales'
        verbose_name_plural ="Cuentas Patrimoniales"
     def __unicode__(self):
        return force_unicode(self.descripcioncuenta)
        
#----------------------------------------------------------------------------------------------------
class Unidadesmedidas(models.Model):
    descripcionunidad = models.CharField(max_length=4, db_column='descripcionUnidad') 
    idunidadmedida = models.IntegerField(primary_key=True, db_column='idUnidadMedida') 
    class Meta:
        db_table = u'unidadesMedidas'
        verbose_name_plural ="Unidad de Medida"        
    def __unicode__(self):
        return force_unicode(self.descripcionunidad)
#----------------------------------------------------------------------------------------------------
class Articulo(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo',verbose_name='Articulo')
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') 
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem', verbose_name=u'Descripción') 
     stmin = models.SmallIntegerField(db_column='stMin', verbose_name='Stock minimo')
     idbarra = models.ForeignKey(Barras, db_column='idBarra',verbose_name='Codigo de barra', blank=True, default = 0) 
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida', verbose_name='Unidad de medida', blank=True) 
     class Meta:
        db_table = u'articulo'
        verbose_name_plural ="Listado de Articulos"
     def __unicode__(self):
        return force_unicode(self.descripcionitem)

class VwArticulos(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo',verbose_name='Articulo')
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') 
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem', verbose_name=u'Descripción') 
     stmin = models.SmallIntegerField(db_column='stMin', verbose_name='Stock minimo')
     idbarra = models.ForeignKey(Barras, db_column='idBarra',verbose_name='Codigo de barra', blank=True, default = 0) 
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida', verbose_name='Unidad de medida', blank=True)
     class Meta:
        db_table = u'VW_articulos'
        verbose_name_plural ="Articulos - (Altas, Bajas, Modificaciones)"
        verbose_name = "Articulos"
     def __unicode__(self):
        return force_unicode(self.descripcionitem)

#----------------------------------------------------------------------------------------------------
class Ciudad(models.Model):
     idciudad = models.AutoField(primary_key=True, db_column='idCiudad')
     codigopostal = models.SmallIntegerField(db_column='codigoPostal')
     nombre = models.CharField(max_length=200)

     class Meta:
        db_table = u'ciudad'
	verbose_name_plural ="Ciudad"
     def __unicode__(self):
        return force_unicode(self.nombre)
        
#----------------------------------------------------------------------------------------------------
class Deposito(models.Model):
     iddeposito = models.AutoField(primary_key=True, db_column='idDeposito', editable=False)
     idciudad = models.ForeignKey(Ciudad, db_column='idCiudad') 
     telefono = models.CharField(max_length=200)
     direccion = models.CharField(max_length=200)

     class Meta:
        db_table = u'deposito'
	verbose_name_plural ="Deposito"
     def __unicode__(self):
        return force_unicode(self.direccion)
        
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Proveedor(models.Model):
     idproveedor = models.AutoField(primary_key=True, db_column='idProveedor') 
     razonsocial = models.CharField(max_length=200, db_column='razonSocial') 
     domicilio = models.CharField(max_length=200)
     ciudad =  models.ForeignKey(Ciudad, db_column='ciudad')
     telefono = models.CharField(max_length=200)

     class Meta:
         db_table = u'proveedor'
	 verbose_name_plural ="Proveedor"
     def __unicode__(self):
         return force_unicode(self.razonsocial)


#----------------------------------------------------------------------------------------------------------------------------------------------------
#===TRANSFERENCIAS==============================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Transferencia(models.Model):
     idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
     fechasalida = models.DateField(db_column='fechaSalida') 
     fechaentrada = models.DateField(db_column='fechaEntrada', blank=True) 
     depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOut') 
     confirmado = models.BooleanField(default=False)
     depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoIn') 
     
     class Meta:
        db_table = u'transferencia'
	verbose_name_plural ="Transferencia"
     def __unicode__(self):
        return force_unicode(self.idtransferencia)

class Detalletrasferencia(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(Transferencia, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
         return force_unicode('')

class VwTransfEntRw(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida',editable=False) 
    fechaentrada = models.DateField(db_column='fechaEntrada') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfEntRw',editable=False) 
    confirmado = models.BooleanField(default=False)
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfEntRw',editable=False) 
    class Meta:
        db_table = u'VW_transfEntRw'
        verbose_name_plural ="Transferencias Entrada Rawson"
        verbose_name = "Transferencia Entrada"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class VwTransfSalRw(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfSalRw', default=5, editable=False) 
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfSalRw') 
    confirmado = models.BooleanField(default=False)
    class Meta:
        db_table = u'transfSalRw'
        verbose_name_plural ="Transferencias Salida Rawson"
        verbose_name = "Transferencia Salida"

    def __unicode__(self):
        return force_unicode(self.idtransferencia)


#
class DetalleTransfEntRw(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(VwTransfEntRw, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Entrada Rawson"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class DetalleTransfSalRw(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey( VwTransfSalRw, db_column='idTransferencia')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
 
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Salida Rawson"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')
#
class VwTransfEntMadryn(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida',editable=False) 
    fechaentrada = models.DateField(db_column='fechaEntrada') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfEntMadryn',editable=False) 
    confirmado = models.BooleanField(default=False)
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfEntMadryn',editable=False) 
    class Meta:
        db_table = u'VW_transfEntMadryn'
        verbose_name_plural ="Transferencias Entrada Madryn"
        verbose_name = "Transferencia Entrada"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class VwTransfSalMadryn(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfSalMadryn',default=2, editable=False) 
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfSalMadryn') 
    confirmado = models.BooleanField(default=False)

    class Meta:
        db_table = u'transfSalMadryn'
        verbose_name_plural ="Transferencias Salida Madryn"
        verbose_name = "Transferencia Salida"

    def __unicode__(self):
        return force_unicode(self.idtransferencia)
    
    

class DetalleTransfEntMadryn(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(VwTransfEntMadryn, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Entrada Madryn"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class DetalleTransfSalMadryn(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey( VwTransfSalMadryn, db_column='idTransferencia')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Salida Madryn"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')


class VwTransfEntGaiman(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida',editable=False) 
    fechaentrada = models.DateField("Fecha de Entrada",db_column='fechaEntrada') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfEntGaiman',editable=False) 
    confirmado = models.BooleanField(default=False)
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfEntGaiman',editable=False) 
    class Meta:
        db_table = u'VW_transfEntGaiman'
        verbose_name_plural ="Transferencias Entrada Gaiman"
        verbose_name = "Transferencia Entrada"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class VwTransfSalGaiman(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfSalGaiman',default=4, editable=False) 
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfSalGaiman') 
    confirmado = models.BooleanField(default=False)
    class Meta:
        db_table = u'transfSalGaiman'
        verbose_name_plural ="Transferencias Salida Gaiman"
        verbose_name = "Transferencia Salida"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class DetalleTransfEntGaiman(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(VwTransfEntGaiman, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()#
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Entrada Gaiman"
	 unique_together = ("idtransferencia","idarticulo")

     def __unicode__(self):
        return force_unicode('')


class DetalleTransfSalGaiman(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey( VwTransfSalGaiman, db_column='idTransferencia')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()

     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Salida Gaiman"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')


class VwTransfEntSarmiento(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida',editable=False) 
    fechaentrada = models.DateField(db_column='fechaEntrada') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfEntSarmiento',editable=False) 
    confirmado = models.BooleanField(default=False)
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfEntSarmiento',editable=False) 
    class Meta:
        db_table = u'VW_transfEntSarmiento'
        verbose_name_plural ="Transferencias Entrada Sarmiento"
        verbose_name = "Transferencia Entrada"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class VwTransfSalSarmiento(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfSalSarmiento',default=1, editable=False) 
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfSalSarmiento') 
    confirmado = models.BooleanField(default=False) 
    class Meta:
        db_table = u'transfSalSarmiento'
        verbose_name_plural ="Transferencias Salida Sarmiento"
        verbose_name = "Transferencia Salida"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class DetalleTransfEntSarmiento(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(VwTransfEntSarmiento, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Entrada Sarmiento"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class DetalleTransfSalSarmiento(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey( VwTransfSalSarmiento, db_column='idTransferencia')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()

     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Salida Sarmiento"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class VwTransfEntEsquel(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida',editable=False) 
    fechaentrada = models.DateField(db_column='fechaEntrada') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfEntEsquel',editable=False) 
    confirmado = models.BooleanField(default=False)
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfEntEsquel',editable=False) 
    class Meta:
        db_table = u'VW_transfEntEsquel'
        verbose_name_plural ="Transferencias Entrada Esquel"
        verbose_name = "Transferencia Entrada"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class VwTransfSalEsquel(models.Model):
    idtransferencia = models.AutoField(primary_key=True, db_column='idTransferencia')
    fechasalida = models.DateField(db_column='fechaSalida') 
    depositoentrada = models.ForeignKey(Deposito,db_column='depositoEntrada', related_name = 'depoInTransfSalEsquel') 
    depositosalida = models.ForeignKey(Deposito, db_column='depositoSalida', related_name = 'depoOutTransfSalEsquel',default=3, editable=False) 
    confirmado = models.BooleanField(default=False)
    class Meta:
        db_table = u'transfSalEsquel'
        verbose_name_plural ="Transferencias Salida Esquel"
        verbose_name = "Transferencia Salida"
    def __unicode__(self):
        return force_unicode(self.idtransferencia)    

class DetalleTransfEntEsquel(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey(VwTransfEntEsquel, db_column='idTransferencia') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 
     cantidad = models.FloatField()
     cantidadconfirmada = models.FloatField(db_column='cantidadConfirmada')
     confirmado = models.BooleanField()
     class Meta:
         db_table = u'detalleTrasferencia'
	 verbose_name_plural ="Detalle Transferencia Entrada Esquel"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class DetalleTransfSalEsquel(models.Model):
     iddettransferencia = models.AutoField(primary_key=True, db_column='idDetTransferencia')
     idtransferencia = models.ForeignKey( VwTransfSalEsquel, db_column='idTransferencia')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()

     class Meta:
         db_table = u'detalleTrasferencia'
         verbose_name_plural ="Detalle Transferencia Salida Esquel"
	 unique_together = ("idtransferencia","idarticulo")
     def __unicode__(self):
        return force_unicode('')


#----------------------------------------------------------------------------------------------------------------------------------------------------
#==COMPRAS===========================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
TIPO_COMPRA = (
	("Caja Chica","Caja Chica"), 
	("Compra Directa","Compra Directa"), 
	("Concurso de Precios","Concurso de Precios"), 
	("Licitacion Privada","Licitacion Privada"), 
	("Licitacion Publica","Licitacion Publica"),
)

class Compra(models.Model):
     idcompra = models.AutoField(primary_key=True, db_column='idCompra')
     tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
     fecha = models.DateField()
     idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
     nroremito = models.CharField(max_length=200,db_column='nroRemito')
     nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
     nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
     observaciones = models.CharField(max_length=200)
     class Meta:
         db_table = u'compra'
         verbose_name_plural ="Compra"
     def __unicode__(self):
         return force_unicode(self.observaciones)

         
class VwComprasrw(models.Model):
    idcompra = models.AutoField(primary_key=True, db_column='idCompra')
    tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
    fecha = models.DateField()
    idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor')
    iddeposito = models.ForeignKey(Deposito, db_column='idDeposito', default=5, editable=False)
    nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
    nroremito = models.CharField(max_length=200,db_column='nroRemito')
    nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
    nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
    observaciones = models.CharField(max_length=200)
    class Meta:
        db_table = u'VW_comprasRw'
        verbose_name_plural ="Compras Rawson"
        verbose_name = "Compra"
    def __unicode__(self):
        return force_unicode(self.observaciones)    

class VwComprassarmiento(models.Model):
    idcompra = models.AutoField(primary_key=True, db_column='idCompra')
    tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
    fecha = models.DateField()
    idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor')
    iddeposito = models.ForeignKey(Deposito, db_column='idDeposito', default=1, editable=False)
    nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
    nroremito = models.CharField(max_length=200,db_column='nroRemito')
    nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
    nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
    observaciones = models.CharField(max_length=200)
    class Meta:
        db_table = u'VW_comprasSarmiento'
        verbose_name_plural ="Compra Sarmiento"
        verbose_name = "Compra"
    def __unicode__(self):
        return force_unicode(self.observaciones)    


class VwCompraspmadryn(models.Model):
    idcompra = models.AutoField(primary_key=True, db_column='idCompra')
    tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
    fecha = models.DateField()
    idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor')
    iddeposito = models.ForeignKey(Deposito, db_column='idDeposito', default=2, editable=False)
    nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
    nroremito = models.CharField(max_length=200,db_column='nroRemito')
    nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
    nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
    observaciones = models.CharField(max_length=200)
    class Meta:
        db_table = u'VW_comprasMadryn'
        verbose_name_plural ="Compra Madryn"
        verbose_name = "Compra"
    def __unicode__(self):
        return force_unicode(self.observaciones)

class VwComprasesquel(models.Model):
    idcompra = models.AutoField(primary_key=True, db_column='idCompra')
    tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
    fecha = models.DateField()
    idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor')
    iddeposito = models.ForeignKey(Deposito, db_column='idDeposito', default=3, editable=False)
    nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
    nroremito = models.CharField(max_length=200,db_column='nroRemito')
    nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
    nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
    observaciones = models.CharField(max_length=200)
    class Meta:
        db_table = u'VW_comprasEsquel'
        verbose_name_plural ="Compra Esquel"
        verbose_name = "Compra"
    def __unicode__(self):
        return force_unicode(self.observaciones)

class VwComprasgaiman(models.Model):
    idcompra = models.AutoField(primary_key=True, db_column='idCompra')
    tipo = models.CharField(max_length=200, choices=TIPO_COMPRA)
    fecha = models.DateField()
    idproveedor = models.ForeignKey(Proveedor,db_column='idProveedor', verbose_name='Proveedor')
    iddeposito = models.ForeignKey(Deposito, db_column='idDeposito', default=4, editable=False)
    nroactuacion = models.CharField(max_length=200,db_column='nroActuacion')
    nroremito = models.CharField(max_length=200,db_column='nroRemito')
    nroordencompra = models.CharField(max_length=200,db_column='nroOrdenCompra',verbose_name='OrdenCompra')
    nroexpediente = models.CharField(max_length=200,db_column='nroExpediente',verbose_name='Expediente')
    observaciones = models.CharField(max_length=200)
    class Meta:
        db_table = u'VW_comprasGaiman'
        verbose_name_plural ="Compra Gaiman"
        verbose_name = "Compra"
    def __unicode__(self):
        return force_unicode(self.observaciones)         

class Detallecomprarw(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(VwComprasrw, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle Compra Rawson"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
        return force_unicode('')
        
class Detallecomprasarmiento(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(VwComprassarmiento, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle Compra Sarmiento"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
        return force_unicode('')
        
class Detallecompramadryn(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(VwCompraspmadryn, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle Compra Madryn"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
        return force_unicode('')
        
class Detallecompragaiman(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(VwComprasgaiman, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle Compra Gaiman"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
        return force_unicode('')

         
class Detallecompraesquel(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(VwComprasesquel, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle compra Esquel"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class Detallecompra(models.Model):
     iddetcompra = models.AutoField(primary_key=True, db_column='idDetCompra')
     idcompra = models.ForeignKey(Compra, db_column='idCompra') 
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo')
     cantidad = models.FloatField()
     preciounitario = models.CharField(max_length=200, db_column='precioUnitario')

     class Meta:
         db_table = u'detalleCompra'
	 verbose_name_plural ="Detalle Compra"
	 unique_together = ("idcompra","idarticulo")
     def __unicode__(self):
         return force_unicode('')

#----------------------------------------------------------------------------------------------------------------------------------------------------
#==DEVOLUCIONES======================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Devoluciones(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()
     
     class Meta:
         db_table = u'devoluciones'
	 verbose_name_plural ="Devoluciones"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class Devoluciongaiman(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito',editable=False,default=4) # Field name made lowercase.
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()

     class Meta:
         db_table = u'devolucionesGaiman'
	 verbose_name_plural ="Devoluciones Gaiman"
         verbose_name = "Articulo Devolucion"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class Devolucionmadryn(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito',editable=False,default=2) # Field name made lowercase.
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()
     
     class Meta:
         db_table = u'devolucionesMadryn'
	 verbose_name_plural ="Devoluciones Madryn"
         verbose_name = "Articulo Devolucion"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class Devolucionrw(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito',editable=False,default=5) # Field name made lowercase.
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()

     class Meta:
         db_table = u'devolucionesRw'
	 verbose_name_plural ="Devoluciones Rawson"
         verbose_name = "Articulo Devolucion"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class Devolucionsarmiento(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito',editable=False,default=1) # Field name made lowercase.
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()
     
     class Meta:
         db_table = u'devolucionesSarmiento'
	 verbose_name_plural ="Devoluciones Sarmiento"
         verbose_name = "Articulo Devolucion"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class Devolucionesquel(models.Model):
     iddevolucion = models.AutoField(primary_key=True, db_column='idDevolucion')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito',editable=False,default=3)
     observaciones = models.CharField(max_length=200)
     idproveedor =  models.ForeignKey(Proveedor, db_column='idProveedor')
     fecha = models.DateField()
     
     class Meta:
         db_table = u'devolucionesEsquel'
	 verbose_name_plural ="Devoluciones Esquel"
         verbose_name = "Articulo Devolucion"
     def __unicode__(self):
         return force_unicode(self.observaciones)

class DetalledevolucionRw(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devolucionrw,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion Rawson"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')

class DetalledevolucionMadryn(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devolucionmadryn,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion Madryn"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')

class DetalledevolucionSarmiento(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devolucionsarmiento,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion Sarmiento"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')

class DetalledevolucionGaiman(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devoluciongaiman,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion Gaiman"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')

class DetalledevolucionEsquel(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devolucionesquel,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion Esquel"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')

class Detalledevolucion(models.Model):
     iddetdevolucion = models.AutoField(primary_key=True, db_column='idDetDevolucion')
     iddevolucion = models.ForeignKey(Devoluciones,db_column='idDevolucion') # Field name made lowercase.
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo,db_column='idArticulo') # Field name made lowercase.
     observacion = models.CharField(max_length=200)

     class Meta:
         db_table = u'detalleDevolucion'
	 verbose_name_plural ="Detalle Devolucion"
	 unique_together = ("iddevolucion","idarticulo")
         verbose_name = "Detalle Articulo Devolucion"
     def __unicode__(self):
         return force_unicode('')
#----------------------------------------------------------------------------------------------------------------------------------------------------
         
class Articulodeposito(models.Model):
     idarticulodeposito = models.AutoField(primary_key=True, db_column='idArticuloDeposito',verbose_name = 'idArtDeposito')
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') # Field name made lowercase.
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito') # Field name made lowercase.
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')
     nroficha = models.SmallIntegerField(db_column='nroFicha')
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)

     class Meta:
         db_table = u'articuloDeposito'
	 verbose_name_plural ="Articulo Deposito (Stock)"
     def __unicode__(self):
         return force_unicode(self.idarticulo)


#----------------------------VW Aticulos-----------------------------------------------------------
#----------------------------Rawson----------------------------------------------------------------

#class ArticuloDepositoAd(models.Model):
#     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
#     
#     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial')
#     nroficha = models.SmallIntegerField(db_column='nroFicha')
#     
#     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem')
#     mueble = models.CharField(max_length=200)
#     casillero = models.CharField(max_length=200)
#     stmin = models.SmallIntegerField(db_column='stMin')
#     idbarra = models.ForeignKey(Barras, db_column='idBarra')
#     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida')
#     stock = models.FloatField()
#     stockentrante = models.FloatField(db_column='stockEntrante')
#     stocksaliente = models.FloatField(db_column='stockSaliente')
#     class Meta:
#         db_table = u'depoAdmin'
#         verbose_name_plural ="Articulos de los Deposito "
#     def __unicode__(self):
#         return force_unicode(self.idarticulo)

class ArticuloDepositoRawson(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
     
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial')
     nroficha = models.SmallIntegerField(db_column='nroFicha')
     
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem',verbose_name='Descripcion')
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)
     stmin = models.SmallIntegerField(db_column='stMin')
     idbarra = models.ForeignKey(Barras, db_column='idBarra')
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida')
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')

     class Meta:
         db_table = u'depositoRw'
         verbose_name_plural ="Articulos Deposito Rawson"
         verbose_name = "Articulo Deposito"
     def __unicode__(self):
         return force_unicode(self.idarticulo)

#----------------------------Sarmiento----------------------------------------------------------------
class ArticuloDepositoSarmiento(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
     
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') # Field n$
     nroficha = models.SmallIntegerField(db_column='nroFicha') # Field name made lowercase.
     
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem',verbose_name='Descripcion') # Field name made lowercas$
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)
     stmin = models.SmallIntegerField(db_column='stMin') # Field name made lowercase.
     idbarra = models.ForeignKey(Barras, db_column='idBarra') # Field name made lowercase.
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida') # Field name made lowercase.
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')

     class Meta:
         db_table = u'depositoSarmiento'
         verbose_name_plural ="Articulos Deposito Sarmiento"
         verbose_name = "Articulo Deposito"
     def __unicode__(self):
         return force_unicode(self.idarticulo)


#----------------------------Esquel----------------------------------------------------------------
class ArticuloDepositoEsquel(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
     
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') # Field n$
     nroficha = models.SmallIntegerField(db_column='nroFicha') # Field name made lowercase.
     
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem',verbose_name='Descripcion') # Field name made lowercas$
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)
     stmin = models.SmallIntegerField(db_column='stMin') # Field name made lowercase.
     idbarra = models.ForeignKey(Barras, db_column='idBarra') # Field name made lowercase.
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida') # Field name made lowercase.
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')

     class Meta:
         db_table = u'depositoEsquel'
         verbose_name_plural ="Articulos Deposito Esquel"
         verbose_name = "Articulo Deposito"
     def __unicode__(self):
         return force_unicode(self.idarticulo)

#----------------------------Gaiman----------------------------------------------------------------
class ArticuloDepositoGaiman(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
     
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') # Field n$
     nroficha = models.SmallIntegerField(db_column='nroFicha') # Field name made lowercase.
     
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem',verbose_name='Descripcion') # Field name made lowercas$
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)
     stmin = models.SmallIntegerField(db_column='stMin') # Field name made lowercase.
     idbarra = models.ForeignKey(Barras, db_column='idBarra') # Field name made lowercase.
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida') # Field name made lowercase.
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')

     class Meta:
         db_table = u'depositoGaiman'
         verbose_name_plural ="Articulos Deposito Gaiman"
         verbose_name = "Articulo Deposito"
     def __unicode__(self):
         return force_unicode(self.idarticulo)

#----------------------------Madryn----------------------------------------------------------------
class ArticuloDepositoMadryn(models.Model):
     idarticulo = models.AutoField(primary_key=True, db_column='idArticulo')
     
     nrocuentapatrimonial = models.ForeignKey(Cuentaspatrimoniales, db_column='nroCuentaPatrimonial',verbose_name='CtaPatrimonial') # Field n$
     nroficha = models.SmallIntegerField(db_column='nroFicha') # Field name made lowercase.
     
     descripcionitem = models.CharField(max_length=200, db_column='descripcionItem',verbose_name='Descripcion') # Field name made lowercas$
     mueble = models.CharField(max_length=200)
     casillero = models.CharField(max_length=200)
     stmin = models.SmallIntegerField(db_column='stMin') # Field name made lowercase.
     idbarra = models.ForeignKey(Barras, db_column='idBarra') # Field name made lowercase.
     unidadmedida = models.ForeignKey(Unidadesmedidas, db_column='unidadMedida') # Field name made lowercase.
     stock = models.FloatField()
     stockentrante = models.FloatField(db_column='stockEntrante')
     stocksaliente = models.FloatField(db_column='stockSaliente')

     class Meta:
         db_table = u'depositoMadryn'
         verbose_name_plural ="Articulos Deposito Madryn"
         verbose_name = "Articulo Deposito"
     def __unicode__(self):
         return force_unicode(self.idarticulo)

        
#----------------------------Historial Precio-----------------------------------------------------------
class HistorialPrecios(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoRawson, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')

class HistorialPreciosArticulo(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(Articulo, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------

class HistorialPreciosrw(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoRawson, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------
class HistorialPreciosmadryn(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoMadryn, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------
class HistorialPreciosgaiman(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoGaiman, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------
class HistorialPreciossarmiento(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoSarmiento, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------
class HistorialPreciosesquel(models.Model):
     idhistorialprecios = models.AutoField(primary_key=True, db_column='idHistorialPrecios')
     idarticulo =  models.ForeignKey(ArticuloDepositoEsquel, db_column='idArticulo')
     idproveedor = models.ForeignKey(Proveedor, db_column='idProveedor')
     iddeposito = models.ForeignKey(Deposito, db_column='idDeposito')
     fecha = models.DateField(db_column='Fecha')
     iddetcompra = models.ForeignKey(Detallecompra, db_column='idDetCompra', editable=False)
     precio = models.CharField(max_length=200, db_column='precio')
     class Meta:
         db_table = u'historialPrecios'
         verbose_name_plural ="Historial Precios"
     def __unicode__(self):
         return force_unicode('')
#--------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------
#==SALIDAS===========================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
class Salida(models.Model):
     idsalida = models.AutoField(primary_key=True, db_column='idSalida')
     fecha = models.DateField()
     entregadoa = models.CharField(max_length=200, db_column='entregadoA') 
     destino = models.CharField(max_length=200)
     observaciones = models.CharField(max_length=200)
     iddeposito =models.ForeignKey(Deposito,db_column='idDeposito') 

     class Meta:
        db_table = u'salida'
	verbose_name_plural ="Salida"
     def __unicode__(self):
        return force_unicode(self.observaciones)

class Detallesalida(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(Salida, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
	verbose_name_plural ="Detalle Salida"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode(self.idsalida)


class VwSalidaesquel(models.Model):
    idsalida = models.AutoField(primary_key=True, db_column='idSalida')
    fecha = models.DateField(null=True)
    entregadoa = models.CharField(max_length=200, db_column='entregadoA') # Field name made lowercase.
    destino = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)
    iddeposito = models.ForeignKey(Deposito,db_column='idDeposito',default=3, editable=False) # Field name made lowercase.
    
    class Meta:
        db_table = u'VW_salidaEsquel'
	verbose_name_plural ="Salida Esquel"
        verbose_name = "Salida"
    def __unicode__(self):
         return force_unicode(self.observaciones)

class DetallesalidaEsquel(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(VwSalidaesquel, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
        verbose_name_plural ="Detalle Salida Esquel"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class VwSalidagaiman(models.Model):
    idsalida = models.AutoField(primary_key=True, db_column='idSalida')
    fecha = models.DateField(null=True)
    entregadoa = models.CharField(max_length=200, db_column='entregadoA') 
    destino = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)
    iddeposito = models.ForeignKey(Deposito,db_column='idDeposito',default=4, editable=False) 
    
    class Meta:
        db_table = u'VW_salidaGaiman'
	verbose_name_plural ="Salida Gaiman"
        verbose_name = "Salida" 
    def __unicode__(self):
         return force_unicode(self.observaciones)

class DetallesalidaGaiman(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(VwSalidagaiman, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
        verbose_name_plural ="Detalle Salida Gaiman"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode('')


class VwSalidasarmiento(models.Model):
    idsalida = models.AutoField(primary_key=True, db_column='idSalida')
    fecha = models.DateField(null=True)
    entregadoa = models.CharField(max_length=200, db_column='entregadoA') 
    destino = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)
    iddeposito = models.ForeignKey(Deposito,db_column='idDeposito',default=1, editable=False) 
    
    class Meta:
        db_table = u'VW_salidaSarmiento'
	verbose_name_plural ="Salida Sarmiento"
        verbose_name = "Salida"
    def __unicode__(self):
         return force_unicode(self.observaciones)

class DetallesalidaSarmiento(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(VwSalidasarmiento, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
        verbose_name_plural ="Detalle Salida Sarmiento"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class VwSalidamadryn(models.Model):
    idsalida = models.AutoField(primary_key=True, db_column='idSalida')
    fecha = models.DateField(null=True)
    entregadoa = models.CharField(max_length=200, db_column='entregadoA') 
    destino = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)
    iddeposito = models.SmallIntegerField(null=True, db_column='idDeposito', default=2,editable=False) 
    
    class Meta:
        db_table = u'VW_salidaMadryn'
	verbose_name_plural ="Salida Madryn"
        verbose_name = "Salida"
    def __unicode__(self):
         return force_unicode(self.observaciones)

class DetallesalidaMadryn(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(VwSalidamadryn, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
        verbose_name_plural ="Detalle Salida Madryn"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode('')

class VwSalidarw(models.Model):
    idsalida = models.AutoField(primary_key=True, db_column='idSalida')
    fecha = models.DateField(null=True)
    entregadoa = models.CharField(max_length=200, db_column='entregadoA') 
    destino = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=200)
    iddeposito = models.ForeignKey(Deposito,db_column='idDeposito',default=5, editable=False) 
    
    class Meta:
        db_table = u'VW_salidaRw'
	verbose_name_plural ="Salida Rawson"
        verbose_name = "Salida"
    def __unicode__(self):
         return force_unicode(self.observaciones)

class DetallesalidaRw(models.Model):
     iddetsalida = models.AutoField(primary_key=True, db_column='idDetSalida')
     idsalida = models.ForeignKey(VwSalidarw, db_column='idSalida') 
     cantidad = models.FloatField()
     idarticulo = models.ForeignKey(Articulo, db_column='idArticulo') 

     class Meta:
        db_table = u'detalleSalida'
        verbose_name_plural ="Detalle Salida Rawson"
	unique_together = ("idsalida","idarticulo")
     def __unicode__(self):
        return force_unicode('')


#*********************************************************************************************************************************
#***MODELOS-DJANGO****************************************************************************************************************
#*********************************************************************************************************************************

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'
    def __unicode__(self):
        return force_unicode(self.username)    
        
class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'
    def __unicode__(self):
        return force_unicode(self.name)    
        
class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'
    def __unicode__(self):
        return force_unicode(self.session_data)    
        
class Log(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.TextField()
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'
    def __unicode__(self):
        return force_unicode(self.user)
