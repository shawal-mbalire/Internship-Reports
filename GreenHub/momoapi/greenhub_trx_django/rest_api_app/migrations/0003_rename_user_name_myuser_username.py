# Generated by Django 5.0.3 on 2024-03-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_myuser_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='user_name',
            new_name='username',
        ),
    ]