from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("its working fine!")


def example(request):
    return HttpResponse("<h1>this example works too!</h1>")
