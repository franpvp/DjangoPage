from django.urls import path
from core import admin
from .views import menu, login, registrarse, animales, armas, construcciones, consumibles, enemigos, flora, forowiki,historia, logros,lugarestf,micuentatf,recuperarcontra
from . import views

urlpatterns = [
    path('', views.menu, name="home"),
    path('menuprincipal_wiki.html', views.menu, name="menu"),
    path('inicio_sesion_wiki.html', views.login, name="login"),
    path('registrase_wiki.html', views.registrarse, name="registro"),
    path('Animales.html', views.animales, name="animales"),
    path('Armas.html', views.armas, name="armas"),
    path('Construcciones.html', views.construcciones, name="construcciones"),
    path('Consumibles.html', views.consumibles, name="consumibles"),
    path('Enemigos.html', views.enemigos, name="enemigos"),
    path('Flora.html', views.flora, name="flora"),
    path('forowiki.html', views.forowiki, name="forowiki"),
    path('historia.html', views.historia, name="historia"),
    path('Logros.html', views.logros, name="logros"),
    path('Lugarestf.html', views.lugarestf, name="lugarestf"),
    path('micuentatf.html', views.micuentatf, name="micuentatf"),
    path('recuperarcontra.html', views.recuperarcontra, name="recuperarcontra")
]
