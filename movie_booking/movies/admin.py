from django.contrib import admin

# Register your models here.
from .models import Movie, BookedSeatDetail
admin.site.register(Movie)
admin.site.register(BookedSeatDetail)
