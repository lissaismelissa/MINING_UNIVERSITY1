from email import message
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from graduates.models import (
    Departments,
    Faculties,
    Directions,
    Profiles,
    Qualifications,
    EducationForms,
    Groups,
    Companies,
    Statuses,
)
from users.models import UserGraduate, UserCompany, UserTeacher

from users.forms import (
    ProfileFormGraduate,
    ProfileFormCompany,
    UserLoginForm,
    UserCompanyRegistrationForm,
    UserGraduateRegistrationForm,
    ProfileFormTeacher,
    UserTeacherRegistrationForm,
)

# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(
                    request, f"{request.user.first_name}, Вы успешно вошли в аккаунт."
                )

                if request.POST.get("next", None):
                    return HttpResponseRedirect(redirect.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration_graduate(request):
    if request.method == "POST":
        form = UserGraduateRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            # auth.login(request, user)
            group = Groups.objects.get(id = request.POST["group"])
            UserGraduate.objects.filter(slug=request.POST["slug"]).update(faculty_id = group.faculty)
            UserGraduate.objects.filter(slug=request.POST["slug"]).update(direction_id = group.direction)
            UserGraduate.objects.filter(slug=request.POST["slug"]).update(profile_id = group.profile)
            UserGraduate.objects.filter(slug=request.POST["slug"]).update(department_id = group.department)
            UserGraduate.objects.filter(slug=request.POST["slug"]).update(qualification_id = group.qualification)
            
            messages.success(
                request,
                "Выпускник успешно зарегистрирован",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserGraduateRegistrationForm()

    faculties = Faculties.objects.all()
    directions = Directions.objects.all()
    profiles = Profiles.objects.all()
    qualifications = Qualifications.objects.all()
    edication_forms = EducationForms.objects.all()
    groups = Groups.objects.all()
    departments = Departments.objects.all()
    companies = Companies.objects.all()

    context = {
        "title": "Регистрация выпускника",
        "form": form,
        "faculties": faculties,
        "directions": directions,
        "profiles": profiles,
        "qualifications": qualifications,
        "edication_forms": edication_forms,
        "groups": groups,
        "departments": departments,
        "companies": companies,
    }
    return render(request, "users/registration_graduate.html", context)


def registration_company(request):
    if request.method == "POST":
        form = UserCompanyRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request,
                f"{request.user.first_name}, Вы успешно зарегистрированы и вошли в аккаунт. Пожалуйста, заполните профиль пользователя",
            )
            return HttpResponseRedirect(reverse("users:profile_company"))
    else:
        form = UserCompanyRegistrationForm()

    companies = Companies.objects.all()

    context = {
        "title": "Регистрация работодателя",
        "form": form,
        "companies": companies,
    }
    return render(request, "users/registration_company.html", context)


def registration_teacher(request):
    if request.method == "POST":
        form = UserTeacherRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            # auth.login(request, user)
            messages.success(
                request,
                "Сотрудник успешно зарегистрирован",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserTeacherRegistrationForm()

    departments = Departments.objects.all()

    context = {
        "title": "Регистрация сотрудника",
        "form": form,
        "departments": departments,
    }
    return render(request, "users/registration_teacher.html", context)


@login_required
def profile_graduate(request):
    user_graduate = UserGraduate.objects.get(username=request.user.username)
    companies = Companies.objects.all()
    statuses = Statuses.objects.all()
    if request.method == "POST":
        if (
            not companies.filter(
                name=request.POST["company"],
            ).exists()
            and not companies.filter(
                name=request.POST["name"],
            ).exists()
            and not request.POST["name"] == ""
        ):
            Companies.objects.create(
                name=request.POST["name"],
                address=request.POST["address"],
                coords=request.POST["coords"],
                is_russia=request.POST["is_russia"],
            )
        form = ProfileFormGraduate(
            data=request.POST, instance=user_graduate, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile_graduate"))
    else:
        form = ProfileFormGraduate(instance=user_graduate)

    companies = Companies.objects.all()

    context = {
        "title": "Личный кабинет",
        "form": form,
        "user_graduate": user_graduate,
        "companies": companies,
        "statuses": statuses,
    }
    return render(request, "users/profile_graduate.html", context)


@login_required
def profile_company(request):
    user_company = UserCompany.objects.get(username=request.user.username)
    companies = Companies.objects.all()
    if request.method == "POST":
        if (
            not companies.filter(
                name=request.POST["company"],
            ).exists()
            and not companies.filter(
                name=request.POST["name"],
            ).exists()
            and not request.POST["name"] == ""
        ):
            Companies.objects.create(
                name=request.POST["name"],
                address=request.POST["address"],
                coords=request.POST["coords"],
                is_russia=request.POST["is_russia"],
            )
        form = ProfileFormCompany(
            data=request.POST, instance=user_company, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile_company"))
    else:
        form = ProfileFormCompany(instance=user_company)

    context = {
        "title": "Личный кабинет",
        "form": form,
        "user_company": user_company,
        "companies": companies,
    }
    return render(request, "users/profile_company.html", context)


@login_required
def profile_teacher(request):
    user_teacher = UserTeacher.objects.get(username=request.user.username)
    if request.method == "POST":
        form = ProfileFormTeacher(
            data=request.POST, instance=user_teacher, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile_teacher"))
    else:
        form = ProfileFormTeacher(instance=user_teacher)

    departments = Departments.objects.all()

    context = {
        "title": "Личный кабинет",
        "form": form,
        "user_teacher": user_teacher,
        "departments": departments,
    }
    return render(request, "users/profile_teacher.html", context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.first_name}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
