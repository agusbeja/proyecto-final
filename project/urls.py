"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (index, saludar_a, sumar, monstrar_familiares,
                             buscar, BuscarFamiliar, AltaFamiliar,
                              ActualizarFamiliar, BorrarFamiliar, 
                              FamiliarList, FamiliarCrear, FamiliarBorrar,
                              FamiliarActualizar,

                               mostrar_mascotas, BuscarMascota, AltaMascota,
                               ActualizarMascota, BorrarMascota,
                               
                               mostrar_autos, BuscarAuto, AltaAuto,
                                ActualizarAuto, BorrarAuto)
                            
from ejemplo_dos.views import index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('mi-familia/', monstrar_familiares),
    path('buscar/', buscar),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),



    path('mis-mascotas/', mostrar_mascotas),
    path('mis-mascotas/buscar-mascotas', BuscarMascota.as_view()),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    

    path('mis-autos/', mostrar_autos),
    path('mis-autos/buscar-auto', BuscarAuto.as_view()),
    path('mis-autos/alta', AltaAuto.as_view()),
    path('mis-autos/actualizar/<int:pk>', ActualizarAuto.as_view()),
    path('mis-autos/borrar/<int:pk>', BorrarAuto.as_view()),

    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', PostBorrar.as_view(), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', PostActualizar.as_view(), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/signup/', UserSignUp.as_view(), name="ejemplo-dos-signup"),
    path('ejemplo-dos/login/', UserLogin.as_view(), name="ejemplo-dos-login"),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),


]

