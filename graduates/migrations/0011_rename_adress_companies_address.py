# Generated by Django 4.2.7 on 2024-03-07 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0010_alter_companies_latitude_alter_companies_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='adress',
            new_name='address',
        ),
    ]
