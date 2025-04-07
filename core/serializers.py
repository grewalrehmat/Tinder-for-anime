from rest_framework import serializers
from .models import Anime,Swipe

class AnimeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Anime
        field = ['id','title','description','genres']

class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        field = ['id','user','anime','anime_type','timestamp']
        read_only_fields=['id','timestamp']