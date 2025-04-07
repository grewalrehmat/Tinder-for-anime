from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import Anime,Swipe
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AnimeSerializer,SwipeSerializer

def swipe_page(request):
    return render(request, 'core/swipe.html')

class AnimeToSwipeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        swiped_ids=Swipe.objects.filter(user=request.user).values_list('anime_id',flat=True) #checking if swipped already
        unswiped_id=Anime.objects.exclude(id__in=swiped_ids) #excluding the swipped ones from unswapped ones
        serializer = AnimeSerializer(unswiped_id,many=True) #sending json request
        return Response(serializer.data)

class SwipeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self ,request):
        data=request.data.copy() #copying data for referencing
        data['user']=request.user.id #injecting the user id
        serializer = SwipeSerializer(data=data) #decoding json response
        if serializer.is_valid():
            serializer.save() #save if valid
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

