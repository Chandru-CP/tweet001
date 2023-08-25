from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            messages.success(request, 'Your account has been created. Please sign in.')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'django_accounts/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully signed in.')
                return render(request, 'django_homepage/homepage.html') # Replace with your homepage URL name
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = SignInForm()
    return render(request, 'django_accounts/signin.html', {'form': form})


def homepage_view(request):
    logout(request)
    messages.success(request, 'You have been successfully signed out.')
    return render(request, 'django_homepage/homepage.html') # Replace with your homepage URL name
