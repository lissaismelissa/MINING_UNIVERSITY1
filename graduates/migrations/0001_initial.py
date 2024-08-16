# Generated by Django 4.2.7 on 2024-02-07 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
                'db_table': 'direction',
            },
        ),
        migrations.CreateModel(
            name='EducationForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Форма обучения',
                'verbose_name_plural': 'Формы обучения',
                'db_table': 'edication_form',
            },
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификации',
                'db_table': 'qualification',
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.directions', verbose_name='Направление подготовки')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Направленность(Профиль)',
                'verbose_name_plural': 'Направленности(Профили)',
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.directions', verbose_name='Направление подготовки')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.profiles', verbose_name='Направленность(Профиль)')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Graduates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='graduate_images', verbose_name='Изображение')),
                ('graduation_year', models.CharField(max_length=150, verbose_name='Год выпуска')),
                ('average_score', models.FloatField(verbose_name='Средний балл диплома')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.departments', verbose_name='Кафедра')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.directions', verbose_name='Направление подготовки')),
                ('edication_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.educationforms', verbose_name='Форма обучения')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.groups', verbose_name='Группа')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.profiles', verbose_name='Направленность(Профиль)')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.qualifications', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Выпускник',
                'verbose_name_plural': 'Выпускники',
                'db_table': 'graduate',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='directions',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='departments',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='graduates.faculties', verbose_name='Факультет'),
        ),
    ]
