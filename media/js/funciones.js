var numeros="0123456789";
var letras="abcdefghyjklmnñopqrstuvwxyz";
var simbolos="¬|@·~½¬{[]}\¸°!#$%&/()=?¡¿'+-.,;:_<>*";
//--------------------------------------------------------------------------------------------------------------
//Evalua una cadena para ver si contiene caracteres numericos, en caso de tenerlos retorna 1, caso contrario 0
function tiene_numeros(texto){
	for(i=0; i<texto.length; i++){
		if (numeros.indexOf(texto.charAt(i),0)!=-1){
			return 1;
		}
	}
	return 0;
} 

//--------------------------------------------------------------------------------------------------------------
function tiene_no_valido(texto){
	texto = texto.toLowerCase();
	for(i=0; i<texto.length; i++){
		if (letras.indexOf(texto.charAt(i),0)!=-1 || simbolos.indexOf(texto.charAt(i),0)!=-1){
			return 1;
		}
	}
	return 0;
}

//--------------------------------------------------------------------------------------------------------------
function acopla(texto, campo){
	var n = texto.concat(".",campo);
	return n;	
}


//--------------------------------------------------------------------------------------------------------------
/***
Recibe el mes que parseo validarFecha, y devuelve la cantidad de dias que trae el mes, caso erroneo retorna -1
***/
function validarMes(mes,anio){
	var dmax = -1;
	switch (mes){
		case 1:
			dmax=31;
			break;
		case 2:
			if (anio % 4 == 0) 
				dmax = 29; 
			else 
				dmax = 28;
			break;
		case 3:
			dmax = 31;
			break; 
		case 4:
			dmax = 30;
			break; 
		case 5:
			dmax = 31;
			break; 
		case 6:
			dmax = 30;
			break; 
		case 7:
			dmax = 31;
			break; 
		case 8:
			dmax = 31;
			break; 
		case 9:
			dmax = 30;
			break; 
		case 10:
			dmax = 31;
			break; 
		case 11:
			dmax = 30;
			break; 
		case 12:
			dmax = 31;
			break;
	}
	return dmax;
}

//--------------------------------------------------------------------------------------------------------------
/***
//Determina si la fecha en su totalidad es correcta o erronea, en caso de error indica en donde se encuentran el o los mismos
***/
function validarFecha(anio,mes,dia){
	var estado = -1;
	if (tiene_no_valido(anio) == 0){
	    var dmax = validarMes(parseInt(mes),parseInt(anio));
	    if (dmax != -1){
		if (parseInt(dia)>=1 || parseInt(dia)<= dmax){
		    estado = 1;
		}
		else{
		    alert("Error en la entrada de dia");
		}
	    }
	    else{
		alert("Error en la entrada de mes");
	    }
	}
	else{
	  alert("Error en la entrada de AÑO");
	}
	return estado;
}

//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function reporteAus(){
	//if (validarFecha(escape(anio.value),escape(mes.value),escape(dia.value)) == 1){
	if (validarFecha($F('anio'), $F('mes'),$F('dia')) == 1){
	    alert("Fecha OK");
	}
	else{
	    alert("Ingrese una fecha correcta!");
	}
	//var url="http://172.155.0.6:7000/ausentismos/"+escape(anio.value)+"/"+escape(mes.value)+"/"+escape(dia.value);
//	var url="http://172.155.0.6:7000/ausentismos/"+$F('anio')+"/"+$F('mes')+"/"+$F('dia');
	var url="http://172.155.0.9:7000/reporteausentismos/"+$F('anio')+"/"+$F('mes')+"/"+$F('dia');
	open(url,"_self");
	return false;
}

//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function llamaPdf(){
	//if (validarFecha(escape(anio.value),escape(mes.value),escape(dia.value)) == 1){
	if (validarFecha($F('anio'), $F('mes'),$F('dia')) == 1){
	    alert("Fecha OK");
	}
	else{
	    alert("Ingrese una fecha correcta!");
	}
	//var url="http://172.155.0.6:7000/ausentismos/"+escape(anio.value)+"/"+escape(mes.value)+"/"+escape(dia.value);
	var url="http://172.155.0.9:7000/ausentismos/"+$F('anio')+"/"+$F('mes')+"/"+$F('dia');

	open(url,"_self");
	return false;
}

//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function infoAgente(nroDoc){
    //parseInt('') 
    var url="http://172.155.0.9:7000/agente/"+nroDoc;
    open(url,"_self");
    return false;
}
//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function listaAgentesAll(){
	var url="http://172.155.0.9:7000/agentesAll/";
	open(url,"_self");
	return false;
}
//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function buscaAgentes(){
	var url="http://172.155.0.9:7000/agentesBusc/"+$F('apellido');
	open(url,"_self");
	return false;
}
//--------------------------------------------------------------------------------------------------------------
/***
/
***/
function fliaAgente(nroDoc){
    //parseInt('') 
    var url="http://172.155.0.9:7000/familiares/"+nroDoc;
    open(url,"_self");
    return false;
}

//-------------------------------------------------------------------------------------------
function generarPdf(){
    
    var url = document.location.href; 
    partes = url.split('/');
    
    p1=partes[partes.length-2];	//numero compra
    p2=partes[partes.length-3];
    p3=partes[partes.length-4];
    p4=partes[partes.length-5];
    p5=partes[partes.length-6];
    
    //alert("p1:"+p1);
    
        
    if (p1== "add"){
	alert("Presione Guardar y Continuar Editando - Para poder generar el Pdf -");
	return false;
    }else{
      
	url= p5+"/"+p4+"/"+p3+"/"+p2;
		
	// COMPRAS ********************************************************
	if ((p2== "compra") || (p2== "vwcomprasesquel") || (p2== "vwcomprasgaiman") ||
	(p2== "vwcompraspmadryn") || (p2== "vwcomprassarmiento") || (p2== "vwcomprasrw")){
	    alert("entre a compras");
	    var destino="http://deponew.django/pdfcompra/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// ARTICULOS ********************************************************
	if ((p2== "articulo") || (p2== "vwarticulos")){
	  
	    var destino="http://deponew.django/pdfarticulo/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// ARTICULOS  Deposito********************************************************
	if (p2== "articulodepositoad") {
	    var destino="http://deponew.django/pdfarticulodepositoad/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// ARTICULOS  Deposito CIUDADES*******************************************************
	
	if (p2== "articulodepositoesquel"){
	    aux = 3; 
	    var destino="http://deponew.django/pdfarticulodeposito/"+p1+"/"+aux;
	    open(destino,"_self");
	    return false;
	} 
	  
	  
	if (p2== "articulodepositogaiman"){
	    aux = 4;
	    var destino="http://deponew.django/pdfarticulodeposito/"+p1+"/"+aux;
	    open(destino,"_self");
	    return false;
	} 
	  
	  	  
	if (p2== "articulodepositomadryn"){
	    aux = 2;
	    var destino="http://deponew.django/pdfarticulodeposito/"+p1+"/"+aux;
	    open(destino,"_self");
	    return false;
	} 
	  
	if (p2== "articulodepositorawson"){
	    aux = 5;
	    var destino="http://deponew.django/pdfarticulodeposito/"+p1+"/"+aux;
	    open(destino,"_self");
	    return false;
	} 
	  
	  
	if (p2== "articulodepositosarmiento"){
	    aux = 1;
	    var destino="http://deponew.django/pdfarticulodeposito/"+p1+"/"+aux;
	    open(destino,"_self");
	    return false;
	}
	
	
	// BARRAS ********************************************************
	if (p2== "barras"){
	  
	    var destino="http://deponew.django/pdfbarra/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// CIUDAD ********************************************************
	if (p2== "ciudad"){
	   
	    var destino="http://deponew.django/pdfciudad/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// COMPRAS ********************************************************
	if ((p2== "compra") || (p2== "vwcomprasesquel") || (p2== "vwcompraspmadryn") ||
	(p2== "vwcomprassarmiento") || (p2== "vwcomprasrw") || (p2== "vwcomprasgaiman")){
	  
	    var destino="http://deponew.django/pdfcompra/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// CUENTAS PATRIMONIALES ********************************************************
	if (p2== "cuentaspatrimoniales"){
	  
	    var destino="http://deponew.django/pdfctapatrimonial/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// DEPOSITO ********************************************************
	if (p2== "deposito"){
	  
	    var destino="http://deponew.django/pdfdeposito/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// DETALLE COMPRA ********************************************************
	if (p2== "detallecompra"){
	  	  
	    var destino="http://deponew.django/pdfdetallecompra/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// DEVOLUCIONES ********************************************************
	if ((p2== "devoluciones") || (p2== "devolucionesquel") || (p2== "devoluciongaiman") || (p2== "devolucionmadryn") ||
	(p2== "devolucionrw") || (p2== "devolucionsarmiento")){
	  	  
	    var destino="http://deponew.django/pdfdevoluciones/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// LOGS ********************************************************
	if (p2== "log"){
	  	  
	    var destino="http://deponew.django/pdflog/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// PROVEEDOR ********************************************************
	if (p2== "proveedor"){
	  	  
	    var destino="http://deponew.django/pdfproveedor/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// SALIDA ********************************************************
	if ((p2== "salida") || (p2== "vwsalidaesquel") || (p2== "vwsalidagaiman") || (p2== "vwsalidamadryn") || 
	(p2== "vwsalidarw") || (p2== "vwsalidasarmiento")){
	  	  
	    var destino="http://deponew.django/pdfsalida/"+p1;
	    open(destino,"_self");
	    return false;
	}
	
	// TRANSFERENCIA ********************************************************
	if ((p2== "transferencia") || (p2== "vwtransfentrw") || (p2== "vwtransfentesquel") || (p2== "vwtransfentgaiman") || (p2== "vwtransfentmadryn") || (p2== "vwtransfentsarmiento")
	|| (p2== "vwtransfsalesquel") || (p2== "vwtransfsalgaiman") || (p2== "vwtransfsalmadryn") || (p2== "vwtransfsalrw") || (p2== "vwtransfsalsarmiento")){
	  	  
	    var destino="http://deponew.django/pdftransferencia/"+p1;
	    open(destino,"_self");
	    return false;
	}
	alert("Sin Funcionalidad");
	return false;
    }  
}
