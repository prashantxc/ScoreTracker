from django.shortcuts import render
from .models import *

# Create your views here.
def Records(request):
    return render(request, 'records.html')