from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def about(request):
    return render(request, 'main_app/about.html')

