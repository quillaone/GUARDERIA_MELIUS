from rest_framework import status
from apps.inventario.models import Empleado, RegistroArticulo, Articulo
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from .serializers import ArticuloSerializers, EmpleadoSerializers, RegistroArticuloSerializers
from django.db.models.manager import Manager
from django.db.models import Case, When


class ArticuloListView(APIView, LimitOffsetPagination):
    # get all
    def get(self, request):
        try:
            articulo = Articulo.objects.all()
            count = len(articulo)
            serializers = ArticuloSerializers(articulo, many=True)
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
            serializer = ArticuloSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "success created",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class ArticuloDetailView(APIView, LimitOffsetPagination):
    # get id
    def get(self, request, pk=None):
        try:
            articulo = Articulo.objects.filter(id=pk)
            # result = self.paginate_queryset(articulo, request, view=self)
            serializer = ArticuloSerializers(articulo, many=True)
            return Response(serializer.data)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo put (update)
    def put(self, request, pk=None):
        try:
            articulo = Articulo.objects.get(id=pk)
            serializer = ArticuloSerializers(articulo, data=request.data, partial=True)
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
            articulo = Articulo.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class ArticuloFilterView(APIView, LimitOffsetPagination):

    def get(self, request):

        try:
            articulo = Articulo.objects

            # filtro por nombre del articulo
            if 'name_articulo' in request.query_params:
                articulo = articulo.filter(name_articulo=request.query_params["name_articulo"])

            if request.query_params is None:
                articulo = articulo.all()

            serializer = ArticuloSerializers(articulo, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_204_NO_CONTENT)


class EmpleadoListView(APIView, LimitOffsetPagination):
    # get all
    def get(self, request):
        try:
            empleados = Empleado.objects.all()
            count = len(empleados)
            serializers = EmpleadoSerializers(empleados, many=True)
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
            serializer = EmpleadoSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "success created",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class EmpleadoDetailView(APIView, LimitOffsetPagination):
    # get id
    def get(self, request, pk=None):
        try:
            empleado = Empleado.objects.filter(id=pk)
            # result = self.paginate_queryset(articulo, request, view=self)
            serializer = EmpleadoSerializers(empleado, many=True)
            return Response(serializer.data)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo put (update)
    def put(self, request, pk=None):
        try:
            empleado = Empleado.objects.get(id=pk)
            serializer = EmpleadoSerializers(empleado, data=request.data, partial=True)
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
            empleado = Empleado.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class EmpleadoFilterView(APIView, LimitOffsetPagination):

    def get(self, request):

        try:

            empleado = Empleado.objects

            # filtro por nombre del empleado
            if 'nombre' in request.query_params:
                empleado = empleado.filter(nombre=request.query_params["nombre"])

            # filtro por email del empleado.
            if 'email' in request.query_params:
                empleado = empleado.filter(email=request.query_params["email"])

            # filtro por cargo del empleado
            if 'cargo' in request.query_params:
                empleado = empleado.filter(cargo=request.query_params["cargo"])

            if request.query_params is None:
                empleado = empleado.all()

            serializer = EmpleadoSerializers(empleado, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_204_NO_CONTENT)


class RegistroArticuloListView(APIView, LimitOffsetPagination):
    # get all
    def get(self, request):
        try:
            registro_articulo = RegistroArticulo.objects.all()
            count = len(registro_articulo)
            serializers = RegistroArticuloSerializers(registro_articulo, many=True)
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
            serializer = RegistroArticuloSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datos = {'message': "success created",
                         'result': serializer.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class RegistroArticuloDetailView(APIView, LimitOffsetPagination):
    # get id
    def get(self, request, pk=None):
        try:
            registro_articulo = RegistroArticulo.objects.filter(id=pk)
            # result = self.paginate_queryset(articulo, request, view=self)
            serializer = RegistroArticuloSerializers(registro_articulo, many=True)
            return Response(serializer.data)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # metodo put (update)
    def put(self, request, pk=None):
        try:
            registro_articulo = RegistroArticulo.objects.get(id=pk)
            serializer = RegistroArticuloSerializers(registro_articulo, data=request.data, partial=True)
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
            registro_articulo = RegistroArticulo.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)


class RegistroArticuloFilterView(APIView, LimitOffsetPagination):

    def get(self, request):
        try:
            registro_articulo = RegistroArticulo.objects

            # filtro por nombre del articulo
            if 'name_articulo' in request.query_params:
                registro_articulo = registro_articulo.filter(name_articulo=request.query_params["name_articulo"])

            # filtro por  empleado.
            if 'empleado' in request.query_params:
                registro_articulo = registro_articulo.filter(empleado=request.query_params["empleado"])

            # filtro por cargo disponibilidad
            if 'disponible' in request.query_params:
                registro_articulo = registro_articulo.filter(disponible=request.query_params["disponible"])

                # filtro por fecha de uso
            if 'date_use' in request.query_params:
                registro_articulo = registro_articulo.filter(date_use=request.query_params["date_use"])

            if request.query_params is None:
                registro_articulo = registro_articulo.all()

            serializer = RegistroArticuloSerializers(registro_articulo, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_204_NO_CONTENT)

