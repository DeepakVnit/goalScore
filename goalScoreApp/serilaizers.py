from rest_framework import serializers
from .models import Matches
from .models import Goals
from .models import Players
from .models import Teams


class teamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'name', 'short_name', 'flag', 'group')


class playerSerializers(serializers.ModelSerializer):
    team = teamSerializers(read_only=True)

    class Meta:
        model = Players
        fields = ('id', 'name', 'team', 'rating', 'position')


class goalSerializers(serializers.ModelSerializer):
    scorer = playerSerializers(read_only=True)
    assist = playerSerializers(read_only=True)

    class Meta:
        model = Goals
        fields = ('id', 'scorer', 'assist', 'time', 'allowed')


class matchSerializers(serializers.ModelSerializer):
    team1 = teamSerializers(read_only=True)
    team2 = teamSerializers(read_only=True)
    goal_scored = goalSerializers(source='goals_set', many=True)

    class Meta:
        model = Matches
        fields = (
        'id', 'team1', 'team2', 'score1', 'score2', 'penality1', 'penality2', 'goal_scored', 'gametime', 'venue')
