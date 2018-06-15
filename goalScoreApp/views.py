from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Matches
from .models import Teams
from .models import Players
from .serilaizers import MatchSerializers
from .serilaizers import TeamSerializers
from .serilaizers import PlayerSerializers


@api_view(['GET'])
def teams(request):
    if request.method == 'GET':
        matches = Teams.objects.all()
        match = TeamSerializers(matches, many=True)
        if match:
            return Response(match.data)
    return Response([])


@api_view(['GET'])
def team(request):
    if request.method == 'GET':
        team_id = request.GET.get('team', None)
        if team_id:
            team = Teams.objects.filter(id=team_id)
            if team:
                team = TeamSerializers(team, many=True)
                return Response(team.data)
    return Response([])


@api_view(['GET'])
def matches(request):
    if request.method == 'GET':
        matches = Matches.objects.all()
        match = MatchSerializers(matches, many=True)
        if match:
            return Response(match.data)
    return Response([])

# Goal in a match
@api_view(['GET'])
def match(request):
    if request.method == 'GET':
        match_id = request.GET.get('match', None)
        if match_id:
            match = Matches.objects.filter(id=match_id)
            match_goals = MatchSerializers(match, many=True)
            if match_goals:
                return Response(match_goals.data)
    return Response([])

@api_view(['GET'])
def players(request):
    if request.method == 'GET':
        team = request.GET.get('team', None)
        if team:
            players = Players.objects.filter(team_id=team)
            if players:
                playerData = PlayerSerializers(players, many=True)
                if playerData:
                    return Response(playerData.data)

    return Response([])

@api_view(['GET'])
def player(request):
    if request.method == 'GET':
        player = request.GET.get('player', None)
        if player:
            player = Players.objects.filter(id=player)
            if player:
                playerData = PlayerSerializers(player, many=True)
                if playerData:
                    return Response(playerData.data)

    return Response([])