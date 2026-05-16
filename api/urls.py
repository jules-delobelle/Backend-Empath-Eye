from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, DetectionViewSet, EnfantViewSet

router = DefaultRouter()

router.register(r"enfant", EnfantViewSet, basename="enfant")
router.register(r"session", SessionViewSet, basename="session")
router.register(r"detection", DetectionViewSet, basename="detection")

urlpatterns = router.urls