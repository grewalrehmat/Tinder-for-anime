from rest_framework import serializers
from .models import Anime,Swipe

class AnimeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = [
            'anime_id', 'title', 'title_english', 'image_url',
            'genre', 'score', 'episodes', 'status', 'background'
        ]

class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = ['id','user','anime','swipe_type','timestamp']
        read_only_fields=['id','timestamp']