from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie, BookedSeatDetail
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login')
def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})


@login_required(login_url='users:login')
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')

        if seat_number:
            # Check if the seat is available
            if movie.get_available_seats() > 0:
                # Book the seat
                movie.booked_seats += 1
                movie.save()
                messages.success(request, 'Seat booked successfully!')
            else:
                messages.error(request, 'Sorry, all seats are booked.')
    booked_seats = movie.bookedseatdetail_set.all().count()
    empty_seats = movie.total_seats - booked_seats
    context = {'movie': movie, "empty_seats": empty_seats,
               "booked_seats": booked_seats}
    return render(request, 'movie_detail.html', context)


@login_required(login_url='users:login')
def seat_status(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    booked_seats = movie.bookedseatdetail_set.all().count()
    empty_seats = movie.total_seats - booked_seats

    context = {
        'movie': movie,
        'empty_seats': empty_seats,
        'booked_seats': booked_seats
    }
    return render(request, 'seat_status.html', context)


@login_required(login_url='users:login')
def book_seat(request, movie_id):
    if request.method == 'POST':
        # Retrieve the movie instance
        movie = get_object_or_404(Movie, id=movie_id)

        # Retrieve the seat number from the POST data
        seat_number = request.POST.get('seat_number')

        # Check if the seat is already booked
        seat = BookedSeatDetail.objects.filter(
            movie=movie, seat_number=seat_number).first()
        if seat and seat.is_booked:
            # Seat is already booked, return an error response
            return JsonResponse({'status': 'error', 'message': 'Seat already booked'})

        if seat:
            # Seat exists, update the booking status
            seat.is_booked = True
            seat.save()
        else:
            # Seat does not exist, create a new seat instance and book it
            seat = BookedSeatDetail.objects.create(
                movie=movie, seat_number=seat_number, user=request.user, is_booked=True)

        # Return a success response
        return JsonResponse({'status': 'success', 'message': 'Seat booked successfully'})

    # Return an error response if the request method is not POST
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@login_required
def my_bookings(request):
    bookings = BookedSeatDetail.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def process_payment(request):
    if request.method == "POST":
        # Get payment details from the request
        card_number = request.POST.get("cardNumber")
        expiration_date = request.POST.get("expirationDate")
        cvv = request.POST.get("cvv")

        # Perform payment validation and booking logic
        # ...

        # Simulate payment success for demonstration purposes
        success = True

        # Return JSON response indicating success or failure
        return JsonResponse({"success": success})

    # Return an error response if the request method is not POST
    return JsonResponse({"success": False})


@staff_member_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movies_list')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})
