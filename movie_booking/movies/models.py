from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from users.models import CustomUser


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movies/images', null=True, blank=True)
    total_seats = models.PositiveIntegerField(default=0)
    booked_seats = models.PositiveIntegerField(default=0)
    # genre = models.CharField(max_length=120)
    # director = models.CharField(max_length=200)
    # release_date = models.DateField(auto_now=True)
    # duration = models.FloatField()

    def __str__(self):
        return self.title

    def get_available_seats(self):
        return self.total_seats - self.booked_seats

    def is_seat_booked(self, seat_number):
        return self.bookedseatdetail_set.get(seat_number=seat_number)

    def get_empty_seat_numbers(self):
        booked_seat_numbers = self.bookedseatdetail_set.values_list(
            'seat_number', flat=True)
        all_seat_numbers = range(1, self.total_seats + 1)
        empty_seat_numbers = [
            seat_number for seat_number in all_seat_numbers if seat_number not in booked_seat_numbers]
        return empty_seat_numbers


class BookedSeatDetail(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False)
    booking_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f"Seat {self.seat_number} - {self.movie.title}"
