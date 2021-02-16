from django.db import models
from django.db.models import Q, F


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

    def __str__(self):
        return f"Bus({self.chofer})"

    class Meta:
        verbose_name_plural = "Buses"


class Trayecto(models.Model):
    
    nombre = models.CharField(max_length=100)

    duracion = models.DurationField()

    def __str__(self):
        return f"Trayecto({self.nombre})"


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

    pasajero = models.OneToOneField(
        'Pasajero',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def reservar(self):
        self.estado = self.RESERVADO
        self.save()


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


    def gen_asientos(self):
        """ Genera Asientos para la ruta creada """
        for identificador in range(self.bus.capacidad):
            asiento = Asiento(
                ruta=self,
                identificador=identificador + 1
            )
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


    def create(self):
        if self.is_valid_bus():
            self.llegada = self.salida + self.trayecto.duracion
            self.save()
            self.gen_asientos()
            return True
        else:
            return False
