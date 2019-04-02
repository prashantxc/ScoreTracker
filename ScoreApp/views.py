from django.shortcuts import render
from .models import *

# Create your views here.
def Record(request):
    return render(request, 'records.html')

def Leaderboard(request):
    count = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'leaderboard.html', {'count':count})