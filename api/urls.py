from rest_framework.routers import DefaultRouter
from .views import ProfilViewSet, SessionViewSet, DetectionViewSet

router = DefaultRouter()

router.register(r"profil", ProfilViewSet)
router.register(r"session", SessionViewSet)
router.register(r"detection", DetectionViewSet)

urlpatterns = router.urls