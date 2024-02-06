from django.urls import path

from graduates import views

app_name = 'graduates'

urlpatterns = [
    path('search/', views.graduates_list, name='search'),
    path('', views.graduates_list, name='index'),
    path('graduate/<slug:graduate_slug>/', views.graduate, name='graduate'),
]