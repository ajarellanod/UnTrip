from rest_framework import routers

from .viewsets import TrayectoViewSet, RutaViewSet, AsientoViewSet


router = routers.SimpleRouter()
router.register(r'trayectos', TrayectoViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'asientos', AsientoViewSet)
urlpatterns = router.urls
