from re import template
from django.shortcuts import redirect, render, HttpResponse #importo HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from miApp.models import Curso


# Create your views here.
# DIFERENCIAS:
# MODELO  VISTA    CONTROLADOR = MVC
# MODELO  TEMPLATE VISTA       = MVT        (EN DJANGO LA VISTA HACE EL PAPEL DE CONTROLADOR Y EL TEMPLATE ES REALMENTE LA VISTA)


#----------MEJOR HACER LAS VIEWS CON CLASES!!!!!!!!!!!!!
class pruebaView (TemplateView):
    template_name="hola_mundo.html"


#----------FORMA DEL CURSO.... PERO FRANCISCO ME RECOMIENDA USAR LAS CLASES.... PARA ALGUNOS
def holaMundo(request): #Para ver que esta vista funciona hay que cargarla en una URL (urls.py)
    return render(request, "hola_mundo.html") 




def index (request): 

  
    return render(request, "index.html", {                                                  #El tercer parámetro son variables que se pasan a la template desde la vista (controlador)
        "mi_variable": "Esto es el valor de una variable",
        "titulo": "Inicio",
        "indice":0
    })
    
"""
def curso(self):

      curso = Curso(nombre = "Desarrollo web", camada = "19881")
      curso.save()
      documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
      return HttpResponse(documentoDeTexto)
"""

    
def hora(request):
    now = datetime.now()
    
    return render(request, "hora.html", {
        "titulo": "Menu de la hora",
        "hora": now
        
    })

def contacto (request, nombre="Sergio Cañete Linares", email="email@email.es", telefono="666 666 666"):
    curso = Curso(nombre = "Desarrollo web", camada=12) 
    return render(request, "contacto.html",{
        "nombre": nombre,   #EL NOMBRE DE LAS VARIABLES QUE PASAN AL HTML VAN ENTRE COMILLAS "NOMBRE"
        "telefono": telefono,
        "email": email,
        "nombreC": curso.nombre,
        "camadaC": curso.camada
    })



def pagina (request, redir=0):
    if redir == 1:
        return redirect("https://www.google.es/")
    elif redir ==2:
        return redirect("contacto", nombre="JESU", apellido="CRISTO")
                        #SI HAGO LA REDIRECCION POR EL NAME="contacto" EN VEZ DE POR LA URL, PUEDO MODIFICAR LA URL SIN PROBLEMA!!!

    return render(request, "pagina.html")