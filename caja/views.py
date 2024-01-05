from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Producto
from .forms import ProductoForm, ActualizarProductoForm, CalendarioForm

# Create your views here.

@login_required
def  caja(request):
    fecha_actual = timezone.now()
    form_crear = ProductoForm(request.POST or None, initial={'cantidad': 1})
    productos = Producto.objects.filter(usuario=request.user, fecha_venta__date=fecha_actual)
    
    venta = 0
    
    for producto in productos:
        venta += producto.precio * producto.cantidad
          
    if request.method == 'POST':
        
        if form_crear.is_valid():
            nuevo_producto = form_crear.save(commit=False)
            nuevo_producto.usuario = request.user
            
            if nuevo_producto.precio < 50 and nuevo_producto.cantidad < 1:
                messages.warning(request, "Error, Los datos precio y cantidad son incorrectos!")
                
            elif nuevo_producto.precio < 50:
                 messages.warning(request, "Error, El precio debe ser mayor a 50!")
                 
            elif nuevo_producto.cantidad < 1:
                 messages.warning(request, "Error, La cantidad debe ser mayor a 1!")
            else:
                
                for producto in productos:
                    if nuevo_producto.nombre.replace(" ", "").lower() == producto.nombre.replace(" ", "").lower():
                        messages.info(request, f"El producto {producto.nombre} ya existe")
                        return redirect("caja:actualizar_producto", pk=producto.id)
                
                messages.success(request, f"El producto {nuevo_producto.nombre} ha sido creado!")
                nuevo_producto.save()
                return redirect("caja:caja")
        
        else:
            messages.warning(request, "Los datos son invalidos")

        
    context = {
        "productos" : productos,
        "form_crear" : form_crear,
        "venta" : venta,
        "fecha_actual": fecha_actual,
    }
    
    return render(request, 'pages/caja/caja.html', context)

@login_required
def historial(request):
    fecha = timezone.localtime(timezone.now())
    fecha = fecha.strftime('%Y-%m-%d')
    form_calendario = CalendarioForm(request.POST or None, initial={'fecha': fecha})
    productos = Producto.objects.filter(usuario=request.user, fecha_venta__date=fecha)

    venta = 0
    
    if form_calendario.is_valid():
        fecha = form_calendario.cleaned_data['fecha']
        productos = Producto.objects.filter(usuario=request.user, fecha_venta__date=fecha)
    
    for producto in productos:
        venta += producto.precio * producto.cantidad
        
    context = {
        "productos" : productos,
        "venta" : venta,
        "form_calendario" : form_calendario,
        "fecha" : fecha
    }
    
    return render(request, 'pages/caja/historial.html', context)
    

@login_required
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, usuario=request.user, pk=pk)
    form_actualizar = ActualizarProductoForm(request.POST or None, instance=producto)
    
    if request.method == 'POST':
        
        if form_actualizar.is_valid():
            actualizar_producto = form_actualizar.save(commit=False)
            
            if actualizar_producto.precio < 50 and actualizar_producto.cantidad < 1:
                messages.warning(request, "Error, Los datos precio y cantidad son incorrectos!")
                
            elif actualizar_producto.precio < 50:
                 messages.warning(request, "Error, El precio debe ser mayor a 50!")
                 
            elif actualizar_producto.cantidad < 1:
                 messages.warning(request, "Error, La cantidad debe ser mayor a 1!")
                 
            else:
                
                messages.success(request, f"El producto {actualizar_producto.nombre} ha sido actualizado!")
                actualizar_producto.save()
                return redirect("caja:caja")
            
        else:
            messages.warning(request, "Los datos son invalidos!")
    
    contexto = {
        "form_actualizar" : form_actualizar,
        "producto" : producto,
    }

    return render(request, 'pages/caja/actualizar_producto.html', contexto)
  
@login_required  
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, usuario=request.user, pk=pk)
    messages.info(request, f"El producto {producto.nombre} ha sido eliminado!")
    producto.delete()
    return redirect("caja:caja")