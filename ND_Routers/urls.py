from django.urls import include, path

from ND_Routers.routers import routers_router

urlpatterns = [
    path('', include(routers_router.urls)),
]
