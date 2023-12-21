from django.urls import path

from .views import (
    caja,
    eliminar_producto,
    actualizar_producto
)

app_name = 'caja'

urlpatterns = [
    path('', caja, name='caja'),
    path('actualizar/<int:pk>', actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>', eliminar_producto, name='eliminar_producto'),
]
