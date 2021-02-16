from rest_framework import serializers

from .models import Trayecto, Ruta, Asiento, Bus, Chofer, Pasajero


class TrayectoSerializer(serializers.ModelSerializer):
    
    rutas = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ruta-detail'
    )

    class Meta:
        model = Trayecto
        fields = '__all__'


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        exclude = ['ruta']


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):

    chofer_nombre = serializers.CharField(source="chofer.nombre", read_only=True)

    class Meta:
        model = Bus
        fields = '__all__'


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'


class RutaSerializer(serializers.ModelSerializer):
    
    asientos = AsientoSerializer(many=True, read_only=True)
    info_bus = BusSerializer(source="bus", read_only=True)

    class Meta:
        model = Ruta
        fields = '__all__'

    def create(self, validated_data):
        ruta = Ruta(**validated_data)
        if ruta.create():
            return ruta
        else:
            error = {'error': 'Bus is not available'}
            raise serializers.ValidationError(error)
