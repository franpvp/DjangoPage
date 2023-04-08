from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

# Menú principal Página
def menu(request):
    return render(request, 'core/menuprincipal_wiki.html',{})
# Inicio Sesión
def login(request):
    return render(request, 'core/inicio_sesion_wiki.html',{})
# Registro
def registrarse(request):
    return render(request, 'core/registrase_wiki.html',{})
# Animales
def animales(request):
    return render(request, 'core/Animales.html',{})
# Armas
def armas(request):
    return render(request, 'core/Armas.html',{})
#Construcciones
def construcciones(request):
    return render(request, 'core/Construcciones.html',{})
# Consumibles
def consumibles(request):
    return render(request, 'core/Consumibles.html',{})
# Enemigos
def enemigos(request):
    return render(request, 'core/Enemigos.html',{})
# Flora
def flora(request):
    return render(request, 'core/Flora.html',{})
# Forowiki
def forowiki(request):
    return render(request, 'core/forowiki.html',{})
# Historia
def historia(request):
    return render(request, 'core/historia.html',{})
# Logros
def logros(request):
    return render(request, 'core/Logros.html',{})
# Lugarestf
def lugarestf(request):
    return render(request, 'core/Lugarestf.html',{})
# Mi Cuentatf
def micuentatf(request):
    return render(request, 'core/micuentatf.html',{})
# Recuperar Contraseña
def recuperarcontra(request):
    return render(request, 'core/recuperarcontra.html',{})

