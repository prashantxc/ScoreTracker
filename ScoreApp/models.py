from django.db import models

# Create your models here.

class Match(models.Model):
    PlayerOne = models.CharField(max_length=100)
    PlayerTwo = models.CharField(max_length=100)
    Score = models.IntegerField(default=0)

    class Meta:
        unique_together = (('PlayerOne', 'PlayerTwo'),)