from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from datetime import datetime

# our database classes get defined here
class Player(AbstractUser):
    custom_groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        blank=True,
    )

    # user django model has username, email and password already
    admin:bool = models.BooleanField(default=False)
    resetPasswordToken:str = models.CharField()
    resetPasswordExpire:datetime = models.DateTimeField(default=datetime.min)
    currentList:list[str] = models.JSONField(default=list)
    streak:int = models.IntegerField(default=0)
    # tracking of score to player comes from the playerscore model keeping the player id

class PlayerScore(models.Model):
    date:datetime = models.DateField()
    wordCount:int = models.IntegerField()
    longestWord:str = models.CharField()
    creativeWord:str = models.CharField()
    player = models.ManyToOneRel(Player.pk, Player, "player")

class DayData(models.Model):
    date:datetime = models.DateField()
    phrase:str = models.CharField()
    extraRules:str = models.JSONField()
    longestWord:str = models.CharField()
    creativeWord:str = models.CharField()
    wordCountData:dict[int,int] = models.JSONField()
    longestScoreData:dict[int,int] = models.JSONField()
    creativeScoreData:dict[int,int] = models.JSONField()
    playerCount:int = models.IntegerField()

class BattleInstance(models.Model):
    phrase:str = models.CharField()
    extraRules:str = models.JSONField()
    startTime:datetime = models.DateTimeField()
    battleDuration:datetime = models.DateTimeField()
    playerUUIDs:list[str] = models.JSONField()
    playerWords:dict[str,list[str]] = models.JSONField()
    teams:dict[str,list[str]] = models.JSONField()