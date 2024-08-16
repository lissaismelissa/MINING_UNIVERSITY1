from django.urls import path
from graduates import views

app_name = 'graduates'

urlpatterns = [
    path('search/', views.graduates_list, name='search'),
    path('companies_list/', views.companies_list, name='companies_list'),
    path('graduates_statistic/', views.graduates_statistic, name='graduates_statistic'),
    path('companies_list_search', views.companies_list, name='companies_list_search'),
    path('', views.graduates_list, name='index'),
    path('graduate/<slug:graduate_slug>/', views.graduate, name='graduate'),
    path('save_comment/<slug:graduate_slug>/', views.save_comment, name='save_comment'),
]