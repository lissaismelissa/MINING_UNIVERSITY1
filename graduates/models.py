from email.policy import default
from pyexpat import model
from sys import version
from tabnanny import verbose
from django.db import models


class Faculties(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")

    class Meta:
        db_table = "faculty"
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def __str__(self):
        return self.name


class Directions(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет")

    class Meta:
        db_table = "direction"
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"

    def __str__(self):
        return self.name


class Profiles(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет")
    direction = models.ForeignKey(to=Directions, on_delete=models.PROTECT, verbose_name="Направление подготовки")

    class Meta:
        db_table = "profile"
        verbose_name = "Направленность(Профиль)"
        verbose_name_plural = "Направленности(Профили)"

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


class Groups(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет")
    direction = models.ForeignKey(
        to=Directions, on_delete=models.PROTECT, verbose_name="Направление подготовки")
    profile = models.ForeignKey(
        to=Profiles, on_delete=models.PROTECT, verbose_name="Направленность(Профиль)")

    class Meta:
        db_table = "group"
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    faculty = models.ForeignKey(to=Faculties, on_delete=models.PROTECT, verbose_name="Факультет")

    class Meta:
        db_table = "department"
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

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
    current_work_or_study_place = models.TextField(
        blank=True, null=True, verbose_name="Текущее место работы/учебы"
    )

    class Meta:
        db_table = "graduate"
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"
        ordering = ("id",)

    def __str__(self):
        return self.name
