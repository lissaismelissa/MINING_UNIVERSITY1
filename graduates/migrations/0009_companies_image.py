# Generated by Django 4.2.7 on 2024-03-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0008_alter_companies_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='graduate_images', verbose_name='Изображение'),
        ),
    ]
