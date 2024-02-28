
from rest_framework.routers import DefaultRouter
from Users.viewsets import UserViewSet


user_router = DefaultRouter()

user_router.register(
    "users",
    UserViewSet,
    basename="users-viewsets"
)
