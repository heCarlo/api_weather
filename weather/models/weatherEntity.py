from django.db import models
import uuid

class WeatherEntity(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.IntegerField()
    city = models.CharField(max_length=100)
    atmospheric_pressure = models.IntegerField()
    humidity = models.IntegerField()
    weather = models.CharField(max_length=100)
    date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)
