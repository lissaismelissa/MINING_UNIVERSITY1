from re import X
from django.conf import settings
from django.shortcuts import render, redirect
from django.template import context
from feedback.models import FeedBackGraduate, FeedBackCompany

from graduates.models import Companies, Departments, Directions, EducationForms, Faculties, Groups, Profiles, Qualifications
from users.models import UserGraduate
from .forms import FeedBackFormGraduate, FeedBackFormCompany, ProfileFormCompany, ProfileFormGraduate
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



class FeedBackViewGraduate(View):
    def post(self, request):
        form = FeedBackFormGraduate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/graduates_list")
        
class FeedBackViewCompany(View):
    def post(self, request):
        form = FeedBackFormCompany(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/graduates_list/companies_list")
        
def FeedBackViewList(request):
    list_graduate = FeedBackGraduate.objects.all()
    list_company = FeedBackCompany.objects.all()
    
    context = {
        "title": "Выпускники Горного Университета - Заявки на изменение данных",
        "list_graduate": list_graduate, 
        "list_company": list_company, 
    }
    return render(request, "feedback/feedbacklist.html", context)


def FeedBackDeleteGraduate(request, id):
    if request.method == "GET":
        FeedBackGraduate.objects.filter(id=id).delete()      

    return HttpResponseRedirect(reverse("feedback:feedbacklist"))


def FeedBackDeleteCompany(request, id):
    if request.method == "GET":
        FeedBackCompany.objects.filter(id=id).delete()      

    return HttpResponseRedirect(reverse("feedback:feedbacklist"))


def Company(request, id):
    company = Companies.objects.get(id=id)    

    context = {
        "title": "Выпускники Горного Университета - Редактирование карточки компании",
        "company": company, 
    }
    return render(request, "feedback/company.html", context)


def ChangeCompany(request, id):
    company = Companies.objects.get(id=id)
    
    if request.method == "POST":
        form = ProfileFormCompany(
            data=request.POST, instance=company, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль компании обновлен")
            return HttpResponseRedirect(reverse("feedback:company", kwargs={'id':id}))
    else:
        form = ProfileFormCompany(instance=company)

    context = {
        "title": "Профиль компании",
        "form": form,
        "company": company,
    }
    return render(request, "feedback/company.html", context)


def WarningDeleteCompany(request, id):
    company = Companies.objects.get(id=id)
    context = {
        "company": company,
    }
    return render(request, "feedback/warning_delete_company.html", context)


def DeleteCompany(request, id):
    if request.method == "GET":
        Companies.objects.get(id=id).delete()      

    return HttpResponseRedirect(reverse("feedback:feedbacklist"))


def Graduate(request, graduate_slug):
    graduate = UserGraduate.objects.get(slug=graduate_slug)
    edication_forms = EducationForms.objects.all()
    faculties = Faculties.objects.all()
    directions = Directions.objects.all()
    departments = Departments.objects.all()
    qualifications = Qualifications.objects.all()
    groups = Groups.objects.all()
    profiles = Profiles.objects.all() 

    context = {
        "title": "Выпускники Горного Университета - Редактирование карточки выпускника",
        "graduate": graduate,
        "faculties": faculties,
        "directions": directions,
        "profiles": profiles,
        "departments": departments,
        "qualifications": qualifications,
        "groups": groups,
        "edication_forms": edication_forms, 
    }
    return render(request, "feedback/graduate.html", context)


def ChangeGraduate(request, graduate_slug):
    graduate = UserGraduate.objects.get(slug=graduate_slug)
    
    if request.method == "POST":
        form = ProfileFormGraduate(
            data=request.POST, instance=graduate, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль выпускника обновлен")
            return HttpResponseRedirect(reverse("feedback:graduate", kwargs={'graduate_slug':graduate_slug}))
    else:
        form = ProfileFormGraduate(instance=graduate)

    context = {
        "title": "Профиль выпускника",
        "form": form,
        "graduate": graduate,
    }
    return render(request, "feedback/graduate.html", context)


def WarningDeleteGraduate(request, graduate_slug):
    graduate = UserGraduate.objects.get(slug=graduate_slug)
    context = {
        "graduate": graduate,
    }
    return render(request, "feedback/warning_delete_graduate.html", context)


def DeleteGraduate(request, graduate_slug):
    if request.method == "GET":
        UserGraduate.objects.get(slug=graduate_slug).delete()      

    return HttpResponseRedirect(reverse("feedback:feedbacklist"))