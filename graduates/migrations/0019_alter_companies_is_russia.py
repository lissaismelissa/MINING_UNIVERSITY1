# Generated by Django 4.2.7 on 2024-04-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0018_companies_is_russia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='is_russia',
            field=models.BooleanField(default=1),
        ),
    ]
