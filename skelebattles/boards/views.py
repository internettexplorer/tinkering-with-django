from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create a view named 'home' which returns a
# http response after receiving a request
def home(request):
    return HttpResponse('Hello, World!')

