from rest_framework import generics, permissions
from demo_app1.models import User, Sensor
from demo_app1.serializers import UserSer, SensorSer
from demo_app1.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(permission=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSer
    permission_classes = (permissions.IsAuthenticated, )

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSer
    permission_classes = (permissions.IsAuthenticated, )

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sensors': reverse('sensor-list', request=request, format=format)
    })
