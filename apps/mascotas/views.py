from rest_framework import status
from apps.mascotas.models import Mascota
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from .serializers import MascotaSerializers
from django.db.models.manager import Manager
from django.db.models import Case, When


class MascotaListView(APIView, LimitOffsetPagination):
    # get all
    def get(self, request):
        try:
            mascotas = Mascota.objects.all()
            count = len(mascotas)
            serializers = MascotaSerializers(mascotas, many=True)
            datos = {'message': "success",
                     'count': count,
                     'next': None,
                     'previus': None,
                     'results': serializers.data}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo post (create)
    def post(self, request):
        try:
            serializer = MascotaSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "success created",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class MascotaDetailView(APIView, LimitOffsetPagination):
    # get id
    def get(self, request, pk=None):
        try:
            mascota = Mascota.objects.filter(id=pk)
            # result = self.paginate_queryset(mascota, request, view=self)
            serializer = MascotaSerializers(mascota, many=True)
            return Response(serializer.data)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo put (update)
    def put(self, request, pk=None):
        try:
            mascota = Mascota.objects.get(id=pk)
            serializer = MascotaSerializers(mascota, data=request.data, partial=True)
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
            mascota = Mascota.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class MascotaFilterView(APIView, LimitOffsetPagination):

    def get(self, request):

        try:
            mascota = Mascota.objects

            # filtro por nombre de la mascota
            if 'nombre' in request.query_params:
                mascota = mascota.filter(nombre=request.query_params["nombre"])

            # filtro por propietario de la mascota.
            if 'propietario' in request.query_params:
                mascota = mascota.filter(propietario=request.query_params["propietario"])

            if 'tipo' in request.query_params:
                mascota = mascota.filter(tipo=request.query_params["tipo"])



            if request.query_params is None:
                mascota = mascota.all()

            if isinstance(reservacion, Manager):
                mascota = mascota.all()

            results = self.paginate_queryset(mascota, request, view=self)
            serializer = MascotaSerializers(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_204_NO_CONTENT)
