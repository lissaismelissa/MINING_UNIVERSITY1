# Generated by Django 4.2.7 on 2024-06-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0019_alter_companies_is_russia'),
        ('users', '0028_usergraduate_status_of_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergraduate',
            name='edication_form',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='graduates.educationforms', verbose_name='Форма обучения'),
        ),
    ]
