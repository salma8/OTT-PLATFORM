from django.shortcuts import render
from .models import Movie, Customer


def admin_dashboard(request):
    movies = Movie.objects.all()
    customers = Customer.objects.all()
    context = {
        'movies': movies,
        'customers': customers,
    }
    return render(request, 'dashboard.html', context)
