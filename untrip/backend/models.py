from decimal import Decimal

from django.db import models
from django.db.models import Q, F, Avg, Count, ExpressionWrapper, FloatField


class Chofer(models.Model):

    nombre = models.CharField(max_length=100)

    edad = models.IntegerField()

    class Meta:
        verbose_name_plural = "Choferes"


class Pasajero(models.Model):

    nombre = models.CharField(max_length=100)

    identificacion = models.IntegerField()


class Bus(models.Model):

    chofer = models.OneToOneField(
        'Chofer',
        on_delete=models.CASCADE,
    )

    capacidad = models.IntegerField()

    class Meta:
        verbose_name_plural = "Buses"


class Asiento(models.Model):

    DISPONIBLE = 1
    RESERVADO = 2

    ESTADOS = (
        (DISPONIBLE, "Disponible"),
        (RESERVADO, "Reservado")
    )

    estado = models.IntegerField(
        choices=ESTADOS,
        default=DISPONIBLE
    )

    identificador = models.IntegerField()

    ruta = models.ForeignKey(
        'Ruta',
        on_delete=models.CASCADE,
        related_name="asientos"
    )

    pasajero = models.ForeignKey(
        'Pasajero',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def reservar(self, pasajero):
        self.pasajero = pasajero

    def save(self, *args, **kwargs):
        if self.pasajero:
            self.estado = self.RESERVADO
        super().save(*args, **kwargs)

    class Meta:   
        constraints = [
            models.UniqueConstraint(fields=['ruta', 'pasajero'], name='unique-pasajero')
        ]
        


class Ruta(models.Model):

    trayecto = models.ForeignKey(
        'Trayecto',
        on_delete=models.CASCADE,
        related_name="rutas"
    )

    bus = models.ForeignKey(
        'Bus',
        on_delete=models.CASCADE,
        related_name="rutas"
    )

    salida = models.DateTimeField()

    llegada = models.DateTimeField(null=True, blank=True)


    def crear_asientos(self):
        for idt in range(self.bus.capacidad):
            Asiento.objects.create(ruta=self, identificador=idt+1)


    def es_valido_bus(self):
        """ 
        Valida que el bus tenga disponibilidad
        en una fecha y hora en particular.
        """
        query = Ruta.objects.filter(
            bus=self.bus,
            llegada__gte=self.salida,
            salida__lte=self.salida,
        )

        if query.first():
            return False
        else:
            return True


    def save(self, *args, **kwargs):
        if self.es_valido_bus():
            self.llegada = self.trayecto.duracion + self.salida
            super().save(*args, **kwargs)
        else:
            raise ValueError("Bus No Disponible")


class Trayecto(models.Model):
    
    nombre = models.CharField(max_length=100)

    duracion = models.DurationField()

    def promedio_pasajeros(self):
        """
        Calcula el promedio de Pasajeros
        en un Trayecto por cada Ruta Existente.
        """
        query = self.rutas.annotate(
            pasajeros=Count(
                "asientos",
                filter=Q(
                    asientos__estado=Asiento.RESERVADO
                )
            )
        ).aggregate(Avg("pasajeros"))

        result = query["pasajeros__avg"]
        
        if result is not None:
            return round(result, 2)
        else:
            return 0.0
