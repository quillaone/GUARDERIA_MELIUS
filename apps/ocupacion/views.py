from rest_framework import status
from apps.ocupacion.models import Reservacion
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from .serializers import ReservationSerializers
from django.db.models.manager import Manager
from django.db.models import Case, When


class ReservationListView(APIView, LimitOffsetPagination):
    # get all
    def get(self, request):
        try:
            reservations = Reservacion.objects.all()
            print(reservations.query) #sentencia SQL
            # results = self.paginate_queryset(reservations, request, view=self)
            reservations_serializers = ReservationSerializers(reservations, many=True)
            return Response(reservations_serializers.data)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo post (create)
    def post(self, request):
        try:
            serializer = ReservationSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "success created",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class ReservationDetailView(APIView, LimitOffsetPagination):
    # get id
    def get(self, request, pk=None):
        try:
            reservation = Reservacion.objects.filter(id=pk)
            # result = self.paginate_queryset(reservation, request, view=self)
            serializer = ReservationSerializers(reservation, many=True)
            return Response(serializer.data)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo put (update)
    def put(self, request, pk=None):
        try:
            reservation = Reservacion.objects.get(id=pk)
            serializer = ReservationSerializers(reservation, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "update success",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'error': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo delete.
    def delete(self, request, pk=None):
        try:
            reservation = Reservacion.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class ReservationFilterView(APIView, LimitOffsetPagination):
    def get(self, request):
        try:
            reservacion = Reservacion.objects


            # filtro por reservas
            if 'fecha_reserva' in request.query_params:
                reservacion = reservacion.filter(fecha_reserva=request.query_params["fecha_reserva"])

            # filtro por rango de fecha.
            if 'fecha_creacion' in request.query_params:
                fecha_creacion = request.query_params['fecha_creacion'].split('-')
                reservacion = reservacion.filter(fecha_creacion__range=(fecha_creacion[0], fecha_creacion[1])).values(
                    'id_reservacion').distinct()

            if request.query_params is None:
                reservacion = reservacion.all()

            if isinstance(reservacion, Manager):
                reservacion = reservacion.all()

            results = self.paginate_queryset(reservacion, request, view=self)
            serializer = ReservationSerializers(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_204_NO_CONTENT)
