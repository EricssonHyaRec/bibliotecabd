import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Libros, Autores, Generos
import json
from django.db import connection
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Verifica el captcha
        captcha_token = request.POST.get('h-captcha-response')
        captcha_data = {
            'secret': '0x0000000000000000000000000000000000000000',
            'response': captcha_token
        }
        captcha_verification = requests.post('https://hcaptcha.com/siteverify', data=captcha_data)
        captcha_result = captcha_verification.json()
        
        if not captcha_result.get('success'):
            messages.error(request, 'Error en el captcha. Por favor, inténtalo de nuevo.')
            return render(request, 'login.html')
        
        # Verificación de usuario y contraseña
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página principal de la biblioteca
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['new_username']
        email = request.POST['new_email']
        password = request.POST['new_password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registro exitoso. Ya puedes iniciar sesión.')
            return redirect('login')
    
    return render(request, 'login.html')

def registro_personal_view(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        usuario = request.POST['usuario']
        dni = request.POST['dni']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        
        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            # Crear el usuario
            user = User.objects.create_user(username=usuario, email=correo, password=contraseña)
            user.first_name = nombres
            user.last_name = apellidos
            user.save()
            
            messages.success(request, 'Usuario registrado exitosamente. Ahora puedes iniciar sesión.')
            return redirect('registro_personal')  # Redirige a la página de inicio de sesión

    return render(request, 'registro_personal.html')

def inicio_view(request):
    return render(request, 'inicio.html')


def agregar_libro_view(request):
    autores = Autores.objects.all()
    generos = Generos.objects.all()

    if request.method == 'POST':
        titulo = request.POST['titulo']
        id_autor = request.POST['id_autor']
        editorial = request.POST['editorial']
        anio_publicacion = request.POST['anio_publicacion']
        id_genero = request.POST['id_genero']
        cantidad_disponible = request.POST['cantidad_disponible']
        
        autor = Autores.objects.get(id_autor=id_autor)
        genero = Generos.objects.get(id_genero=id_genero)

        libro = Libros.objects.create(
            titulo=titulo,
            id_autor=autor,
            editorial=editorial,
            anio_publicacion=anio_publicacion,
            id_genero=genero,
            cantidad_disponible=cantidad_disponible
        )

        libro.save()
        messages.success(request, 'Libro añadido exitosamente.')
        return redirect('lista_libros')  # Asegúrate de que la URL sea correcta

    return render(request, 'lista_libros.html', {'autores': autores, 'generos': generos})


def lista_libros_view(request):
    libros = Libros.objects.all()  # Traer todos los libros
    autores = Autores.objects.all()  # Traer todos los autores
    generos = Generos.objects.all()  # Traer todos los géneros
    
    return render(request, 'lista_libros.html', {
        'libros': libros,
        'autores': autores,
        'generos': generos
    })

def lista_autores_view(request):
    libros = Libros.objects.all()  # Traer todos los libros
    autores = Autores.objects.all()  # Traer todos los autores
    generos = Generos.objects.all()  # Traer todos los géneros
    
    return render(request, 'lista_autores.html', {
        'libros': libros,
        'autores': autores,
        'generos': generos
    })

def agregar_autor_view(request):
    if request.method == 'POST':
        nombre_autor = request.POST.get('nombre_autor')
        if nombre_autor:  # Validación simple
            Autores.objects.create(nombre_autor=nombre_autor)
            return redirect('lista_libros')  # Redirige a la lista de libros u otra página
    return redirect('lista_libros')  # En caso de que no sea POST

def editar_autor_view(request, id_autor):
    autor = get_object_or_404(Autores, id_autor=id_autor)

    if request.method == 'POST':
        autor.nombre_autor = request.POST.get('nombre_autor')
        autor.save()
        return redirect('lista_autores')  # Redirigir a la lista de géneros

    return render(request, 'lista_autores.html', {'autor': autor})

def eliminar_autor_view(request, id_autor):
    autor = get_object_or_404(Autores, id_autor=id_autor)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')  # Redirige a la lista de libros después de eliminar
    return redirect('lista_autores')  # En caso de que no sea POST

def agregar_genero_view(request):
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')
        if nombre_categoria:  # Validación simple
            Generos.objects.create(nombre_categoria=nombre_categoria)
            return redirect('lista_libros')  # Redirige a la lista de libros u otra página
    return redirect('lista_libros')  # En caso de que no sea POST

def activar_desactivar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categorias, id_categoria=id_categoria)
    
    # Cambiar el estado de la categoría
    if categoria.estado == 'activo':
        categoria.estado = 'inactivo'
        messages.success(request, 'Categoría desactivada exitosamente.')
    else:
        categoria.estado = 'activo'
        messages.success(request, 'Categoría activada exitosamente.')

    categoria.save()
    return redirect('lista_categorias')

def activar_desactivar_producto(request, id_producto):
    productos = get_object_or_404(Productos, id_producto=id_producto)
    
    # Cambiar el estado de la categoría
    if productos.estado == 'activo':
        productos.estado = 'inactivo'
        messages.success(request, 'producto desactivada exitosamente.')
    else:
        productos.estado = 'activo'
        messages.success(request, 'producto activada exitosamente.')

    productos.save()
    return redirect('CatalogoProducto')


def editar_libro_view(request, id_libro):
    libro = get_object_or_404(Libros, id_libro=id_libro)
    
    if request.method == 'POST':
        # Obtener datos del formulario
        libro.titulo = request.POST.get('titulo')
        
        # Obtener la instancia del autor usando el ID proporcionado
        autor_id = request.POST.get('id_autor')
        if autor_id:
            libro.id_autor = get_object_or_404(Autores, id_autor=autor_id)
        
        libro.editorial = request.POST.get('editorial')
        libro.anio_publicacion = request.POST.get('anio_publicacion')
        
        # Obtener la instancia del género
        genero_id = request.POST.get('id_genero')
        if genero_id:
            libro.id_genero = get_object_or_404(Generos, id_genero=genero_id)
        
        libro.cantidad_disponible = request.POST.get('cantidad_disponible')
        
        # Guardar los cambios
        libro.save()
        return redirect('lista_libros')  # Redirigir a la lista de libros

    # Obtener listas de autores y géneros para el formulario
    autores = Autores.objects.all()
    generos = Generos.objects.all()

    return render(request, 'editar_libro.html', {
        'libro': libro,
        'autores': autores,
        'generos': generos
    })

def eliminar_libro_view(request, id_libro):
    libro = get_object_or_404(Libros, id_libro=id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')  # Redirige a la lista de libros después de eliminar
    return redirect('lista_libros')  # En caso de que no sea POST

def lista_generos_view(request):
    generos = Generos.objects.all()  # Obtener todos los géneros
    return render(request, 'lista_generos.html', {'generos': generos})

def editar_genero_view(request, id_genero):
    genero = get_object_or_404(Generos, id_genero=id_genero)

    if request.method == 'POST':
        genero.nombre_categoria = request.POST.get('nombre_categoria')
        genero.save()
        return redirect('lista_generos')  # Redirigir a la lista de géneros

    return render(request, 'editar_genero.html', {'genero': genero})

# Vista para eliminar un género
def eliminar_genero_view(request, id_genero):
    genero = get_object_or_404(Generos, id_genero=id_genero)
    genero.delete()
    return redirect('lista_generos')  # Redirigir a la lista de géneros