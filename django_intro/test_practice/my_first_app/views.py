from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is the equivalant of @app.route('/')")
