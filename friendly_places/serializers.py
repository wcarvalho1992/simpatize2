from rest_framework import serializers
from friendly_places.models import Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('id', 'name')