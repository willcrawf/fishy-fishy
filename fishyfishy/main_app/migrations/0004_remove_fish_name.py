# Generated by Django 3.1.2 on 2020-10-12 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_fish_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='name',
        ),
    ]