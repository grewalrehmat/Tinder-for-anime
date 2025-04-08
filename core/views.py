from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import Anime,Swipe
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AnimeSerializer,SwipeSerializer
from rest_framework.permissions import AllowAny
def swipe_page(request):
    return render(request, 'core/swipe.html')

class AnimeToSwipeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        anime = Anime.objects.first()
        if anime:
            serializer = AnimeSerializer(anime)
            return Response(serializer.data)
        else:
            return Response({"message": "No more anime to swipe on!"})

class SwipeAPIView(APIView):
    def post (self ,request):
        data=request.data.copy() #copying data for referencing
        data['user']=request.user.id #injecting the user id
        anime_id = data.get('anime')
        direction = data.get('direction')
        if Swipe.objects.filter(user=request.user, anime_id=anime_id).exists():
            return Response({"error": "You have already swiped on this anime!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SwipeSerializer(data=data) #decoding json response
        if serializer.is_valid():
            serializer.save() #save if valid
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)