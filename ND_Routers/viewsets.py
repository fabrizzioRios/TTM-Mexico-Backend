from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ND_Routers.models import Router
from ND_Routers.serializers import RouterSerializer


class RouterViewSet(ModelViewSet):
    serializer_class = RouterSerializer
    queryset = Router.objects.all()
    permission_classes = [IsAdminUser]
