from rest_framework import serializers
from .models import Game, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user_name','comment','rating','created']


class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id','title','description','created','reviews']

