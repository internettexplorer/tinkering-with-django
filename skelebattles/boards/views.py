from django.shortcuts import render

from django.http import HttpResponse
from .models import Board

# Create a view named 'home' which returns a
# http response after receiving a request
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

#

