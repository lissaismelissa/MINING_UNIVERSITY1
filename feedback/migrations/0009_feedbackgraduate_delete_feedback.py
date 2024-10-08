# Generated by Django 4.2.7 on 2024-04-15 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_usergraduate_status_of_working'),
        ('feedback', '0008_feedback_delete_feedbackgraduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackGraduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Почта')),
                ('description', models.TextField(blank=True, max_length=120, null=True, verbose_name='Описание')),
                ('graduate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.usergraduate', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
                'db_table': 'feedbackgraduate',
            },
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
    ]
