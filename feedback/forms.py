from dataclasses import fields
from django import forms

from graduates.models import Companies
from users.models import UserGraduate

from .models import FeedBackGraduate, FeedBackCompany
from django.contrib.auth.forms import UserChangeForm


class FeedBackFormGraduate(forms.ModelForm):
    class Meta:
        model = FeedBackGraduate
        fields = ['graduate', 'description', 'email']

class FeedBackFormCompany(forms.ModelForm):
    class Meta:
        model = FeedBackCompany
        fields = ['company', 'description', 'email']

class ProfileFormCompany(forms.ModelForm):
    class Meta:
        model = Companies
        fields = (
            "name",
            "image",
            "description",
            "is_russia",
            "address",
            "coords",
        )

class ProfileFormGraduate(forms.ModelForm):
    class Meta:
        model = UserGraduate
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "faculty",
            "direction",
            "profile",
            "qualification",
            "edication_form",
            "group",
            "department",
            "average_score",
            "graduation_year",
        )
        
    average_score = forms.FloatField()