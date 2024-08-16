from random import choices
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from users.models import UserGraduate, UserCompany, UserTeacher


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserGraduate
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()
    
class UserCompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = UserCompany
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "company",
            "username",
            "email",
            "password1",
            "password2",
            "is_company",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    is_company = forms.BooleanField()

class UserGraduateRegistrationForm(UserCreationForm):
    class Meta:
        model = UserGraduate
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "email",
            "slug",
            "group",
            
            # "faculty",
            # "direction",
            # "profile",
            # "qualification",
            # "edication_form",
            # "department",
            
            "company",
            "graduation_year",
            "average_score",
            "password1",
            "password2",
            "is_graduate",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    slug = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    average_score = forms.FloatField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    is_graduate = forms.BooleanField()
    
class UserTeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = UserTeacher
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "email",
            "password1",
            "password2",
            "is_teacher",
            "post",
            "department"
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    is_teacher = forms.BooleanField()
    post = forms.CharField()

class ProfileFormGraduate(UserChangeForm):
    class Meta:
        model = UserGraduate
        fields = (
            "image",
            "email",
            "company",
            "post",
            "skills",
            "achievements",
            "status_of_working",
        )

    image = forms.ImageField(required=False)
    email = forms.CharField()
    company = forms.Textarea()
    post = forms.Textarea()
    skills = forms.Textarea()
    achievements = forms.Textarea()
    status_of_working = forms.Textarea()

class ProfileFormCompany(UserChangeForm):
    class Meta:
        model = UserCompany
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "image",
            "email",
            "company",
            "post",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    username = forms.CharField()
    image = forms.ImageField(required=False)
    email = forms.CharField()
    post = forms.CharField()
    # company = forms.Textarea()
    
class ProfileFormTeacher(UserChangeForm):
    class Meta:
        model = UserTeacher
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "image",
            "email",
            "post", 
            "department",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    username = forms.CharField()
    image = forms.ImageField(required=False)
    email = forms.CharField()
    post = forms.CharField()