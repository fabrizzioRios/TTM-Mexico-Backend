from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from Users.models import User
from Users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)


