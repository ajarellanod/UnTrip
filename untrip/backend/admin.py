from django.contrib import admin

from .models import (
    Trayecto,
    Ruta,
    Bus,
    Asiento,
    Ticket
)


admin.site.register(Trayecto)
admin.site.register(Ruta)
admin.site.register(Bus)
admin.site.register(Asiento)
admin.site.register(Ticket)