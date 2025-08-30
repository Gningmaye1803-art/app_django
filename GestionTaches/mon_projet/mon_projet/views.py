from django.http import HttpResponse
from django.urls import path
from . import views

def home_view(request):
    return HttpResponse("Bonjour Maye")
