# -*- coding: utf-8 -*-

#IMPORTS PARA PDF
#====================================================
#pisa requiere ReportLab Toolkit, HTML5lib, pyPdf y PIL para instalarlos:
#sudo apt-get install python-html5lib
#sudo apt-get install python-pypdf
#sudo apt-get install python-reportlab
#sudo apt-get install python-imagin

#import ho.pisa as pisa #esto hay que bajarlo de internet, se puede instalar con easy install - http://pypi.python.org/pypi/pisa/
import cStringIO as StringIO
import cgi
from django.template import RequestContext, Template, Context
from django.template.loader import *
from django.http import HttpResponse
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
def listado(peticion):
    """
    Vista que retorno el template index.html
    """
    c={}
    c.update(csrf(peticion))
    #cursor = conexion()
    #lista = cursor.execute('SELECT * FROM proveedor')
    lista = list(Proveedor.objects.all())
    user = peticion.user
    return render_to_response('listado.html',{'lista':lista,'user':user,},)
