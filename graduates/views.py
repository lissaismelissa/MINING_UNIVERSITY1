from cgi import print_form
from email import contentmanager
import imp
from itertools import count
from logging import Filter
from django.core.paginator import Paginator
from django.shortcuts import render
from graduates.models import Companies, Faculties, Directions, Qualifications, Groups, Statuses
from graduates.utils import q_search, q_search_companies
from users.models import UserGraduate, Comments
from graduates.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.db.models import Avg, Func


def graduates_list(request):
    page = request.GET.get("page", 1)
    order_by = request.GET.get("order_by", None)
    faculty_filter = request.GET.get("faculty_filter", None)
    direction_filter = request.GET.get("direction_filter", None)
    qualification_filter = request.GET.get("qualification_filter", None)
    group_filter = request.GET.get("group_filter", None)
    query = request.GET.get("q", None)

    graduates = UserGraduate.objects.all()
    faculties = Faculties.objects.all()
    directions = Directions.objects.all()
    qualifications = Qualifications.objects.all()
    groups = Groups.objects.all()
    grad = UserGraduate.objects.all()

    if query:
        graduates = q_search(query)

    if faculty_filter and faculty_filter != "default":
        graduates = graduates.filter(faculty__name=faculty_filter)
        directions = directions.filter(faculty__name=faculty_filter)
        groups = groups.filter(faculty__name=faculty_filter)

    if direction_filter and direction_filter != "default":
        if faculty_filter and faculty_filter != "default":
            graduates = graduates.filter(faculty__name=faculty_filter)
        graduates = graduates.filter(direction__name=direction_filter)
        groups = groups.filter(direction__name=direction_filter)
            

    if qualification_filter and qualification_filter != "default":
        graduates = graduates.filter(qualification__name=qualification_filter)

    if group_filter and group_filter != "default":
        if faculty_filter and faculty_filter != "default":
            graduates = graduates.filter(faculty__name=faculty_filter)
        if direction_filter and direction_filter != "default":
            graduates = graduates.filter(direction__name=direction_filter)
        graduates = graduates.filter(group__name=group_filter)

    if order_by and order_by != "default":
        graduates = graduates.order_by(order_by)

    paginator = Paginator(graduates, 10)
    current_page = paginator.page(int(page))
    

    context = {
        "title": "Выпускники Горного Университета - Поиск выпускников",
        "graduates": current_page,
        "faculties": faculties,
        "directions": directions,
        "qualifications": qualifications,
        "groups": groups,
        "grad": grad,
    }
    return render(request, "graduates/graduates_list.html", context)


def graduate(request, graduate_slug):
    graduate = UserGraduate.objects.get(slug=graduate_slug)
    comments = Comments.objects.order_by("-create_date")
    context1 = {}
    if graduate.company:
        company = Companies.objects.get(id=graduate.company_id)
        coords = Companies.objects.get(id=graduate.company_id)
        coords = coords.coords
        context1 = {
        "coords": coords,
        "company": company,
    }
    
    is_comment = 0
    for i in comments:
        if i.username_graduate.id == graduate.id:
            is_comment += 1
            
    if context1 == {}:
        context = {
        "title": graduate.last_name
        + " "
        + graduate.first_name
        + " ",
        "graduate": graduate,
        "comments": comments,
        "is_comment": is_comment,
    }
    else:  
        context = {
            "title": graduate.last_name
            + " "
            + graduate.first_name
            + " ",
            "graduate": graduate,
            "comments": comments,
            "coords": coords,
            "company": company,
            "is_comment": is_comment,
        }

    return render(request, "graduates/graduate.html", context=context)


def save_comment(request, graduate_slug):
    if request.method == "POST":
        if not request.POST["textarea"] == "":
            Comments.objects.create(username_graduate_id=request.POST["username_graduate"],
                                   username_author_id=request.user.id,
                                   text=request.POST["textarea"])

    return redirect('graduates_list:graduate', graduate_slug=graduate_slug)


def companies_list(request):
    page = request.GET.get("page", 1)
    query = request.GET.get("q", None)
    companies = Companies.objects.all()
    comp = Companies.objects.all()
    graduates = UserGraduate.objects.all()

    if query:
        companies = q_search_companies(query)
        
    paginator = Paginator(companies, 10)
    current_page = paginator.page(int(page))
    
    

    context = {
        "title": "Выпускники Горного Университета - Поиск организаций",
        "companies": current_page,
        "comp": comp,
        "graduates": graduates,
    }
    return render(request, "graduates/companies_list.html", context=context)


def graduates_statistic(request):
    statuses = Statuses.objects.all()
    graduates = UserGraduate.objects.all()
    faculties = Faculties.objects.all()
    directions = Directions.objects.all()
    qualifications = Qualifications.objects.all()
    groups = Groups.objects.all()
    
    faculty_filter = request.GET.get("faculty_filter", None)
    direction_filter = request.GET.get("direction_filter", None)
    qualification_filter = request.GET.get("qualification_filter", None)
    group_filter = request.GET.get("group_filter", None)
    year_filter = request.GET.get("year_filter", None)
    
    if faculty_filter and faculty_filter != "default":
        graduates = graduates.filter(faculty__name=faculty_filter)
        directions = directions.filter(faculty__name=faculty_filter)
        groups = groups.filter(faculty__name=faculty_filter)

    if direction_filter and direction_filter != "default":
        if faculty_filter and faculty_filter != "default":
            graduates = graduates.filter(faculty__name=faculty_filter)
        graduates = graduates.filter(direction__name=direction_filter)
        groups = groups.filter(direction__name=direction_filter)
            

    if qualification_filter and qualification_filter != "default":
        graduates = graduates.filter(qualification__name=qualification_filter)

    if group_filter and group_filter != "default":
        if faculty_filter and faculty_filter != "default":
            graduates = graduates.filter(faculty__name=faculty_filter)
        if direction_filter and direction_filter != "default":
            graduates = graduates.filter(direction__name=direction_filter)
        graduates = graduates.filter(group__name=group_filter)
        
    if year_filter and year_filter != "default":
        if faculty_filter and faculty_filter != "default":
            graduates = graduates.filter(faculty__name=faculty_filter)
        if direction_filter and direction_filter != "default":
            graduates = graduates.filter(direction__name=direction_filter)
        if group_filter and group_filter != "default":
            graduates = graduates.filter(group__name=group_filter)
        graduates = graduates.filter(graduation_year=year_filter)

        
    for status in statuses:
        status.count = graduates.filter(status_of_working=status).count()
        if status.count == 0:
            status.percent = 0
        else:    
            status.percent = round((status.count / graduates.count()), 2) * 100
        
    graduates_count = graduates.count()
    if graduates_count == 0:
        average_marks_all = 0
        count_spb = 0
        count_russia = 0
        count_abroad = 0
    else:    
        average_marks_all = graduates.aggregate(Avg('average_score'))
        count_spb = graduates.filter(company__address__icontains='Санкт-Петербург').count()
        count_russia = graduates.filter(company__is_russia='True').count()
        count_abroad = graduates.filter(company__is_russia='False').count()
        
    
    context = {
        "title": "Выпускники Горного Университета - Статистика по выпускникам",
        "statuses": statuses,
        "graduates_count": graduates_count,
        "average_marks_all": average_marks_all,
        "count_russia": count_russia,
        "count_abroad": count_abroad,
        "count_spb": count_spb,
        "faculties": faculties,
        "directions": directions,
        "qualifications": qualifications,
        "groups": groups,
    }
    return render(request, "graduates/graduates_statistic.html", context=context)
