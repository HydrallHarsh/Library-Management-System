from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

# Create your views here.


def mainScreen(request):
    return render(request, 'Home.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(username, password)
            return redirect('mainScreen')
        else:
            messages.info(request, "Invalid username or password")
            return redirect(login)
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)
        if User.objects.filter(username=username).exists():
            messages.info(
                request, "Username already exists. Try with different username.")
            return redirect('signup')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            return redirect(login)
    else:
        return render(request, 'signup.html')


def logout(request):
    auth_logout(request)
    return redirect(request ,'mainScreen')
