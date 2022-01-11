from .views import MascotaListView, MascotaDetailView, MascotaFilterView
from django.urls import path

urlpatterns = [
    path('mascotas/', MascotaListView.as_view()),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view()),
    path('mascotas/filters/', MascotaFilterView.as_view())

]
