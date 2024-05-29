from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def transportation(request):
    return HttpResponse("Transportation")

def test(request):
    return HttpResponse("Test Url1")

def test2(request):
    return HttpResponse("Test Url2")

def test3(request):
    return HttpResponse("Test Url3")