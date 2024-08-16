# Generated by Django 4.2.7 on 2024-02-16 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='average_score',
            field=models.FloatField(null=True, verbose_name='Средний балл диплома'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.departments', verbose_name='Кафедра'),
        ),
        migrations.AddField(
            model_name='user',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.directions', verbose_name='Направление подготовки'),
        ),
        migrations.AddField(
            model_name='user',
            name='edication_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.educationforms', verbose_name='Форма обучения'),
        ),
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_year',
            field=models.CharField(max_length=150, null=True, verbose_name='Год выпуска'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.groups', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.profiles', verbose_name='Направленность(Профиль)'),
        ),
        migrations.AddField(
            model_name='user',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.qualifications', verbose_name='Квалификация'),
        ),
    ]
