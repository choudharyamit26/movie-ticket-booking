# Generated by Django 4.2 on 2023-06-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movies'),
        ),
    ]