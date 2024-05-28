from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Customer
from .forms import MyLoginForm


def admin_dashboard(request):
    movies = Movie.objects.all()
    customers = Customer.objects.all()
    context = {
        'movies': movies,
        'customers': customers,
    }
    return render(request, 'dashboard.html', context)


def user_login(request):
    if request.method == 'POST':
        # we will be getting username and password through post
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            auth_user = authenticate(request, username=cleaned_data['username'],
                                     password=cleaned_data['password'])
            if auth_user is not None:
                login(request, auth_user)
                return HttpResponse('Authenticated')
    else:
        login_form = MyLoginForm()

    return render(request, 'login.html', {'login': login_form})
