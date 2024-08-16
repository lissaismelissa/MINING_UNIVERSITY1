from django.db import models
from graduates.models import Companies
from users.models import UserGraduate

class FeedBackGraduate(models.Model):
    email = models.EmailField('Почта', max_length=120, blank=True, null=True)
    description = models.TextField('Описание', max_length=120, blank=True, null=True)
    graduate = models.ForeignKey(
        to=UserGraduate,
        on_delete=models.CASCADE,
        verbose_name="Выпускник",
        blank=True,
        null=True,
    )
    
    class Meta:
        db_table = "feedbackgraduate"
        verbose_name = "Форма обратной связи для выпускников"
        verbose_name_plural = "Формы обратной связи для выпускников"

    def __str__(self):
        return self.description
    
class FeedBackCompany(models.Model):
    email = models.EmailField('Почта', max_length=120, blank=True, null=True)
    company = models.ForeignKey(
        to=Companies,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        blank=True,
        null=True,
    )
    description = models.TextField('Описание', blank=True, null=True)
    
    class Meta:
        db_table = "feedbackcompany"
        verbose_name = "Форма братной связи для компаний"
        verbose_name_plural = "Формы братной связи для компаний"

    def __str__(self):
        return self.description