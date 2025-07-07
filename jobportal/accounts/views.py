from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.user.role == 'company':
        return redirect('jobs:company_jobs')
    elif request.user.role == 'applicant':
        return redirect('jobs:job_list')
    else:
        return HttpResponse("Role not defined", status=403)


def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('accounts:login')
