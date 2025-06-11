from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to Dealership App</h1>")

def about_view(request):
    return HttpResponse("<h1>About Us</h1><p>This is the About page.</p>")

def contact_view(request):
    return HttpResponse("<h1>Contact Us</h1><p>This is the Contact page.</p>")
