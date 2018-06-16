from rest_framework import serializers
from .models import Matches
from .models import Goals
from .models import Players
from .models import Teams
from .models import Cards


class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'name', 'short_name', 'flag', 'group')


class PlayerSerializers(serializers.ModelSerializer):
    team = TeamSerializers(read_only=True)
    class Meta:
        model = Players
        fields = ('id', 'name', 'team', 'rating', 'position')


class GoalSerializers(serializers.ModelSerializer):
    scorer = PlayerSerializers(read_only=True)
    assist = PlayerSerializers(read_only=True)

    class Meta:
        model = Goals
        fields = ('id', 'scorer', 'assist', 'time', 'allowed')

class CardSerializers(serializers.ModelSerializer):
    player = PlayerSerializers(read_only=True)

    class Meta:
        model = Cards
        fields = ('id','card_type', 'player', 'time')

class MatchSerializers(serializers.ModelSerializer):
    team1 = TeamSerializers(read_only=True)
    team2 = TeamSerializers(read_only=True)
    team1_captain = PlayerSerializers(read_only=True)
    team2_captain = PlayerSerializers(read_only=True)
    cards_given = CardSerializers(source='cards_set', many=True, default=[])
    goal_scored = GoalSerializers(source='goals_set', many=True, default=[])

    class Meta:
        model = Matches
        fields = (
        'id','result', 'team1', 'team2', 'score1', 'score2', 'penality1', 'penality2', 'goal_scored', 'gametime', 'venue', 'team1_captain', 'team2_captain', 'cards_given')
