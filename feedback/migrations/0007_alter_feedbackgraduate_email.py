# Generated by Django 4.2.7 on 2024-04-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_alter_feedbackgraduate_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackgraduate',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True, verbose_name='Почта'),
        ),
    ]
