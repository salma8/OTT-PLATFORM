from datetime import timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Customer, Subscription
from .forms import MyLoginForm, MovieForm, SubscriptionForm


def admin_dashboard(request):
    movies = Movie.objects.all()
    customers = Customer.objects.all()
    movie_form = MovieForm()

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            Movie.objects.create(
                title=movie_form.cleaned_data['title'],
                description=movie_form.cleaned_data['description'],
                genre=movie_form.cleaned_data['genre'],
                director=movie_form.cleaned_data['director'],
                duration=movie_form.cleaned_data['duration'],
                actor=movie_form.cleaned_data['actor'],
                image=movie_form.cleaned_data['image'],
                video=movie_form.cleaned_data['video']
            )
            return redirect('admin_dashboard')  # Replace 'admin_dashboard' with your URL name
    return render(request, 'dashboard.html', {'movie_form': movie_form, 'customers': customers, 'movies': movies})


def dashboard(request):
    search_query = request.GET.get('search', '')

    if search_query:
        movies = Movie.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(genre__icontains=search_query) |
            Q(director__icontains=search_query) |
            Q(actor__icontains=search_query)
        )
        customers = Customer.objects.filter(
            Q(FirstName__icontains=search_query) |
            Q(LastName__icontains=search_query) |
            Q(Email__icontains=search_query) |
            Q(Mobile__icontains=search_query) |
            Q(Plan__icontains=search_query)
        )
    else:
        movies = Movie.objects.all()
        customers = Customer.objects.all()
    movie_form = MovieForm()

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            Movie.objects.create(
                title=movie_form.cleaned_data['title'],
                description=movie_form.cleaned_data['description'],
                genre=movie_form.cleaned_data['genre'],
                director=movie_form.cleaned_data['director'],
                duration=movie_form.cleaned_data['duration'],
                actor=movie_form.cleaned_data['actor'],
                image=movie_form.cleaned_data['image'],
                video=movie_form.cleaned_data['video']
            )
            return redirect('admin_dashboard')  # Replace 'admin_dashboard' with your URL name

    context = {
        'movies': movies,
        'customers': customers,
        'movie_form': movie_form
    }
    return render(request, 'dashboard.html', {'movie_form': movie_form})


def user_login(request):
    if request.method == 'POST':
        # we will be getting username and password through post
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():

            cleaned_data = login_form.cleaned_data
            username = cleaned_data['username']
            print(username)
            auth_user = authenticate(request, username=cleaned_data['username'],
                                     password=cleaned_data['password'])
            if auth_user is not None:
                login(request, auth_user)
                return redirect('admin-dashboard')
    else:
        login_form = MyLoginForm()

    return render(request, 'login.html', {'login': login_form})


def logout_confirmation(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to the login page after logout
    return render(request, 'logout_confirmation.html')


def subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            plan = form.cleaned_data['plan']
            subscription = Subscription.objects.get(plan=plan)
            request.user.customer.subscription = subscription
            request.user.customer.save()
            return redirect('subscription')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription.html', {'form': form})
