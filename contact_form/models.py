from xml.parsers.expat import model
from django.db import models


class Contact(models.Model):
    theme = models.TextField('Тема письма', max_length=100, default='Здравствуйте! Примите, пожалуйста, участие в нашем опросе!')
    email = models.CharField('Email', blank=True, null=True)
    message = models.TextField('Текст письма')

    def __str__(self):
        return self.email