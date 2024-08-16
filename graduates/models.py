from email.policy import default
from itertools import count
from pyexpat import model
from sys import version
from tabnanny import verbose
from tokenize import blank_re
from django.db import models


class Faculties(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")

    class Meta:
        db_table = "faculty"
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Directions(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет"
    )

    class Meta:
        db_table = "direction"
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Profiles(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет"
    )
    direction = models.ForeignKey(
        to=Directions, on_delete=models.PROTECT, verbose_name="Направление подготовки"
    )

    class Meta:
        db_table = "profile"
        verbose_name = "Направленность(Профиль)"
        verbose_name_plural = "Направленности(Профили)"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Qualifications(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")

    class Meta:
        db_table = "qualification"
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"

    def __str__(self):
        return self.name


class EducationForms(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")

    class Meta:
        db_table = "edication_form"
        verbose_name = "Форма обучения"
        verbose_name_plural = "Формы обучения"

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет"
    )

    class Meta:
        db_table = "department"
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет"
    )
    direction = models.ForeignKey(
        to=Directions, on_delete=models.PROTECT, verbose_name="Направление подготовки"
    )
    profile = models.ForeignKey(
        to=Profiles, on_delete=models.PROTECT, verbose_name="Направленность(Профиль)"
    )
    department = models.ForeignKey(
        to=Departments, on_delete=models.PROTECT, verbose_name="Кафедра", blank=True, null=True,
    )
    qualification = models.ForeignKey(
        to=Qualifications, on_delete=models.PROTECT, verbose_name="Квалификация", blank=True, null=True,
    )

    class Meta:
        db_table = "group"
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ("name",)

    def __str__(self):
        return self.name



class Companies(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    address = models.CharField(max_length=150, verbose_name="Адрес")
    image = models.ImageField(
        upload_to="graduate_images", blank=True, null=True, verbose_name="Изображение"
    )
    coords = models.CharField(
        max_length=150, verbose_name="Координаты", blank=True, null=True
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_russia = models.BooleanField(default=True)

    class Meta:
        db_table = "companies"
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Graduates(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="graduate_images", blank=True, null=True, verbose_name="Изображение"
    )
    graduation_year = models.CharField(max_length=150, verbose_name="Год выпуска")
    average_score = models.FloatField(verbose_name="Средний балл диплома")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет"
    )
    direction = models.ForeignKey(
        to=Directions, on_delete=models.PROTECT, verbose_name="Направление подготовки"
    )
    profile = models.ForeignKey(
        to=Profiles, on_delete=models.PROTECT, verbose_name="Направленность(Профиль)"
    )
    qualification = models.ForeignKey(
        to=Qualifications, on_delete=models.PROTECT, verbose_name="Квалификация"
    )
    edication_form = models.ForeignKey(
        to=EducationForms, on_delete=models.PROTECT, verbose_name="Форма обучения"
    )
    group = models.ForeignKey(
        to=Groups, on_delete=models.PROTECT, verbose_name="Группа"
    )
    department = models.ForeignKey(
        to=Departments, on_delete=models.PROTECT, verbose_name="Кафедра"
    )
    company = models.ForeignKey(
        to=Companies,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Текущее место работы",
    )

    class Meta:
        db_table = "graduate"
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"
        ordering = ("id",)

    def __str__(self):
        return self.name
    
    
class Statuses(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    count = models.IntegerField(default=0, verbose_name="Количество выпускников")
    percent = models.FloatField(default=0.00, verbose_name="Количество выпускников в процентах")

    class Meta:
        db_table = "status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ("id",)

    def __str__(self):
        return self.name
