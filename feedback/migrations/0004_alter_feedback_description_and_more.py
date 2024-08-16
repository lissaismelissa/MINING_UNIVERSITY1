# Generated by Django 4.2.7 on 2024-04-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedbackcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='feedbackcompany',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='feedbackcompany',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True, verbose_name='Почта'),
        ),
    ]
