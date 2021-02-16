from rest_framework import routers

from .viewsets import (
    TrayectoViewSet,
    RutaViewSet,
    AsientoViewSet,
    BusViewSet,
    ChoferViewSet,
    PasajeroViewSet,
)


router = routers.SimpleRouter()
router.register(r'trayectos', TrayectoViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'asientos', AsientoViewSet)
router.register(r'pasajeros', PasajeroViewSet)
router.register(r'choferes', ChoferViewSet)
router.register(r'buses', BusViewSet)
urlpatterns = router.urls
