# Generated by Django 5.0.3 on 2024-03-11 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_num', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TimeField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Not yet attempted'), (1, 'In the process'), (2, 'Completed Succesfully'), (3, 'tried but failed keep trying'), (4, 'tried x times and failed')])),
                ('user_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api_app.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TimeField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Not yet attempted'), (1, 'In the process'), (2, 'Completed Succesfully'), (3, 'tried but failed keep trying'), (4, 'tried x times and failed')])),
                ('user_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api_app.myuser')),
            ],
        ),
    ]