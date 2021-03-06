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

        return HttpResponseRedirect('/leaderboard/')



def Leaderboard(request):
    TeamData = Match.objects.order_by('-Score')
    if not TeamData:
        TeamData = None
    
    if TeamData is not None:
        TopMatches = [[] for _ in range(10)]
        LastScore, LastRank = None, 0
        for Matchs in TeamData:
            if LastRank <= 9:
                if LastScore is not None and Matchs.Score != LastScore:
                    if LastRank >= 9:
                        break
                    LastRank += 1
                LastScore = Matchs.Score
                TopMatches[LastRank].append(Matchs)
    else:
        TopMatches = TeamData

    return render(request, 'leaderboard.html', { 'TeamData':TopMatches })
