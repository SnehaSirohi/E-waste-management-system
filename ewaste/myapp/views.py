from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicespage")

def contact(request):
    return HttpResponse("this is contactpage")