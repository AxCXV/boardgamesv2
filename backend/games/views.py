from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

# Create your views here.


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('-created')
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

