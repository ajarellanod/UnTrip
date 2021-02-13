from django.db import models
from django.db.models import Q, F


class Ticket(models.Model):

    pasajero = models.CharField(max_length=100)

    asiento = models.ForeignKey(
        'Asiento',
        on_delete=models.CASCADE,
        related_name="tickets"
    )


class Bus(models.Model):

    DISPONIBLE = 1
    EN_RUTA = 2
    
    ESTADOS = (
        (DISPONIBLE, "Disponible"),
        (EN_RUTA, "En Ruta")
    )

    estado = models.IntegerField(
        choices=ESTADOS, default=DISPONIBLE
    )

    chofer = models.CharField(max_length=100)

    capacidad = models.IntegerField()


class Trayecto(models.Model):
    
    nombre = models.CharField(max_length=100)

    duracion = models.DurationField()


class Asiento(models.Model):

    DISPONIBLE = 1
    RESERVADO = 2

    identificador = models.IntegerField()

    ESTADOS = (
        (DISPONIBLE, "Disponible"),
        (RESERVADO, "Reservado")
    )

    ruta = models.ForeignKey(
        'Ruta',
        on_delete=models.CASCADE,
        related_name="asientos"
    )

    estado = models.IntegerField(choices=ESTADOS, default=DISPONIBLE)


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

    llegada = models.DateTimeField()

    def gen_asientos(self):
        """ Genera Asiento para la ruta creada """
        for identificador in range(self.bus.capacidad):
            asiento = Asiento(ruta=self, identificador=identificador)
            asiento.save()


    def is_valid_bus(self):
        """ Valida que el Bus tenga disponibilidad """
        query = Ruta.objects.filter(
            Q(bus=self.bus),
            Q(llegada__gte=self.salida),
        )

        if query.first():
            return False
        else:
            return True


    def save(self, *args, **kwargs):
        if self.is_valid_bus():
            self.llegada = self.salida + self.trayecto.duracion
            super().save(*args, **kwargs)
            self.gen_asientos()
        else:
            raise ValueError("Bus no disponible en esa fecha")
