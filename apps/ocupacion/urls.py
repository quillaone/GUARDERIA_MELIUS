from .views import ReservationListView, ReservationDetailView, ReservationFilterView
from django.urls import path

urlpatterns = [
    path('ocupacion/', ReservationListView.as_view()),
    path('ocupacion/<int:pk>/', ReservationDetailView.as_view()),
    path('ocupacion/filters/', ReservationFilterView.as_view())

]
