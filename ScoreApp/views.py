from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *

from .utils import AlphaArrange
from .utils import SaveRecords


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
    TeamData = Match.objects.order_by('-Score')

    return render(request, 'leaderboard.html', { 'TeamData':TeamData })