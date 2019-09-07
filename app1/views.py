from django.shortcuts import render, HttpResponse

def hello_app1(request):
    return HttpResponse("<h1>Hello from App1</h1>")