# Generated by Django 3.1.2 on 2020-10-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
