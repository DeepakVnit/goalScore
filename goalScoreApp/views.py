from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Matches
from .models import Teams
from .models import Goals
from .serilaizers import MatchSerializers
from .serilaizers import TeamSerializers
from .serilaizers import GoalSerializers


@api_view(['GET'])
def matches(request):
    if request.method == 'GET':
        matches = Matches.objects.all()
        match = MatchSerializers(matches, many=True)
        if match:
            return Response(match.data)
        else:
            return Response([])


@api_view(['GET'])
def teams(request):
    if request.method == 'GET':
        matches = Teams.objects.all()
        match = TeamSerializers(matches, many=True)
        if match:
            return Response(match.data)
        else:
            return Response([])


# Goal in a match
@api_view(['GET'])
def get_match_goals(request):
    if request.method == 'GET':
        match_id = request.GET.get('match_id', None)
        goals = Goals.objects.filter(match_id=match_id)
        match_goals = GoalSerializers(goals, many=True)
        if match_goals:
            return Response(match_goals.data)
        else:
            return Response([])