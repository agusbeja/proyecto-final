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
from django.conf import settings
from django.conf.urls.static import static
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
                            
from tenis_de_mesa.views import (index, PostDetalle, PostListar, PostCrear,
                                 PostBorrar, PostActualizar, UserSignUp,
                                  UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle)


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

    path('tenis-de-mesa/', index, name="tenis-de-mesa-index"),
    path('tenis-de-mesa/<int:pk>/detalle/', PostDetalle.as_view(), name="tenis-de-mesa-detalle"),
    path('tenis-de-mesa/listar/', PostListar.as_view(), name="tenis-de-mesa-listar"),
    path('tenis-de-mesa/crear/', PostCrear.as_view(), name="tenis-de-mesa-crear"),
    path('tenis-de-mesa/<int:pk>/borrar/', PostBorrar.as_view(), name="tenis-de-mesa-borrar"),
    path('tenis-de-mesa/<int:pk>/actualizar/', PostActualizar.as_view(), name="tenis-de-mesa-actualizar"),
    path('tenis-de-mesa/signup/', UserSignUp.as_view(), name="tenis-de-mesa-signup"),
    path('tenis-de-mesa/login/', UserLogin.as_view(), name="tenis-de-mesa-login"),
    path('tenis-de-mesa/logout/', UserLogout.as_view(), name="tenis-de-mesa-logout"),
    path('tenis-de-mesa/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="tenis-de-mesa-avatars-actualizar"),
    path('tenis-de-mesa/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="tenis-de-mesa-users-actualizar"),
    path('tenis-de-mesa/mensajes/crear/', MensajeCrear.as_view(), name="tenis-de-mesa-mensajes-crear"),
    path('tenis-de-mesa/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="tenis-de-mesa-mensajes-detalle"),
    path('tenis-de-mesa/mensajes/listar/', MensajeListar.as_view(), name="tenis-de-mesa-mensajes-listar"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
