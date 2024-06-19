from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from ScanBarApp.forms import FormularioProducts
from ScanBarApp.models import Barcode

# Create your views here.
class FormularioProductView(HttpRequest):
    def index (request):
        producto = FormularioProducts()
        #vamos a retornar el request, una view y un diccionario donde hacemos referencia al formulario que creamos
        return render (request, "ProoductoIndex.html", {"form": producto})
    
    
    def ProcesarFormulario (request):
        producto = FormularioProducts(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducts()
        
        return render(request, "ProoductoIndex.html", {"form": producto, "message": 'ok'} )
    
    def listarProducto(request):
        producto = Barcode.objects.all()
        return render(request, "ListaProductos.html", {"productos": producto})
    
    #vamos a crear los metodos para poder editar registros

    def editProducto(request, id_producto):
        #vanos a obtener el producto que vamos a editar
        
        producto = Barcode.objects.filter(id=id_producto).first()
        form = FormularioProducts(instance=producto)

        return render(request, "productoEdit.html", {"form": form, "producto":producto})
    
    #vamos a crear un metodo para que podamos procesar los datos ya editados

    def actualizarProducto(request, id_producto):
        producto = Barcode.objects.get(id = id_producto)
        form = FormularioProducts(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        producto = Barcode.objects.all()
        return render(request, "ListaProductos.html",{"productos": producto, "message":'ok'})
    
    def deleteProducto(request, id_producto):
        producto = Barcode.objects.get(id=id_producto)
        producto.delete()
        productos =Barcode.objects.all()

        return render(request, "ListaProductos.html", {"productos":productos, "message":'ok'} )
    #vamos acreara un metodo para que nos muestre solo un rpoducto que nosotros le indiquemos.

    def filtrarProducto (request, sku_producto):
        sku_producto=7890045
        productos = Barcode.objects.filter(sku=sku_producto)

        if productos.exists():
           # productos=[productos]
            return render(request, "filtrar.html",{"productos": productos})
        else:
            #producto=[]
            return render(request, "filtrar.html",{"productos": productos, "mensaje": "No se encotraron registros con ese sku"})
    

       


        

