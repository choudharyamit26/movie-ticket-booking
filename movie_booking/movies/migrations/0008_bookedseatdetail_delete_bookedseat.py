# Generated by Django 4.2 on 2023-06-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_bookedseat_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedSeatDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_seats_details', to='movies.movie')),
            ],
        ),
        migrations.DeleteModel(
            name='BookedSeat',
        ),
    ]
