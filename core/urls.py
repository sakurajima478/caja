from django.contrib import admin
from django.urls import path, include

from .views import (
    inicio,
    signIn,
    registro,
    salir,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('inicio', inicio, name='inicio'),
    
    path('login/', signIn, name="login"),
    path('registro/', registro, name="registro"),
    path('salir/', salir, name="salir"),
    
    path('', include('caja.urls', namespace='caja')),
]
