from rest_framework.serializers import ModelSerializer

from ND_Switches.models import Switch


class SwitchSerializer(ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'
