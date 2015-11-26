from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from friendly_places.models import Place
from friendly_places.serializers import PlaceSerializer
from friendly_places.utils import *

@api_view(['GET'])
def search(request):
	places = GooglePlacesQueries().prepare(request).do_request().get_results()
	serializer = PlaceSerializer(places, many=True)
	return Response(serializer.data)
