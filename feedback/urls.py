from django.urls import path
from .views import FeedBackViewGraduate, FeedBackViewCompany, FeedBackViewList, FeedBackDeleteGraduate, FeedBackDeleteCompany, ChangeCompany, Company, DeleteCompany, ChangeGraduate, Graduate, DeleteGraduate, WarningDeleteCompany, WarningDeleteGraduate

app_name = 'feedback'

urlpatterns = [
    path('feedbackgraduate/', FeedBackViewGraduate.as_view(), name='feedbackgraduate_view'),
    path('feedbackcompany/', FeedBackViewCompany.as_view(), name='feedbackcompany_view'),
    path('feedbacklist/', FeedBackViewList, name='feedbacklist'),
    path('feedbackdeletegraduate/<int:id>/', FeedBackDeleteGraduate, name='feedbackdeletegraduate'),
    path('feedbackdeletecompany/<int:id>/', FeedBackDeleteCompany, name='feedbackdeletecompany'),
    path('company/<int:id>/', Company, name='company'),
    path('change_company/<int:id>/', ChangeCompany, name='change_company'),
    path('delete_company/<int:id>/', DeleteCompany, name='delete_company'),
    path('graduate/<slug:graduate_slug>/', Graduate, name='graduate'),
    path('change_graduate/<slug:graduate_slug>/', ChangeGraduate, name='change_graduate'),
    path('delete_graduate/<slug:graduate_slug>/', DeleteGraduate, name='delete_graduate'),
    path('warning_delete_company/<int:id>/', WarningDeleteCompany, name ='warning_delete_company'),
    path('warning_delete_graduate/<slug:graduate_slug>/', WarningDeleteGraduate, name ='warning_delete_graduate'),
]