# Generated by Django 4.2 on 2023-07-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]