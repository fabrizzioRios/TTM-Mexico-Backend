
from rest_framework.routers import DefaultRouter
from ND_Routers.viewsets import RouterViewSet

routers_router = DefaultRouter()

routers_router.register(
    "routers",
    RouterViewSet,
    basename="routers-viewsets"
)
