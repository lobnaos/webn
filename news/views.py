from django.shortcuts import render

# Create your views here.
def fashion(request):
    return render(request,'news/fashion.html')

def artist(request):
    return render(request,'news/artist.html')

def nutrition(request):
    return render(request,'news/nutrition.html')

def sports(request):
    return render(request,'news/sports.html')