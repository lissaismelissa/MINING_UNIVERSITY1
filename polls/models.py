from email.policy import default
from pyexpat import model
from django.db import models
from users.models import UserGraduate

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Текст вопроса")

    class Meta:
        db_table = "questions"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ("id",)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    choice_text = models.CharField(max_length=200, verbose_name="Вариант ответа")
    votes = models.IntegerField(default=0, verbose_name="Количество голосов")
    choice_percent = models.FloatField(default=0, verbose_name="Процент голосов")

    class Meta:
        db_table = "choices"
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"
        ordering = ("id",)
        

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    username_graduate = models.ForeignKey(
        to=UserGraduate,
        on_delete=models.CASCADE,
        verbose_name="Выпускник",
        blank=True,
        null=True,
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, verbose_name="Ответ", null=True
    )

    class Meta:
        db_table = "answers"
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студентов"
