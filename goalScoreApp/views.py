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

@api_view(['GET'])
def groupStanding(request):
    if request.method == 'GET':
        standing = {}
        completed_status = Matches.POSSIBLE_RESULT
        teams = Teams.objects.all()
        for team in teams:
            standing[team.name] = {"MP":0, "W":0, "L":0, "D":0, "GF":0, "GA":0, "GD": 0, "Pts": 0}

        matches_played = Matches.objects.filter(result__in=[x[0] for x in completed_status]).prefetch_related('team1', 'team2')
        for match in matches_played:
            team1 = match.team1
            team2 = match.team2
            result = match.result

            standing[team1.name]["MP"] += 1
            standing[team2.name]["MP"] += 1

            standing[team1.name]["GF"] += match.score1
            standing[team1.name]["GA"] += match.score2

            standing[team2.name]["GF"] += match.score2
            standing[team2.name]["GA"] += match.score1

            standing[team1.name]["GD"] = standing[team1.name]["GF"] - standing[team1.name]["GA"]
            standing[team2.name]["GD"] = standing[team2.name]["GF"] - standing[team2.name]["GA"]

            possible_result = [x[0] for x in Matches.POSSIBLE_RESULT]
            if result == possible_result[0]: #WON
                standing[team1.name]["W"] += 1
                standing[team2.name]["L"] += 1

            elif result == possible_result[1]: #LOST
                standing[team2.name]["W"] += 1
                standing[team1.name]["L"] += 1
            else: #DRAW
                standing[team1.name]["D"] += 1
                standing[team2.name]["D"] += 1

            standing[team1.name]["Pts"] = (standing[team1.name]["W"]*3) + (standing[team1.name]["D"]*1)
            standing[team2.name]["Pts"] = (standing[team2.name]["W"] * 3) + (standing[team2.name]["D"] * 1)

    return Response(standing)