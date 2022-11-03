from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")