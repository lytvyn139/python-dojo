from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("| HELLO WORLD | PYTHON | DJANGO | Create your views here")
