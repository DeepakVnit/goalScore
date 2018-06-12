from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Matches
from .models import Teams
from .models import Goals
from .models import Players
from .serilaizers import matchSerializers
from .serilaizers import teamSerializers
from .serilaizers import goalSerializers
from .serilaizers import playerSerializers


@api_view(['GET'])
def matches(request):
    if request.method == 'GET':
        matches = Matches.objects.all()
        match = matchSerializers(matches, many=True)
        if match:
            return Response(match.data)
        else:
            return Response([])


@api_view(['GET'])
def teams(request):
    if request.method == 'GET':
        matches = Teams.objects.all()
        match = teamSerializers(matches, many=True)
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
        match_goals = goalSerializers(goals, many=True)
        if match_goals:
            return Response(match_goals.data)
        else:
            return Response([])
