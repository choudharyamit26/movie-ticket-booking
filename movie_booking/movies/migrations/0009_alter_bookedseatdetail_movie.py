# Generated by Django 4.2 on 2023-06-03 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_bookedseatdetail_delete_bookedseat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedseatdetail',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]