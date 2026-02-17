from django.urls import path
from .views import GameListCreate, GameRetrieveUpdateDestroy

urlpatterns = [
    path('games/', GameListCreate.as_view(), name='game-list'),
    path('games/<int:pk>', GameRetrieveUpdateDestroy.as_view(), name='game-detail'),
]

