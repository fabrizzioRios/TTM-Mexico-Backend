from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ND_Switches.models import Switch
from ND_Switches.serializers import SwitchSerializer


class SwitchViewSet(ModelViewSet):
    serializer_class = SwitchSerializer
    queryset = Switch.objects.all()
    permission_classes = [IsAdminUser]
