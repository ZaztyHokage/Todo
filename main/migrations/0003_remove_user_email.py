# Generated by Django 5.0 on 2024-02-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
