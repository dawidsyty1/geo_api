# Create your views here.
from accounts.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet


class UserCreateView(ModelViewSet):
    serializer_class = UserSerializer
