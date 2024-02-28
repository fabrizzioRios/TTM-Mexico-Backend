
from rest_framework.routers import DefaultRouter
from ND_Switches.viewsets import SwitchViewSet

switch_router = DefaultRouter()

switch_router.register(
    "switches",
    SwitchViewSet,
    basename="switches-viewsets"
)
