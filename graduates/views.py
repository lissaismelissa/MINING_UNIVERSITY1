from django.core.paginator import Paginator
from django.shortcuts import render

from graduates.models import Graduates
from graduates.utils import q_search


def graduates_list(request):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    graduates = Graduates.objects.all()

    if query:
        graduates = q_search(query)

    if order_by and order_by != "default":
        graduates = graduates.order_by(order_by)

    paginator = Paginator(graduates, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Mining career - Выпускники Горного Университета",
        "graduates": current_page,
    }
    return render(request, "graduates/graduates_list.html", context)


def graduate(request, graduate_slug):
    graduate = Graduates.objects.get(slug=graduate_slug)

    context = {"graduate": graduate}

    return render(request, "graduates/graduate.html", context=context)