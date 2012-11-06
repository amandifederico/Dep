# -*- coding: utf-8 -*-
from depoapp.models import *
from django.db.models import base
from django.contrib import admin

#En este archivo se define como se va a mostrar los datos en la interfaz administrativa, a su vez aqui tambien se definen filtros, y campos por los 
#cuales se podra

#---------------------------------------------------------------------------------------------------------------------------------------------------
#==HISTORIAL-PRECIOS================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------
class HistorialPreciosInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPrecios
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']

class HistorialPreciosrwInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciosrw
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']
#-----------------------------------------------------------------------------------------------------------------------$

class HistorialPreciosArticuloInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciosArticulo
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']

#-----------------------------------------------------------------------------------------------------------------------$

class HistorialPreciosgaimanInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciosgaiman
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']
#-----------------------------------------------------------------------------------------------------------------------$

class HistorialPreciossarmientoInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciossarmiento
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']
#-----------------------------------------------------------------------------------------------------------------------$

class HistorialPreciosesquelInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciosesquel
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']
#-----------------------------------------------------------------------------------------------------------------------$

class HistorialPreciosmadrynInline(admin.TabularInline):
     list_display = ('idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     model = HistorialPreciosmadryn
     readonly_fields=( 'idarticulo', 'idproveedor', 'iddeposito', 'fecha','precio',)
     ordering = ['-fecha']
#---------------------------------------------------------------------------------------------------------------------------------------------------
#==ARTICULO=========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------
#class ArticuloAdmin(ReadPermissionModelAdmin):
class ArticuloAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosArticuloInline]
     list_display = ['descripcionitem']
     search_fields = ['descripcionitem','idbarra__idbarra']
     readonly_fields = ('idarticulo','nrocuentapatrimonial','descripcionitem','stmin','idbarra','unidadmedida',)

class ArticulodepositoAdmin(admin.ModelAdmin):
     #inlines = [HistorialPreciosInline]
     #list_display = ['idarticulo','iddeposito','stock','stockentrante', 'stocksaliente','casillero','mueble','nroficha']

     list_filter = ('iddeposito',)
     search_fields = ('idarticulo__descripcionitem','iddeposito__direccion',)
     ordering = ('idarticulo',)
     readonly_fields = ('idarticulo','iddeposito','stock','stockentrante', 'stocksaliente','casillero','mueble','nroficha',)

class VwArticulosAdmin(admin.ModelAdmin):
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     raw_id_fields = ('idbarra','nrocuentapatrimonial')

#---------------------------------------------------------------------------------------------------------------------------------------------------
#==CIUDAD===========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class CiudadAdmin(admin.ModelAdmin):
     list_display = ('nombre','codigopostal',)
     
#---------------------------------------------------------------------------------------------------------------------------------------------------
#==CUENTAS-PATRIMONIALES============================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class CuentaspatrimonialesAdmin(admin.ModelAdmin):
     list_display = ('descripcioncuenta','codigocuenta',)
     
#---------------------------------------------------------------------------------------------------------------------------------------------------
#=DEPOSITO==========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class DepositoAdmin(admin.ModelAdmin):
     list_display = ('idciudad','telefono','direccion',)

class vwdepositoAdAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#RAWSON
class vwdepositorawsonAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosrwInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#ESQUEL
class vwdepositoesquelAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosesquelInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#SARMIENTO
class vwdepositosarmientoAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciossarmientoInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#MADRYN
class vwdepositomadrynAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosmadrynInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#GAIMAN
class vwdepositogaimanAdmin(admin.ModelAdmin):
     inlines = [HistorialPreciosgaimanInline]
     search_fields = ('descripcionitem',)
     ordering = ('descripcionitem',)
     list_display = ('descripcionitem','stock', 'stockentrante', 'stocksaliente',)
     readonly_fields = ('stock', 'stockentrante', 'stocksaliente','descripcionitem','idbarra','stmin','unidadmedida','nrocuentapatrimonial',)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#==PROVEEDOR========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class ProveedorAdmin(admin.ModelAdmin):
     list_display = ('razonsocial','domicilio','ciudad','telefono',)
     list_filter = ('ciudad',)
     search_fields = ('razonsocial','domicilio',)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#==COMPRA===========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class DetalleCompraInline(admin.TabularInline):
     model = Detallecompra
     raw_id_fields = ('idarticulo',)

class DetallecompraAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)
     

class CompraAdmin(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('-fecha',)
     inlines = [DetalleCompraInline]
     raw_id_fields = ('idproveedor',)

#RAWSON

class DetalleComprarwInline(admin.TabularInline):
     model = Detallecomprarw
     raw_id_fields = ('idarticulo',)

class DetallecomprarwAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)

   
class CompraAdminrw(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('-fecha',)
     inlines = [DetalleComprarwInline]
     raw_id_fields = ('idproveedor',)
     
#SARMIENTO

class DetalleComprasarmientoInline(admin.TabularInline):
     model = Detallecomprasarmiento
     raw_id_fields = ('idarticulo',)

class DetallecomprasarmientoAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)


class CompraAdminsarmiento(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('-fecha',)
     inlines = [DetalleComprasarmientoInline]   
     raw_id_fields = ('idproveedor',)
#MADRYN

class DetalleCompramadrynInline(admin.TabularInline):
     model = Detallecompramadryn
     raw_id_fields = ('idarticulo',)

class DetallecompramadrynAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)

     
class CompraAdminpmadryn(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('-fecha',)
     inlines = [DetalleCompramadrynInline]
     raw_id_fields = ('idproveedor',)
     
#GAIMAN

class DetalleCompragaimanInline(admin.TabularInline):
     model = Detallecompragaiman
     raw_id_fields = ('idarticulo',)


class DetallecompragaimanAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)
     #search_fields =('articulo__idbarra',)
     
class CompraAdmingaiman(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('fecha',)
     inlines = [DetalleCompragaimanInline]    
     raw_id_fields = ('idproveedor',)
     
#ESQUEL

class DetalleCompraesquelInline(admin.TabularInline):
     model = Detallecompraesquel
     raw_id_fields = ('idarticulo',)

class DetallecompraesquelAdmin(admin.ModelAdmin):
     list_display = ('iddetcompra',)


class CompraAdminesquel(admin.ModelAdmin):
     list_display = ('fecha','observaciones','tipo','idproveedor','iddeposito','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     list_filter = ('iddeposito','tipo')
     search_fields = ('observaciones','fecha','nroactuacion','nroordencompra','nroexpediente','nroremito',)
     ordering = ('fecha',)
     inlines = [DetalleCompraesquelInline]    
     raw_id_fields = ('idproveedor',)     

#---------------------------------------------------------------------------------------------------------------------------------------------------
#==SALIDA===========================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class DetalleSalidaInline(admin.TabularInline):
     model = Detallesalida
     raw_id_fields = ('idarticulo',)     
     
class SalidaAdmin(admin.ModelAdmin):
      inlines = [DetalleSalidaInline]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      list_filter = ('iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)

#ESQUEL
class DetalleSalidaInlineEsquel(admin.TabularInline):
     model = DetallesalidaEsquel
     raw_id_fields = ('idarticulo',)

class SalidaAdminEsquel(admin.ModelAdmin):
      inlines = [DetalleSalidaInlineEsquel]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)

#GAIMAN
class DetalleSalidaInlineGaiman(admin.TabularInline):
     model = DetallesalidaGaiman
     raw_id_fields = ('idarticulo',)

class SalidaAdminGaiman(admin.ModelAdmin):
      inlines = [DetalleSalidaInlineGaiman]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)

#SARMIENTO
class DetalleSalidaInlineSarmiento(admin.TabularInline):
     model = DetallesalidaSarmiento
     raw_id_fields = ('idarticulo',)

class SalidaAdminSarmiento(admin.ModelAdmin):
      inlines = [DetalleSalidaInlineSarmiento]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)

#MADRYN
class DetalleSalidaInlineMadryn(admin.TabularInline):
     model = DetallesalidaMadryn
     raw_id_fields = ('idarticulo',)


class SalidaAdminMadryn(admin.ModelAdmin):
      inlines = [DetalleSalidaInlineMadryn]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)

#RAWSON
class DetalleSalidaInlineRw(admin.TabularInline):
     model = DetallesalidaRw
     raw_id_fields = ('idarticulo',)

class SalidaAdminRw(admin.ModelAdmin):
      inlines = [DetalleSalidaInlineRw]
      list_display = ('fecha','observaciones','entregadoa','destino','iddeposito',)
      search_fields = ('fecha','entregadoa','destino','observaciones',)
      ordering = ('-fecha',)


#---------------------------------------------------------------------------------------------------------------------------------------------------
#==DEVOLUCIONES=====================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class DetalleDevolucionesInline(admin.TabularInline):
     model = Detalledevolucion
     raw_id_fields = ('idarticulo',)

class DevolucionesAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesInline]
     list_filter = ('iddeposito',)
     raw_id_fields = ('idproveedor',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')
     
#GAIMAN

class DetalleDevolucionesGaimanInline(admin.TabularInline):
     model = DetalledevolucionGaiman
     raw_id_fields = ('idarticulo',)

class DevolucionesGaimanAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesGaimanInline]
     raw_id_fields = ('idproveedor',)
#     list_display = ('idcompra','descripcion',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')

#ESQUEL

class DetalleDevolucionesEsquelInline(admin.TabularInline):
     model = DetalledevolucionEsquel
     raw_id_fields = ('idarticulo',)

class DevolucionesEsquelAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesEsquelInline]
     raw_id_fields = ('idproveedor',)
#     list_display = ('idcompra','descripcion',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')

#RAWSON

class DetalleDevolucionesRawsonInline(admin.TabularInline):
     model = DetalledevolucionRw
     raw_id_fields = ('idarticulo',)

class DevolucionesRawsonAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesRawsonInline]
     raw_id_fields = ('idproveedor',)
#     list_display = ('idcompra','iddeposito','descripcion',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')

#MADRYN

class DetalleDevolucionesMadrynInline(admin.TabularInline):
     model = DetalledevolucionMadryn
     raw_id_fields = ('idarticulo',)

class DevolucionesMadrynAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesMadrynInline]
     raw_id_fields = ('idproveedor',)
#     list_display = ('idcompra','descripcion',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')


#SARMIENTO

class DetalleDevolucionesSarmientoInline(admin.TabularInline):
     model = DetalledevolucionSarmiento
     raw_id_fields = ('idarticulo',)

class DevolucionesSarmientoAdmin(admin.ModelAdmin):
     inlines = [DetalleDevolucionesSarmientoInline]
     raw_id_fields = ('idproveedor',)
#     list_display = ('idcompra'	,'descripcion',)
#     search_fields = ('idcompra__observacion','iddeposito__direccion')


#---------------------------------------------------------------------------------------------------------------------------------------------------
#==TRANSFERENCIA====================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class DetalleTransferenciaInline(admin.TabularInline):
     model = Detalletrasferencia 
     
class TransferenciaAdmin(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInline]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)



#SALIDA-RAWSON

class DetalleTransferenciaInlineTransfSalRw(admin.TabularInline):
     model = DetalleTransfSalRw
     raw_id_fields = ('idarticulo',)

class TransfSalRw(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfSalRw]
     list_display = ('fechasalida','depositoentrada','confirmado')
     list_filter = ('depositoentrada','depositosalida')
     search_fields = ('fechasalida','depositoentrada__direccion')
     readonly_fields=( 'confirmado',)

     
#ENTRADA-RAWSON

class DetalleTransferenciaInlineTransfEntRw(admin.TabularInline):
     model = DetalleTransfEntRw
     readonly_fields = ('cantidad','confirmado','idarticulo',) 

 
class TransfEntRw(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfEntRw]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)
 
#SALIDA-MADRYN

class DetalleTransferenciaInlineTransfSalMadryn(admin.TabularInline):
     model = DetalleTransfSalMadryn
     raw_id_fields = ('idarticulo',)

class TransfSalMadryn(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfSalMadryn]
     list_display = ('fechasalida','depositoentrada','confirmado')
     list_filter = ('depositoentrada','depositosalida')
     search_fields = ('fechasalida','depositoentrada__direccion')          
     #readonly_fields = ('confirmado',)
     model = VwTransfSalMadryn()
     type(model.confirmado)
     if model.confirmado ==True:
         readonly_fields = ('fechasalida','depositoentrada','confirmado',)
     else:
         readonly_fields = ('confirmado',)

#ENTRADA-MADRYN

class DetalleTransferenciaInlineTransfEntMadryn(admin.TabularInline):
     model = DetalleTransfEntMadryn
     readonly_fields = ('cantidad','confirmado','idarticulo',) 

 
class TransfEntMadryn(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfEntMadryn]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)     
     readonly_fields=( 'confirmado',)

#SALIDA-GAIMAN

class DetalleTransferenciaInlineTransfSalGaiman(admin.TabularInline):
     model = DetalleTransfSalGaiman
     raw_id_fields = ('idarticulo',)
     
class TransfSalGaiman(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfSalGaiman]
     list_display = ('fechasalida','depositoentrada','confirmado',)
     list_filter = ('depositoentrada','depositosalida')
     search_fields = ('fechasalida','depositoentrada__direccion')     
     readonly_fields=( 'confirmado',)

#ENTRADA-GAIMAN

class DetalleTransferenciaInlineTransfEntGaiman(admin.TabularInline):
     model = DetalleTransfEntGaiman
     readonly_fields = ('cantidad','confirmado','idarticulo',) 

 
class TransfEntGaiman(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfEntGaiman]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)
     readonly_fields=( 'confirmado',)

#SALIDA-SARMIENTO

class DetalleTransferenciaInlineTransfSalSarmiento(admin.TabularInline):
     model = DetalleTransfSalSarmiento
     raw_id_fields = ('idarticulo',)

class TransfSalSarmiento(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfSalSarmiento]
     list_display = ('fechasalida','depositoentrada','confirmado')
     list_filter = ('depositoentrada','depositosalida')
     search_fields = ('fechasalida','depositoentrada__direccion')     
     readonly_fields=( 'confirmado',)

#ENTRADA-SARMIENTO

class DetalleTransferenciaInlineTransfEntSarmiento(admin.TabularInline):
     model = DetalleTransfEntSarmiento
     readonly_fields = ('cantidad','confirmado','idarticulo',) 
 
class TransfEntSarmiento(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfEntSarmiento]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)     
     readonly_fields=( 'confirmado',)

#SALIDA-ESQUEL

class DetalleTransferenciaInlineTransfSalEsquel(admin.TabularInline):
     model = DetalleTransfSalEsquel
     raw_id_fields = ('idarticulo',)

class TransfSalEsquel(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfSalEsquel]
     list_display = ('fechasalida','depositoentrada','confirmado')
     list_filter = ('depositoentrada',)
     search_fields = ('fechasalida','depositoentrada__direccion')     
     readonly_fields=( 'confirmado',)
#     if VwTransfSalEsquel.confirmado:
 #        readonly_fields=( 'confirmado','fechasalida',)

#ENTRADA-ESQUEL

class DetalleTransferenciaInlineTransfEntEsquel(admin.TabularInline):
     model = DetalleTransfEntEsquel
     readonly_fields = ('cantidad','confirmado','idarticulo',)  

class TransfEntEsquel(admin.ModelAdmin):
     inlines = [DetalleTransferenciaInlineTransfEntEsquel]
     list_display = ('fechaentrada','fechasalida','confirmado','depositoentrada','depositosalida',)
     list_filter = ('confirmado','depositoentrada','depositosalida')
     search_fields = ('fechaentrada','fechasalida',)     
     readonly_fields=( 'confirmado',)     


#---------------------------------------------------------------------------------------------------------------------------------------------------
#==LOG==============================================================================================================================================
#---------------------------------------------------------------------------------------------------------------------------------------------------

class LogAdmin(admin.ModelAdmin):
     list_display = ('user','action_time','content_type','object_id','object_repr','action_flag','change_message',)
     list_filter = ('user',)
     ordering = ['-action_time']
     readonly_fields = ('id','user','action_time','content_type','object_id','object_repr','action_flag','change_message',)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(VwArticulos,VwArticulosAdmin)
admin.site.register(Barras)
admin.site.register(Cuentaspatrimoniales,CuentaspatrimonialesAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Deposito, DepositoAdmin)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(Salida, SalidaAdmin)
admin.site.register(VwSalidaesquel, SalidaAdminEsquel)
admin.site.register(VwSalidamadryn, SalidaAdminMadryn)
admin.site.register(VwSalidasarmiento, SalidaAdminSarmiento)
admin.site.register(VwSalidarw, SalidaAdminRw)
admin.site.register(VwSalidagaiman, SalidaAdminGaiman)
#admin.site.register(Detallesalida)
admin.site.register(Transferencia, TransferenciaAdmin)
#admin.site.register(Detalletrasferencia)
admin.site.register(Proveedor,ProveedorAdmin)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#admin.site.register(Detallecompra, DetallecompraAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(VwComprasrw, CompraAdminrw)
admin.site.register(VwComprassarmiento, CompraAdminsarmiento)
admin.site.register(VwCompraspmadryn, CompraAdminpmadryn)
admin.site.register(VwComprasesquel, CompraAdminesquel)
admin.site.register(VwComprasgaiman, CompraAdmingaiman)
admin.site.register(Devoluciones, DevolucionesAdmin)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(Devolucionrw, DevolucionesRawsonAdmin)
admin.site.register(Devoluciongaiman, DevolucionesGaimanAdmin)
admin.site.register(Devolucionesquel, DevolucionesEsquelAdmin)
admin.site.register(Devolucionsarmiento, DevolucionesSarmientoAdmin)
admin.site.register(Devolucionmadryn, DevolucionesMadrynAdmin)
#admin.site.register(Detalledevolucion)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(VwTransfEntRw, TransfEntRw)
admin.site.register(VwTransfSalRw, TransfSalRw)
admin.site.register(VwTransfEntMadryn, TransfEntMadryn)
admin.site.register(VwTransfSalMadryn, TransfSalMadryn)
admin.site.register(VwTransfEntGaiman, TransfEntGaiman)
admin.site.register(VwTransfSalGaiman, TransfSalGaiman)
admin.site.register(VwTransfEntSarmiento, TransfEntSarmiento)
admin.site.register(VwTransfSalSarmiento, TransfSalSarmiento)
admin.site.register(VwTransfEntEsquel, TransfEntEsquel)
admin.site.register(VwTransfSalEsquel, TransfSalEsquel)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(Articulodeposito,ArticulodepositoAdmin)
#admin.site.register(ArticuloDepositoAd, vwdepositoAdAdmin)
admin.site.register(ArticuloDepositoRawson, vwdepositorawsonAdmin)
admin.site.register(ArticuloDepositoMadryn, vwdepositomadrynAdmin)
admin.site.register(ArticuloDepositoEsquel, vwdepositoesquelAdmin)
admin.site.register(ArticuloDepositoSarmiento, vwdepositosarmientoAdmin)
admin.site.register(ArticuloDepositoGaiman, vwdepositogaimanAdmin)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
admin.site.register(Log,LogAdmin)

#admin.site.register(DjangoSession)
