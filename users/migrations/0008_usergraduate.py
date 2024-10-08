# Generated by Django 4.2.7 on 2024-02-22 13:02

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0001_initial'),
        ('users', '0007_remove_user_average_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGraduate',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('middle_name', models.CharField(max_length=150, null=True, verbose_name='Отчество')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users_image', verbose_name='Изображение пользователя')),
                ('graduation_year', models.CharField(max_length=150, null=True, verbose_name='Год выпуска')),
                ('average_score', models.FloatField(null=True, verbose_name='Средний балл диплома')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.departments', verbose_name='Кафедра')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.directions', verbose_name='Направление подготовки')),
                ('edication_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.educationforms', verbose_name='Форма обучения')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.groups', verbose_name='Группа')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.profiles', verbose_name='Направленность(Профиль)')),
                ('qualification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.qualifications', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Пользователь_выпускник',
                'verbose_name_plural': 'Пользователи_выпускники',
                'db_table': 'user_graduate',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
