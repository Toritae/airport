import requests
from django.db import models
# Create your models here.
class ticket:
    def get_ticket_json():
        url = "https://gist.githubusercontent.com/creduo/90aafdc0d28a7b45ca6e75d82600a5cf/raw/69a67722ed3f82403751597fba5ca5cb4b576abd/airports.json"
        res = requests.get(url).json()
        return res

class Airport(models.Model):
    icao = models.CharField(max_length=10, unique=True)
    iata = models.CharField(max_length=5)
    name = models.TextField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    elevation = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    tz = models.TextField()

    class Meta:
        db_table = 'airport'