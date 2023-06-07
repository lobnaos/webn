

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # should be home page here
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, 'incorrect username or password')
            return render(request, 'registration/login.html')

    else:
        return render(request, 'registration/login.html')