from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['email','message', 'theme']