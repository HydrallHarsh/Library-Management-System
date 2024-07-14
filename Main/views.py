from django.shortcuts import render

# Create your views here.
def mainScreen(request):
    return render(request, 'Home.html')