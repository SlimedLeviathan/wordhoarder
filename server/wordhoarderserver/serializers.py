from .models import Player, PlayerScore, DayData, BattleInstance
from rest_framework import serializers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields="__all__"

class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerScore
        fields="__all__"

class DayDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayData
        fields="__all__"

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleInstance
        fields="__all__"