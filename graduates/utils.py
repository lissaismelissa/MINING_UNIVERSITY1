from django.db.models import Q

from graduates.models import Graduates


def q_search(query):
    if query.isdigit():
        return Graduates.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(current_work_or_study_place__icontains=token)
        q_objects |= Q(graduation_year__icontains=token)


    return Graduates.objects.filter(q_objects)
