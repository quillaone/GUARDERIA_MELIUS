from django.urls import path
from django.conf.urls import (url, include)

urlpatterns = [
    path('guarderia/', include('apps.ocupacion.urls')),
    path('guarderia/', include('apps.mascotas.urls')),
    path('guarderia/', include('apps.inventario.urls'))
]
