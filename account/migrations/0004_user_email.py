# Generated by Django 5.0 on 2024-02-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
