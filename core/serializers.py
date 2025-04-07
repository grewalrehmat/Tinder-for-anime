from rest_framework import serializers
from .models import Anime,Swipe

class AnimeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id','title','description','genres']

class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = ['id','user','anime','swipe_type','timestamp']
        read_only_fields=['id','timestamp']