from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *

from .utils import AlphaArrange
from .utils import SaveRecords

from django.views.decorators.csrf import csrf_exempt


def Record(request):
    return render(request, 'records.html')


def NewMatch(request):
    if request.method == 'POST':
        
        TeamOnePlayerOne = request.POST.get('TeamOnePlayerOne')
        TeamOnePlayerTwo = request.POST.get('TeamOnePlayerTwo')
        TeamOneScore = request.POST.get('TeamOneScore')
        PlayerOne, PlayerTwo = AlphaArrange(TeamOnePlayerOne, TeamOnePlayerTwo)
        SaveRecords(PlayerOne, PlayerTwo, TeamOneScore)

        TeamTwoPlayerOne = request.POST.get('TeamTwoPlayerOne')
        TeamTwoPlayerTwo = request.POST.get('TeamTwoPlayerTwo')
        TeamTwoScore = request.POST.get('TeamTwoScore')
        PlayerOne, PlayerTwo = AlphaArrange(TeamTwoPlayerOne, TeamTwoPlayerTwo)
        SaveRecords(PlayerOne, PlayerTwo, TeamTwoScore)

        return HttpResponseRedirect('/')



def Leaderboard(request):
    count = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'leaderboard.html', {'count':count})