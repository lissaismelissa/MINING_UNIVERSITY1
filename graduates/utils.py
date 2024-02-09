from ast import Str
import string
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from graduates.models import Graduates


def q_search(query):
    # if query.isdigit():
    #     return Graduates.objects.filter(id=int(query))
    
    vector = SearchVector("name", "current_work_or_study_place", "average_score", "graduation_year", "faculty__name", "direction__name", "profile__name", "qualification__name", "edication_form__name", "group__name", "department__name")
    query = SearchQuery(query)
    
    return Graduates.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)
    #     q_objects |= Q(current_work_or_study_place__icontains=token)
    #     q_objects |= Q(graduation_year__icontains=token)


    # return Graduates.objects.filter(q_objects)
