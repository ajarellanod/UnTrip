from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Trayecto, Ruta, Asiento
from .serializers import TrayectoSerializer, RutaSerializer, AsientoSerializer


class TrayectoViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer


class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    @action(detail=True, methods=['get', 'post'], url_path="reservar/(?P<identificador>[^/.]+)")
    def reservar(self, request, pk=None, identificador=None):
        ruta = self.get_object()
        asiento = ruta.asientos.get(identificador=identificador)
        asiento.reservar()
        return Response({"message": "Asiento reservado correctamente"})


class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer
