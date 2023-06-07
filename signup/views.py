
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    return render(request, 'home/home.html')

def SignupPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
           return HttpResponse("your password and confrom password are not same !")
        else:
            my_user = User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('login')

    return render(request,'registration/signup.html')
