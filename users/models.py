from email.mime import image
from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from graduates.models import (
    Faculties,
    Directions,
    Departments,
    Profiles,
    EducationForms,
    Qualifications,
    Groups,
    Companies, 
    Statuses
)


class User(AbstractUser):
    is_graduate = models.BooleanField("graduate status", default=False)
    is_company = models.BooleanField("company status", default=False)
    is_teacher = models.BooleanField("teacher status", default=False)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class UserGraduate(User):
    middle_name = models.CharField(blank=True, null=True, max_length=150, verbose_name="Отчество")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="users_image",
        blank=True,
        null=True,
        verbose_name="Изображение пользователя",
    )
    graduation_year = models.CharField(
        null=True, max_length=150, verbose_name="Год выпуска"
    )
    average_score = models.FloatField(null=True, verbose_name="Средний балл диплома")
    faculty = models.ForeignKey(
        to=Faculties, on_delete=models.PROTECT, null=True, verbose_name="Факультет"
    )
    direction = models.ForeignKey(
        to=Directions,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Направление подготовки",
    )
    profile = models.ForeignKey(
        to=Profiles,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Направленность(Профиль)",
    )
    qualification = models.ForeignKey(
        to=Qualifications,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Квалификация",
    )
    edication_form = models.ForeignKey(
        to=EducationForms,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Форма обучения",
        default=1,
    )
    group = models.ForeignKey(
        to=Groups, on_delete=models.PROTECT, null=True, verbose_name="Группа"
    )
    department = models.ForeignKey(
        to=Departments, on_delete=models.PROTECT, null=True, verbose_name="Кафедра"
    )
    
    company = models.ForeignKey(
        to=Companies,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        blank=True,
        null=True,
    )
    post = models.CharField(blank=True, null=True, max_length=150, verbose_name="Должность")
    skills = models.TextField(blank=True, null=True, verbose_name="Навыки")
    achievements = models.TextField(blank=True, null=True, verbose_name="Карьерные достижения")
    
    status_of_working= models.ForeignKey(
        to=Statuses,
        on_delete=models.CASCADE,
        verbose_name="Статус",
        blank=True,
        null=True,
        default=1,
    )
    
    class Meta:
        db_table = "user_graduate"
        verbose_name = "Пользователь_выпускник"
        verbose_name_plural = "Пользователи_выпускники"
        ordering = ("last_name",)

    def __str__(self):
        return self.username


class UserCompany(User):
    middle_name = models.CharField(blank=True, null=True, max_length=150, verbose_name="Отчество")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="users_image",
        blank=True,
        null=True,
        verbose_name="Изображение пользователя",
    )
    company = models.ForeignKey(
        to=Companies,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        blank=True,
        null=True,
    )
    post = models.CharField(null=True, max_length=150, verbose_name="Должность")

    class Meta:
        db_table = "user_company"
        verbose_name = "Пользователь_компания"
        verbose_name_plural = "Пользователи_компании"

    def __str__(self):
        return self.username
    
    
class UserTeacher(User):
    middle_name = models.CharField(blank=True, null=True, max_length=150, verbose_name="Отчество")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="users_image",
        blank=True,
        null=True,
        verbose_name="Изображение пользователя",
    )
    post = models.CharField(null=True, max_length=150, verbose_name="Должность")
    department = models.ForeignKey(
        Departments, on_delete=models.CASCADE, null=True, verbose_name="Кафедра"
    )

    class Meta:
        db_table = "user_teacher"
        verbose_name = "Пользователь_преподаватель"
        verbose_name_plural = "Пользователи_преподаватели"

    def __str__(self):
        return self.username


class Comments(models.Model):
    username_graduate = models.ForeignKey(
        to=UserGraduate,
        on_delete=models.CASCADE,
        verbose_name="Выпускник",
        blank=True,
        null=True,
    )
    username_author = models.ForeignKey(
        to=UserCompany,
        on_delete=models.CASCADE,
        verbose_name="Автор комментария",
        blank=True,
        null=True,
    )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name="Текст комментария")

    class Meta:
        db_table = "comment"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("id",)

    def __str__(self):
        # return 'Отзыв на выпускника ' + f'{self.username_graduate.last_name}' + ' ' + f'{self.username_graduate.first_name}' + ' от ' + f'{self.username_author.company}'
        return self.text