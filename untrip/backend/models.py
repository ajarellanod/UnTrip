from django.db import models


class Horario(models.Model):
    salida = models.TimeField()


class Bus(models.Model):
    pass


class Trayecto(models.Model):
    nombre = models.CharField()


class Ruta(models.Model):
    
    trayecto = models.ForeignKey(
        'Trayecto',
        on_delete=models.CASCADE
    )
    
    horario = models.ForeignKey(
        'Horario',
        on_delete=models.CASCADE
    )
    
    bus = models.ForeignKey(
        'Bus',
        on_delete=models.CASCADE
    )



    
    
    


    
    
    
    