# Generated by Django 4.2.7 on 2024-02-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_answer_options_alter_answer_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ студента', 'verbose_name_plural': 'Ответы студента'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.BooleanField(default=0, verbose_name='Наличие ответа'),
        ),
    ]
