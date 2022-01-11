from .views import ArticuloListView, ArticuloDetailView, ArticuloFilterView, EmpleadoListView, EmpleadoDetailView, \
    EmpleadoFilterView, RegistroArticuloListView, RegistroArticuloDetailView, RegistroArticuloFilterView
from django.urls import path

urlpatterns = [
    path('articulos/', ArticuloListView.as_view()),
    path('articulos/<int:pk>/', ArticuloDetailView.as_view()),
    path('articulos/filters/', ArticuloFilterView.as_view()),
    path('empleados/', EmpleadoListView.as_view()),
    path('empleados/<int:pk>/', EmpleadoDetailView.as_view()),
    path('empleados/filters/', EmpleadoFilterView.as_view()),
    path('registro/', RegistroArticuloListView.as_view()),
    path('registro/<int:pk>/', RegistroArticuloDetailView.as_view()),
    path('articulos/filters/', RegistroArticuloFilterView.as_view())

]
