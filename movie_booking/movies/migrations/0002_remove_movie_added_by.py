# Generated by Django 4.2 on 2023-06-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='added_by',
        ),
    ]