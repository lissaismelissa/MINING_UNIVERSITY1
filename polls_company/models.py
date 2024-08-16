from email.policy import default
from django.db import models
from users.models import UserCompany

# Create your models here.

class Question_company(models.Model):
    question_text = models.CharField(max_length = 200, verbose_name="Текст вопроса")
    class Meta:
        db_table = "questions_company"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ("id",)
 
    def __str__(self):
        return self.question_text
 
 
class Choice_company(models.Model):
    question = models.ForeignKey(Question_company(), on_delete = models.CASCADE, verbose_name="Вопрос")
    choice_text = models.CharField(max_length = 200, verbose_name="Вариант ответа")
    votes = models.IntegerField(default = 0, verbose_name="Количество голосов")
    choice_percent = models.FloatField(default=0, verbose_name="Процент голосов")
    
    class Meta:
        db_table = "choices_company"
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"
        ordering = ("id",)
 
    def __str__(self):
        return self.choice_text
    
class Answer_company(models.Model):
    username_company = models.ForeignKey(
        to=UserCompany,
        on_delete=models.CASCADE,
        verbose_name="Представитель компании",
        blank=True,
        null=True,
    )
    question = models.ForeignKey(Question_company, on_delete = models.CASCADE, verbose_name="Вопрос")
    choice = models.ForeignKey(Choice_company, on_delete = models.CASCADE, verbose_name="Ответ", null=True)
    
    class Meta:
        db_table = "answers_company"
        verbose_name = "Ответ представителя компании"
        verbose_name_plural = "Ответы представителей компаний"