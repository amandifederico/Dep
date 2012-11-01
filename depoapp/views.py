# -*- coding: utf-8 -*-

#IMPORTS PARA PDF
#====================================================
#pisa requiere ReportLab Toolkit, HTML5lib, pyPdf y PIL para instalarlos:
#sudo apt-get install python-html5lib
#sudo apt-get install python-pypdf
#sudo apt-get install python-reportlab
#sudo apt-get install python-imagin

import ho.pisa as pisa #esto hay que bajarlo de internet, se puede instalar con easy install - http://pypi.python.org/pypi/pisa/
import cStringIO as StringIO
import cgi
from django.template import RequestContext, Template, Context
from django.template.loader import *
from django.http import HttpResponse
from datetime import *
#from reportlab.pdfgen import canvas
#====================================================
from depoapp.models import *
import psycopg2
from django.shortcuts import render_to_response
#===================================================
from django import http
from django.core.context_processors import csrf #para formularios
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
#from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required


#==========================================================================================================
def conexion():
        """
        Realiza la conexion a la base de datos y devuelve el cursor correspondiente
        """
        conec = "host='172.155.0.8'  dbname='deposito' user='postgres' password='sistemasavp'"
        cnx = psycopg2.connect(conec)
        cursor = cnx.cursor()
        return cursor

#==========================================================================================================
def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    
    pisa.CreatePDF(html,result)
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    response = HttpResponse(result.getvalue(), mimetype ='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=prueba.pdf'
    return response
    #if not pdf.err:
    #   return HttpResponse(result.getvalue(), mimetype ='application/pdf')
    #return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


@csrf_exempt
@login_required
def listado(peticion,Nmodelo):
    """
    Vista que retorno el template index.html
    """
    c={}
    c.update(csrf(peticion))
    modelo = models.get_model('depoapp',Nmodelo)
    campos = modelo._meta.fields
    listCampos = list()
    for a in campos:
        listCampos.append(a.name)
    lista = list(modelo.objects.all())    
    user = peticion.user

    return render_to_response('listado.html',{'lista':lista,'user':user,'campos':listCampos,'modelo':Nmodelo,},)
    
@csrf_exempt
@login_required
def listPdf(peticion,Nmodelo):
    """
    Vista que retorno el template index.html
    """
    c={}
    c.update(csrf(peticion))
    modelo = models.get_model('depoapp',Nmodelo)
    campos = modelo._meta.fields
    listCampos = list()
    for a in campos:
        listCampos.append(a.name)
    lista = list(modelo.objects.all())    
    user = peticion.user

    return generar_pdf(render_to_response('listPdf.html',{'lista':lista,'user':user,'campos':listCampos,'modelo':Nmodelo,},))


def listaCompra(peticion):

    c={}
    c.update(csrf(peticion))
    start_date = date(2005, 1, 1)
    end_date = date(2012, 10, 26)
    listacompra = list(Compra.objects.filter(fecha__range=(start_date, end_date)))    
    listadcompra = []
    for a in listacompra:
	listadcompraaux = list(Detallecompra.objects.filter(idcompra__exact=a.idcompra))
	if len(listadcompra) == 0:
		for b in listadcompraaux:
			listadcompra.append(b)
	else:	
		for b in listadcompraaux:
			w = 0
			for c in listadcompra:
				if c.idarticulo == b.idarticulo:
					c.cantidad += b.cantidad
					w = 1				
			if w == 0:
				listadcompra.append(b)
	
	
		
		
    user = peticion.user

    return render_to_response('listacompra.html',{'lista':listadcompra,'user':user,},)

def listaSalida(peticion):

    c={}
    c.update(csrf(peticion))
    start_date = date(2005, 1, 1)
    end_date = date(2012, 10, 26)
    listasalida = list(Salida.objects.filter(fecha__range=(start_date, end_date)).filter(iddeposito__exact=3))   
    listadsalida = []
    for a in listasalida:
	listadsalidaaux = list(Detallesalida.objects.filter(idsalida__exact=a.idsalida))
	if len(listadsalida) == 0:
		for b in listadsalidaaux:
			listadsalida.append(b)
	else:	
		for b in listadsalidaaux:
			w = 0
			for c in listadsalida:
				if c.idarticulo == b.idarticulo:
					c.cantidad += b.cantidad
					w = 1				
			if w == 0:
				listadsalida.append(b)
	
	
		
		
    user = peticion.user

    return render_to_response('listasalida.html',{'lista':listadsalida,'user':user,},)

def listaTransf(peticion):

    c={}
    c.update(csrf(peticion))
    start_date = date(2005, 1, 1)
    end_date = date(2012, 10, 31)
    listatransf = list(Transferencia.objects.filter(fechaentrada__range=(start_date, end_date)))    
    listadtransf = []
    lista2dtransf = []
    for a in listatransf:
	listadtransfaux = list(Detalletrasferencia.objects.filter(idtransferencia__exact=a.idtransferencia))
	if len(listadtransf) == 0:
		for b in listadtransfaux:
			listadtransf.append(b)
	else:	
		for b in listadtransfaux:
			w = 0
			for c in listadtransf:
				if c.idarticulo == b.idarticulo:
					c.cantidadconfirmada += b.cantidadconfirmada
					c.cantidad += b.cantidad
					w = 1				
			if w == 0:
				listadtransf.append(b)
				lista2dtransf.append([b,a.depositoentrada,a.depositosalida])
	
	
		
		
    user = peticion.user

    return render_to_response('listatransf.html',{'lista':listadtransf,'lista2':lista2dtransf,'user':user,},)








