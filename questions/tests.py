from django.test import TestCase
from .models import Airport, ticket
# Create your tests here.
class TestQuestion1(TestCase):
    def test_get_json(self):
        data = ticket.get_ticket_json()
        print(data)

class TestQuestion2(TestCase):
    def test_add_local_model(self):
        data = ticket.get_ticket_json()
        for key, value in data.items():
            airport = Airport.objects.create(icao=value['icao'], iata=value['iata'], name=value['name'], city=value['city'],
                                             state=value['state'], country=value['country'], elevation=value['elevation'],
                                             lat=value['lat'], lon=value['lon'], tz=value['tz'])
        airport = Airport.objects.all()

