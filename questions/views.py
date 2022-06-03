import json

from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,Http404
from .models import ticket, Airport
from .forms import SearchForm
from django.core.checks import messages
from django.core.serializers import serialize
import requests
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

class Question2():
    def index(request):
        form = SearchForm
        airports = Airport.objects.order_by('-id')

        if request.GET.get('search_tag'):
            search_airports = []
            search_keyword = request.GET['data']
            search_tag = request.GET['search_tag']

            if search_tag == 'iata':
                search_airports = airports.filter(iata=search_keyword)
            elif search_tag == 'name':
                search_airports = airports.filter(name=search_keyword)
            elif search_tag == 'city':
                search_airports = airports.filter(city=search_keyword)


            # paginator = Paginator(search_airports, 15)
            context = {'data_list': search_airports, 'form': form, 'search_tag': search_tag}
            return render(request, "questions/question2/index.html", context)

        context = {'data_list': airports, 'form':form }

        return render(request, "questions/question2/index.html", context)

    def detail(request, pk):
        airport = Airport.objects.filter(pk=pk).values()

        return JsonResponse(*airport)

# 리스트뷰를 위한 로컬db 생성
# 1회만 실행 목적 /
class Setup():
    def setup(self):
        data = ticket.get_ticket_json()
        for key, value in data.items():
            airport = Airport.objects.create(icao=value['icao'], iata=value['iata'], name=value['name'], city=value['city'],
                                             state=value['state'], country=value['country'], elevation=value['elevation'],
                                             lat=value['lat'], lon=value['lon'], tz=value['tz'])
        return redirect('questions:home')


