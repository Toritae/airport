import json
from django.views.generic import ListView
from django.shortcuts import render
from django.http import JsonResponse,Http404
from .models import ticket
from .forms import SearchForm
# Create your views here.

class home():
    def index(request):
        return render(request, 'questions/index.html')

class Question1():
    def index_question1(request):
        return render(request, 'questions/question1/index.html')

    # 현재 제공받은 json 데이터에선 iata 데이터가 ''인경우를 제외하곤 1개 이므로 json 단일처리, 2개이상, 즉,''일시 icao를 키값으로 원본데이터를 유지하게 처리.
    # 전달받은 iata코드가 데이터중 일치하는 코드가 없을시, 404status return.
    def search_question1(request):
        airport = ticket.get_ticket_json()
        try:
            search_res = []
            none_res = {}
            for key, value in airport.items():
                for k, v in value.items():
                    if request.GET['iata'] == '':
                        if k == 'icao':
                            icao = key
                        if k == 'iata':
                            none_res[icao] = value

                    elif k == 'iata' and request.GET['iata'] == v:
                        search_res.append(value)
                        break
            if len(none_res) < 1:
                return JsonResponse(*search_res)
            else:
                return JsonResponse(none_res)
        except:
            raise Http404("iata not found")

class Question2(ListView):
    def index(request):
        context = {}
        form = SearchForm
        context['form'] = form
        return render(request, 'questions/question2/index.html', context)

    def detail_question2(request):
        # result =
        return render(request, 'questions/question2/detail.html', json)