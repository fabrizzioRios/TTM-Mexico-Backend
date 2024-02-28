from django.urls import include, path

from ND_Switches.routers import switch_router

urlpatterns = [
    path('', include(switch_router.urls)),
]
