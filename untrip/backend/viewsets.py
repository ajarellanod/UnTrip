from decimal import Decimal
from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q, F, Avg, Count, ExpressionWrapper, FloatField

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

    @action(detail=True, 
            methods=['get'],
            url_path="rutas/(?P<porcentaje>[^/.]+)")
    def rutas(self, request, porcentaje=None, *args, **kwargs):
        """
        Devuelve Rutas con un porcentaje
        de ocupación mayor que el indicado
        """
        trayecto = self.get_object()
        query = trayecto.rutas.filter(
            disponible=True,
            salida__gte=datetime.now()
        )

        if porcentaje is not None:
            porcentaje_real = round(float(porcentaje) / 100, 2)

            query = query.annotate(
                reservados=Count(
                    "asientos",
                    filter=Q(
                        asientos__estado=Asiento.RESERVADO
                    )
                ),
                total=Count("asientos")
            ).annotate(
                porcentaje=ExpressionWrapper(
                    F("reservados") * Decimal('1.0') / F("total"),
                    output_field=FloatField(),
                )
            )

            queryset = query.filter(porcentaje__gte=porcentaje_real)
        else:
            queryset = query.get_queryset()

        serializer = RutaSerializer(queryset, many=True)
        return Response(serializer.data)


class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    @action(detail=True, methods=['get'])
    def asientos(self, request, pk=None):
        ruta = self.get_object()
        asientos = ruta.asientos.filter(estado=Asiento.DISPONIBLE)
        serializer = AsientoSerializer(asientos, many=True)
        return Response(serializer.data)

    @action(detail=True, 
            methods=['post'], 
            url_path="reservar/(?P<idt>[^/.]+)")
    def reservar(self, request, pk=None, idt=None):
        ruta = self.get_object()
        serializer = PasajeroSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # Creando Pasajero y Obteniendo Asiento
            pasajero = serializer.save()
            asiento = ruta.asientos.get(identificador=idt)

            # Reservando Asiento
            if asiento.estado == asiento.DISPONIBLE:
                asiento.reservar(pasajero)
                asiento.save()

            # Respondiendo con el Asiento
            serializer = AsientoSerializer(asiento)
            return Response(serializer.data)


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
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
