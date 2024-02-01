from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Mining career - Главная',
        'content': 'Выпускники Горного Университета'
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Mining career - О нас',
        'content': 'О нас',
        'text_on_page': 'ldfkgvjaofslfnvskejfvnksdjfvn' 
        
    }
    
    return render(request, 'main/about.html', context)