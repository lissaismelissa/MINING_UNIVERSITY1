from django.urls import path, reverse_lazy

from users import views

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration_graduate/', views.registration_graduate, name='registration_graduate'),
    path('registration_teacher/', views.registration_teacher, name='registration_teacher'),
    path('registration_company/', views.registration_company, name='registration_company'),
    path('profile_graduate/', views.profile_graduate, name='profile_graduate'),
    path('profile_teacher/', views.profile_teacher, name='profile_teacher'),
    path('profile_company/', views.profile_company, name='profile_company'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html', success_url = reverse_lazy('users:password_reset_done')), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url = reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/login.html'), name='password_reset_complete'),
]