from unittest import mock
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from graduates.models import Companies

from django.db.models import Q

from graduates.views import graduate

from users.models import UserGraduate

def index(request):
    companies = UserGraduate.objects.values('company__name').distinct()
    companies = Companies.objects.filter(~Q(name = "Санкт-Петербургский Горный Университет"))
    
        
    context = {
        'title': 'Выпускникини Горного Университета - Главная страница',
        'content': 'Выпускники Горного Университета',
        "companies" : companies,
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Mining career - О нас',
        'content': 'О нас',
        'text_on_page': 'Сервис разработан для Выпускной Квалификационной работы студентки группы ИАС Благополучной Елизаветой' 
        
    }
    
    return render(request, 'main/about.html', context)