from django.contrib import admin

from .models import (
    Trayecto,
    Ruta,
    Bus,
    Asiento,
    Pasajero,
    Chofer
)


admin.site.register(Trayecto)
admin.site.register(Ruta)
admin.site.register(Bus)
admin.site.register(Asiento)
admin.site.register(Pasajero)
admin.site.register(Chofer)
