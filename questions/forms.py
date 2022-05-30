from django import forms

tags = [
    ('iata', '공항코드'),
    ('name', '이름'),
    ('city', '도시')
]

class SearchForm(forms.Form):
    search_tag = forms.ChoiceField(choices=tags)
    data = forms.CharField(max_length=30)