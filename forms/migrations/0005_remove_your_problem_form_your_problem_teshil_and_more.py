# Generated by Django 5.0.6 on 2024-08-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_remove_doctors_panel_form_teshil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='your_problem_form',
            name='Your_problem_teshil',
        ),
        migrations.RemoveField(
            model_name='your_problem_form',
            name='teshil',
        ),
    ]
