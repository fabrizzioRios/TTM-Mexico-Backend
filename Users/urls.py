from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from Users.routers import user_router


urlpatterns = [
    path('', include(user_router.urls)),
    path('users/auth-token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
