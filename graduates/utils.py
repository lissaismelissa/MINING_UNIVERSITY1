from ast import Str
import string
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from graduates.models import Companies
from users.models import UserGraduate


def q_search(query):
    vector = SearchVector("first_name", "last_name", "middle_name", "post", "achievements", "skills", "company__name", "average_score", "graduation_year", "faculty__name", "direction__name", "profile__name", "qualification__name", "edication_form__name", "group__name", "department__name")
    query = SearchQuery(query)
    
    return UserGraduate.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

def q_search_companies(query):
    # if query.isdigit():
    #     return Graduates.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description", "address")
    query = SearchQuery(query)
    
    return Companies.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")