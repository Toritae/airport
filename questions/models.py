import requests
from django.forms import ModelForm
# Create your models here.
class ticket:
    def get_ticket_json():
        url = "https://gist.githubusercontent.com/creduo/90aafdc0d28a7b45ca6e75d82600a5cf/raw/69a67722ed3f82403751597fba5ca5cb4b576abd/airports.json"
        res = requests.get(url).json()
        return res

# class SearchForm(ModelForm):
#     d
#     class Meta():
#         d