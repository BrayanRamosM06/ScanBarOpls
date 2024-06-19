"""
URL configuration for ScanBarOpls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path

from ScanBarApp.views import FormularioProductView
from .Views.homeView import HomeView


urlpatterns = [
    #path('admin/', admin.site.urls),
    #vamos a crear la ruta predeterminada para que se ejecute cuando se inicie el servidor
    #path('Page/', HomeView.pageOne, name='PageOne'),
    #path('Page2/<int:parametro1>',HomeView.page2, name='page2'),
    #path('Page3/<int:parametro1>/<int:parametro2>',HomeView.page3, name='page3')
    path('',HomeView.home, name='home'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('registrarProducto/',FormularioProductView.index, name = "registrarProducto" ),
    path('GuardarProducto/', FormularioProductView.ProcesarFormulario, name = 'guardarProducto'),
    path('ListarProducto/', FormularioProductView.listarProducto, name = 'listarProducto'),
    path('ProductoEdit/<int:id_producto>', FormularioProductView.editProducto, name = 'editProducto'),
    path('ProductoActualizar/<int:id_producto>', FormularioProductView.actualizarProducto, name = 'actualizarProducto'),
    path('DeleteProducto/<int:id_producto>', FormularioProductView.deleteProducto, name = 'deleteProducto'),
    path('FiltrarProducto/<str:sku_producto>', FormularioProductView.filtrarProducto, name = 'filtrarProducto'),


]
