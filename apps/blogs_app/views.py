from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect ('/blogs_app')

def show(request, year):
    response = "placeholder to display blog " + year
    return HttpResponse(response)

def edit(request, year):
    response = "placeholder to edit blog " + year
    return HttpResponse(response)

def destroy(request, year):
    return redirect ('/blogs_app')