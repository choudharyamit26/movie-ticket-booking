from django.urls import path

from .views import movies_list, add_movie, movie_detail, seat_status, book_seat, my_bookings, process_payment
app_name = 'movies'

urlpatterns = [
    path('add-movie/', add_movie, name='add_movie'),
    path('list/', movies_list, name='movies_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('<int:movie_id>/seat-status/', seat_status, name='seat_status'),
    path('book_seat/<int:movie_id>/', book_seat, name='book_seat'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path("process_payment/", process_payment, name="process_payment"),

]
