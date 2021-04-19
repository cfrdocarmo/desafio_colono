"""djangoColonoV1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuarioViewSets
from atividades.views import AtividadeViewSets,ListaAtividadesUsuarios

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSets, basename='Usuarios')
router.register('atividade', AtividadeViewSets, basename='Atividades')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', include(router.urls)),
    path('atividades/', include('atividades.urls')),
    path('usuario/<int:pk>/atividades/', ListaAtividadesUsuarios.as_view())

]
