from django.db import models

# Create your models here.
class User(models.Model):
    User_id = models.IntegerField()
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    permission = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    sensor_id = models.IntegerField()
    name = models.CharField(max_length=32)
    value = models.IntegerField()

    my_sensor = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
