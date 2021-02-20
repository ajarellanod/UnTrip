from rest_framework import serializers

from .models import Trayecto, Ruta, Asiento, Bus, Chofer, Pasajero


class TrayectoSerializer(serializers.ModelSerializer):
    
    rutas = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ruta-detail'
    )

    promedio_pasajeros = serializers.SerializerMethodField()

    class Meta:
        model = Trayecto
        fields = '__all__'

    def get_promedio_pasajeros(self, obj):
        return obj.promedio_pasajeros()


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = '__all__'


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):

    chofer_nombre = serializers.CharField(
        source="chofer.nombre",
        read_only=True
    )

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
        try:
            ruta = Ruta.objects.create(**validated_data)
            ruta.crear_asientos()
            return ruta
        except Exception as error:
            raise serializers.ValidationError(error)
