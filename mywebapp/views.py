from django.http import HttpResponse
from django.shortcuts import render

def process_home(request):
    return render(request, "index.html")

def process_main_page(request):
    return HttpResponse("This is main page.")