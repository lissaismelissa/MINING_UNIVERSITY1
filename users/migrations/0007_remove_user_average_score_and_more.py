# Generated by Django 4.2.7 on 2024-02-22 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_companyuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='user',
            name='edication_form',
        ),
        migrations.RemoveField(
            model_name='user',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='user',
            name='graduation_year',
        ),
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]
