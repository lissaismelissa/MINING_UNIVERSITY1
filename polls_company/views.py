import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render

from .models import Question_company, Choice_company, Answer_company


def index(request):
    questions_list = Question_company.objects.order_by("id")
    answers_list = Answer_company.objects.filter(username_company_id=request.user.id)
    que_list = []
    check_list = []
    for que in questions_list:
        a = que.id
        que_list += [a]
    for ans in answers_list:
        a = ans.question_id
        check_list += [a]

    context = {
        "title": "Выпускники Горного Университета - Анкета работодателя",
        "questions_list": questions_list,
        "answers_list": answers_list,
        "check_list": check_list,
        "que_list": que_list,
    }
    return render(request, "polls_company/index.html", context)


def results(request):
    # questions_list = get_object_or_404(Question, pk = question_id)
    questions_list = Question_company.objects.order_by("id")
    
    for question in questions_list:
        choices_list = Choice_company.objects.filter(question=question.id)
        all_votes = 0
        
        for choice in choices_list:
            all_votes += choice.votes
        
        for choice in choices_list:
            choice_percent = round(((choice.votes / all_votes) * 100), 2)
            Choice_company.objects.filter(id = choice.id).update(choice_percent = choice_percent)
        
        context = {
        "questions_list": questions_list,
        "choices_list": choices_list,
        "choice_percent": choice_percent,
        "title": "Выпускники Горного Университета - Результаты опроса работодателей",
        }
    
    return render(request, "polls_company/results.html", context)


def vote(request):
    questions = Question_company.objects.order_by("id")
    answers_list = Answer_company.objects.filter(username_company_id=request.user.id)
    check_list = []
    for ans in answers_list:
        a = ans.question_id
        check_list += [a]

    if request.method == "POST":
        for q in questions:
            if q.id not in check_list:
                selected_choice = q.choice_company_set.get(
                    pk=request.POST["choice" + str(q.id)]
                )
                selected_choice.votes += 1
                selected_choice.save()
                answer = Answer_company.objects.create(
                    username_company_id=request.user.id,
                    question_id=q.id,
                    choice_id=selected_choice.id,
                )

    return HttpResponseRedirect(reverse("main:index"))


def add_question(request):                
    context = {"title": "Выпускники Горного Университета - Добавить новый вопрос в анкету работодателя",
             }         

    return render(request, "polls_company/add_question.html", context)

def save_question(request):
    if request.method == "POST":
        question = Question_company.objects.create(question_text=request.POST["question"])
        choice = Choice_company.objects.create(
            question_id=question.id, choice_text=request.POST["choice1"]
        )
        for i in range(2, 10):
            if not request.POST["choice" + str(i)] == "":
                choice = Choice_company.objects.create(
                    question_id=question.id, choice_text=request.POST["choice" + str(i)]
                )
    return HttpResponseRedirect(reverse("polls_company:add_question"))

def warning_delete_question(request, id):
    question = Question_company.objects.get(id=id)
    context = {
        "question": question,
        "title": "Выпускники Горного Университета - Удаление вопроса из анкеты работодателей",
    }
    return render(request, "polls_company/warning_delete_question.html", context)

def delete_question(request, id):
    if request.method == "GET":
        Question_company.objects.filter(id=id).delete()      

    return HttpResponseRedirect(reverse("polls_company:results"))

def change_question(request, id):
    question = Question_company.objects.get(id=id)
    choices = Choice_company.objects.filter(question = id)
    
    context = {
        "title": "Выпускники Горного Университета - Редактирование вопроса из анкеты работодателей",
        "question": question,
        "choices": choices,
    }
    
    return render(request, "polls_company/change_question.html", context)

def save_change_question(request):
    choices = Choice_company.objects.filter(question = request.POST["q_id"])
    if request.method == "POST":
        Question_company.objects.filter(id=request.POST["q_id"]).update(question_text=request.POST["question"])
        for choice in choices:
            Choice_company.objects.filter(id=request.POST["ch_id" + str(choice.id)]).update(choice_text=request.POST["choice" + str(choice.id)])

        return HttpResponseRedirect(reverse("polls_company:results"))
    
    context = {
        "question": question,
        "choices": choices,
    }
    return render(request, "polls_company/change_question.html", context)
