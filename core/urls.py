from django.contrib import admin
from django.urls import path, include

from .views import (
    signIn,
    registro,
    salir,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', signIn, name="login"),
    path('registro/', registro, name="registro"),
    path('salir/', salir, name="salir"),
    
    path('', include('caja.urls', namespace='caja')),
]
