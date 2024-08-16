   
from django.urls import path
from . import views
 
app_name = 'polls'
urlpatterns = [
    path('', views.index, name ='index'),
    path('results/', views.results, name ='results'),
    path('add_question/', views.add_question, name ='add_question'),
    path('delete_question/<int:id>/', views.delete_question, name ='delete_question'),
    path('warning_delete_question/<int:id>/', views.warning_delete_question, name ='warning_delete_question'),
    path('change_question/<int:id>/', views.change_question, name ='change_question'),
    path('<save_question/', views.save_question, name ='save_question'),
    path('<save_change_question/', views.save_change_question, name ='save_change_question'),
    path('<vote/', views.vote, name ='vote'),
]