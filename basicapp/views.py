from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'webpages/home.html')

def about(request):
    return render(request,'webpages/about.html')

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')