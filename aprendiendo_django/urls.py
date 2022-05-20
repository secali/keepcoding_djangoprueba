"""aprendiendo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#importo miapp con mis vistas
import miApp.views as miAppV

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hora/", miAppV.hora),
    path("", miAppV.index, name="index"),
    path("inicio/", miAppV.index, name="index"),
    #path('hola-mundo/', miAppV.holaMundo, name='hola_mundo'),
    #a path('hola-mundo2/', miAppV.pruebaView.as_view(), name='hola_mundo_clase'),
    path('contacto/<str:nombre>/<str:email>/<str:telefono>', miAppV.contacto, name='contacto'),  #<str:nombre> indica que voy a pasar un parametro por url de tipo str
    path('contacto/<str:nombre>', miAppV.contacto, name='contacto'),                 #Para controlar si me pasan nombre, nombre y apellido o nada
    path('contacto/', miAppV.contacto, name='contacto'),                        
    path("pagina/", miAppV.pagina, name="pagina"),
    path("pagina/<int:redir>", miAppV.pagina, name="pagina") #Parece que al parametro que se le pasa, debe llamarse igual que en el views.py, si no da error
    
]
