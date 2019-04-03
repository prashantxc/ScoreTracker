""" All the utility files exits there
import in view as from .utils import *
"""
from .models import *


# Capitalizing Initials
def CapitalWords(First, Second):
    Name = []
    First = First.split(" ")
    for i in First:
        Name.append(i.capitalize())
    First = " ".join(Name)
    
    Name = []
    Second = Second.split(" ")
    for i in Second:
        Name.append(i.capitalize())
    Second = " ".join(Name)

    return [First, Second]


# Arranges name alphabetically
def AlphaArrange(PlayerOne, PlayerTwo):
    Players = CapitalWords(PlayerOne, PlayerTwo)
    Players = sorted(Players)

    return (Players[0], Players[1])


# Saving match record to database
def SaveRecords(PlayerOne, PlayerTwo, Score):
    Score = int(Score)
    obj, _ = Match.objects.get_or_create(
        PlayerOne = PlayerOne, 
        PlayerTwo = PlayerTwo,
    )
    obj.Score += Score

    obj.save()