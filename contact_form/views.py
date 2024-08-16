from django.views.generic import CreateView

from graduates.models import Companies
from users.views import profile_teacher
from users.admin import UserAdmin
from users.models import UserCompany, UserGraduate
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm

from django.conf import settings


class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm
    
    context = {
         "title": "Выпускники Горного Университета - Рассылка писем",
      }
    
    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        companies = UserCompany.objects.all()
        graduates_list = UserGraduate.objects.all()
        senders_list = []
        if data['senders'] == 'companies':
           for company in companies:
              senders_list += [company.email]
        elif data['senders'] == 'graduates':
           for graduate in graduates_list:
              senders_list += [graduate.email]
        else:
           text = data['email']
           senders_list += text.split(',')
           
        subject = data['theme']
        email(subject, data['message'], senders_list)
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, message, recipient_list):
   send_mail(subject,
      message,
      settings.DEFAULT_FROM_EMAIL,
      recipient_list,
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   messages.success(request, "Письмо успешно отправлено!")
   return redirect("contact_page")