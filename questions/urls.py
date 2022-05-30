from django.urls import path
from . import views

app_name = "questions"
urlpatterns = [
    path('', views.home.index, name="home"),
    path('question1/', views.Question1.index_question1),
    path('question1/search', views.Question1.search_question1),
    path('question2/', views.Question2.index),
]
