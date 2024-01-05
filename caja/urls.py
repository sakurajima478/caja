from django.urls import path

from .views import (
    caja,
    historial,
    eliminar_producto,
    actualizar_producto
)

app_name = 'caja'

urlpatterns = [
    path('', caja, name='caja'),
    path('historial/', historial, name="historial"),
    path('actualizar/<int:pk>', actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>', eliminar_producto, name='eliminar_producto'),
]
