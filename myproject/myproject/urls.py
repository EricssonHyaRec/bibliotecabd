"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('lista_libros/', views.lista_libros_view, name='lista_libros'),
    path('registro_personal/', views.registro_personal_view, name='registro_personal'),
    path('agregar_libro/', views.agregar_libro_view, name='agregar_libro'),
    path('lista_autores/', views.lista_autores_view, name='lista_autores'),
    path('agregar_autor/', views.agregar_autor_view, name='agregar_autor'),
    path('editar_autor/<int:id_autor>/', views.editar_autor_view, name='editar_autor'),
    path('eliminar_autor/<int:id_autor>/', views.eliminar_autor_view, name='eliminar_autor'),
    path('agregar_genero/', views.agregar_genero_view, name='agregar_genero'),
    path('eliminar_libro/<int:id_libro>/', views.eliminar_libro_view, name='eliminar_libro'),
    path('editar_libro/<int:id_libro>/', views.editar_libro_view, name='editar_libro'),
    path('lista_generos/', views.lista_generos_view, name='lista_generos'),
    path('eliminar_genero/<int:id_genero>/', views.eliminar_genero_view, name='eliminar_genero'),
    path('editar_genero/<int:id_genero>/', views.editar_genero_view, name='editar_genero'),


    path('activar_desactivar_categoria/<int:id_categoria>/', views.activar_desactivar_categoria, name='activar_desactivar_categoria'),
    path('activar_desactivar_producto/<int:id_producto>/', views.activar_desactivar_producto, name='activar_desactivar_producto'),
]
