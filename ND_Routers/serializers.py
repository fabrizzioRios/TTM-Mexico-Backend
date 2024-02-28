from rest_framework.serializers import ModelSerializer

from ND_Routers.models import Router


class RouterSerializer(ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'
