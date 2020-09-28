from rest_framework import serializers
from demo_app1.models import User, Sensor

class UserSer(serializers.ModelSerializer):
    permission = serializers.ReadOnlyField(source='permission.username')
    class Meta:
        model = User
        fields = '__all__'

class SensorSer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'
