# Generated by Django 4.2.7 on 2024-02-22 13:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_usergraduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('middle_name', models.CharField(max_length=150, null=True, verbose_name='Отчество')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users_image', verbose_name='Изображение пользователя')),
                ('post', models.CharField(max_length=150, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Пользователь_компания',
                'verbose_name_plural': 'Пользователи_компании',
                'db_table': 'user_company',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
