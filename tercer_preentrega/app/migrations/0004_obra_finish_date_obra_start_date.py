# Generated by Django 4.2.1 on 2023-06-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_image_obra_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='finish_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obra',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
