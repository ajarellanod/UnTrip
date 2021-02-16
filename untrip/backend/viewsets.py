from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Trayecto, Ruta, Asiento, Bus, Pasajero, Chofer
from .serializers import (
    TrayectoSerializer,
    RutaSerializer,
    AsientoSerializer,
    BusSerializer,
    ChoferSerializer,
    PasajeroSerializer,
)


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
        return Response({"message": "Asiento Reservado Correctamente"})


class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        queryset = Chofer.objects.filter(bus=None)
        serializer = ChoferSerializer(queryset, many=True)
        return Response(serializer.data)


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
